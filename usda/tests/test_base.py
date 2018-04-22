#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for Data.gov API features"""

import pytest
from httmock import urlmatch, HTTMock
from requests import HTTPError
from usda.base import api_request, DataGovClientBase, \
    DataGovApiError, DataGovApiRateExceededError


class TestBase(object):
    """Unit tests for base Data.gov features"""

    @urlmatch(path=r'/?ok.*')
    def api_ok(self, url, request):
        return {
            'status_code': 200,
            'content': '{"key": "value"}'
        }

    @urlmatch(path=r'/?param.*')
    def api_parameter_error(self, url, request):
        return {
            'status_code': 400,
            'content': '{"errors": {"error": [{'
                       '"status": 400, "parameter": "name",'
                       '"message": "something"}]}}'
        }

    @urlmatch(path=r'/?rate.*')
    def api_rate_limit_error(self, uri, request):
        return {
            'status_code': 429,
            'content': '{"error": {"code": "OVER_RATE_LIMIT", '
                       '"message": "API rate limit exceeded"}}'
        }

    @urlmatch(path=r'/?error.*')
    def api_unknown_error(self, uri, request):
        return {
            'status_code': 418,
            'content': '{"error": {"code": "CODE", "message": "message"}}'
        }

    @urlmatch(path=r'/?httperror.*')
    def api_http_error(self, uri, request):
        return {'status_code': 500, 'content': 'oh no'}

    @pytest.fixture
    def apimock(self):
        """Pytest Fixture to provide a HTTMock that will return fake responses
        to test API features"""
        return HTTMock(self.api_ok,
                       self.api_parameter_error,
                       self.api_rate_limit_error,
                       self.api_unknown_error,
                       self.api_http_error)

    def test_api_request_ok(self, apimock):
        """Test api_request with a normal working response."""
        with apimock:
            data = api_request("http://api/ok")
        assert data["key"] == "value"

    def test_api_request_parameter_error(self, apimock):
        """Test api_request with a parameter value error"""
        with pytest.raises(ValueError, match='something'):
            with apimock:
                api_request("http://api/param")

    def test_api_request_rate_limit_error(self, apimock):
        """Test api_request with an API rate limit exceeded error"""
        with pytest.raises(DataGovApiRateExceededError):
            with apimock:
                api_request("http://api/rate")

    def test_api_request_other_error(self, apimock):
        """Test api_request with an unknown API error"""
        with pytest.raises(DataGovApiError, match='CODE: message'):
            with apimock:
                api_request("http://api/error")

    def test_api_request_http_error(self, apimock):
        """Test api_request with a HTTP error code with no JSON"""
        with pytest.raises(HTTPError):
            with apimock:
                api_request("http://api/httperror")
