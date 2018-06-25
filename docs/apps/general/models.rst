Models
=======

Models in the general app should not be added to if it can be avoided. Ask Nathan for details.

.. py:currentmodule:: general.models

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

.. py:class:: AMBaseModel

    :ivar DateTimeField created_at:

        The exact date/time a specific instance of a model was created at. Automatically fills. You shouldn't have to think about this.

    :ivar DateTimeField updated_at:

        The exact date/time a specific instance of a model was last updated/changed at. Automatically fills. You shouldn't have to think about this.

    :ivar JSONField extras:

        Perhaps the most important of the inherited fields, this is a ``JSONField`` key-value store of anything that doesn't fit somewhere else in a model. Use liberally. More info in the database is better than less.

-----------------------------

Person
~~~~~~

The core model to all the people-centered functionality in Access Missouri. Surprisingly simple, actually.

.. py:class:: Person

    :ivar CharField first_name:

        Self explanatory. Max length 300.

    :ivar CharField last_name:

        Self explanatory. Max length 300.

    :ivar CharField middle_name:

        Self explanatory. Max length 300. Can be blank, cannot be ``None``.

    :ivar CharField nickname:

        Pretty straightforward. If someone’s name is Joan, but they go by “Peggy,” this should be filled in, but also if someone’s name is Robert and they go by “Bob.” We use this for a lot of fuzzy object matching. Max length 300. Can be blank, cannot be ``None``.

    :ivar CharField gender:

        Free-form ``CharField``. Not really used. Can be blank, cannot be ``None``.

    :ivar CharField suffix:

        “Jr.”, “Sr.”, etc. if relevant. Max length 10. Can be blank, cannot be ``None``.

    :ivar CharField index_name:

        The least intuitive of the fields, this is a cached concatenation of the person's name fields designed to be easily queryable. Max length is 400.

    :ivar CharField flavor_text:

        Just like on a trading card, this is the text to give someone an idea of a person's character.

    .. py:method:: get_full_name()

        Returns a person's formatted full name without making you do the heavy lifting in an inconsistent way.

        :return: Full concatenated person name.
        :rtype: str

    .. py:method:: get_absolute_url()

        Concatenates absolute path (no "https://....", but "/path/to") to standard view of object.

        :return: Path to person's standard template view.
        :rtype: str

    .. py:method:: get_admin_url()

        Concatenates absolute path (no "https://....", but "/path/to") to admin interface view of object.

        :return: Path to person's standard Django admin UI view.
        :rtype: str

