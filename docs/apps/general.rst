general
=======

If I were re-architecting Access Missouri tomorrow, we wouldn't have an app named "general." It's a minor disaster to manage.

Most of the logic and models stored in general are broad enough that they're dependencies for several other apps. General also houses person and organization models.

.. toctree::
   :maxdepth: 2

   general/models
   general/management-commands