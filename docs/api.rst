API Reference
=============

.. contents::
   :local:
   :backlinks: none

Client
------

.. autoclass:: usda.client.UsdaClient
   :members:

Domain
------

Base classes
^^^^^^^^^^^^

.. autoclass:: usda.domain.UsdaObject
   :members:

.. autoclass:: usda.domain.ListItem
   :members:

Items
^^^^^

.. autoclass:: usda.domain.Food
   :members:

.. autoclass:: usda.domain.Nutrient
   :members:

.. autoclass:: usda.domain.Measure
   :members:

Food Reports
^^^^^^^^^^^^

.. autoclass:: usda.domain.FoodReport
   :members:

.. autoclass:: usda.domain.FoodReportV2
   :members:

.. autoclass:: usda.domain.Source
   :members:

Nutrient Reports
^^^^^^^^^^^^^^^^

.. autoclass:: usda.domain.NutrientReportFood
   :members:

Enums
-----

.. automodule:: usda.enums
   :members: UsdaUriActions, UsdaNdbListType, UsdaNdbReportType,
      UsdaNdbDataSource

Low level classes
-----------------

Base client
^^^^^^^^^^^

.. autodata:: usda.base.BASE_URI

.. autoclass:: usda.base.DataGovClientBase
   :members:

.. autofunction:: usda.base.api_request

Exceptions
^^^^^^^^^^

.. autoexception:: usda.base.DataGovApiError
   :members:

.. autoexception:: usda.base.DataGovApiRateExceededError
   :members:

.. autoexception:: usda.base.DataGovInvalidApiKeyError
   :members:

Pagination
^^^^^^^^^^

All USDA NDB list API responses are paginated ; to help users not deal with
pagination, some specific generators ("paginators") have been created.
They are designed to be lazy and will only make requests when necessary.

.. automodule:: usda.pagination
   :members: RawPaginator, ModelPaginator, RawNutrientReportPaginator
