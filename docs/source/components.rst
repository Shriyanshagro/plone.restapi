Components
==========

.. warning::
   The @components endpoint is deprecated and will be removed in plone.restapi
   1.0b1. :doc:`breadcrumbs` and :doc:`navigation` are now top-level endpoints.

How to get pages components (i.e. everything but the main content), like breadcrumbs, navigations, actions, etc.


Breadcrumbs
-----------

Getting the breadcrumbs for the current page:

..  http:example:: curl httpie python-requests
    :request: _json/breadcrumbs.req

Example response:

.. literalinclude:: _json/breadcrumbs.resp
   :language: http

Navigation
-------------------------

Getting the top navigation items:

..  http:example:: curl httpie python-requests
    :request: _json/navigation.req

Example response:

.. literalinclude:: _json/navigation.resp
   :language: http
