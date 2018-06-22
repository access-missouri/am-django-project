Models
=======

Models in the general app should not be added to if it can be avoided. Ask Nathan for details.


-------------------------

AMBaseModel
~~~~~~~~~~~

This is the abstract model all Access Missouri models inherit from, which means all models get the following characteristics.

.. note::

	``AMBaseModel`` is intended to be an abstract model. Do not create instances of it, but make sure every single Access Missouri model does implement it. The canned functionality can save your bacon.

**Model Fields:**

* ``created_at`` - ``DateTimeField`` with the exact date/time a specific instance of a model was created at. Automatically fills. You shouldn't have to think about this.

* ``updated_at`` - ``DateTimeField`` with the exact date/time a specific instance of a model was last updated/changed at. Automatically fills. You shouldn't have to think about this.

* ``extras`` - Perhaps the most important of the inherited fields, this is a ``JSONField`` key-value store of anything that doesn't fit somewhere else in a model. Use liberally. More info in the database is better than less.

-----------------------------

Person
~~~~~~

The core model to all the people-centered functionality in Access Missouri. Surprisingly simple, actually.

**Model Fields:**

* ``first_name`` - Self explanatory. Type is ``CharField``, max length 300.
* ``middle_name`` - Self explanatory. Type is ``CharField``, max length 300. Can be blank, cannot be ``None``.
* ``last_name`` - Self explanatory. Type is ``CharField``, max length 300.
* ``suffix`` - "Jr.", "Sr.", etc. if relevant. Type is ``CharField``, max length **10**. Can be blank, cannot be ``None``.
* ``nickname`` - Pretty straightforward. If someone's name is Joan, but they go by "Peggy," this should be filled in, but also if someone's name is Robert and they go by "Bob." We use this for a lot of fuzzy object matching. Type is ``CharField``, max length 300. Can be blank, cannot be ``None``.
* ``gender`` - Free-form ``CharField``. Not really used. Can be blank, cannot be ``None``.
* ``index_name`` - The least intuitive of the fields, this is a cached concatenation of the person's name fields designed to be easily queryable. Max length is 400.

**Model Methods:**

* ``get_full_name()`` - Returns a person's formatted full name without making you do the heavy lifting in an inconsistent way.
* ``get_absolute_url()``
* ``get_admin_url()`` - Like ``get_absolute_url()`` but for Django admin.