Management Commands
===================

As primary business logic, management tasks generally should not be stored in the general app.

--------------------

person_full_name_to_index_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A task that should eventually be deprecated and relegegated to model managers and aggregation, this creates an easily-queryable version of someone's name and stores it in a searchable format.

Behind the scenes, what's happening is a bunch of conditional concatenation, then it's getting stored in the Person model's `index_name` field.

Example
```````

Run the task:

.. code-block:: sh

	$ python manage.py person_full_name_to_index_name