sarscov2
========

Add to an EDC_, for example the meta_edc_ for the META Trial.

Add to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        "sarscov2.apps.AppConfig",
        ...
        ]

Add the CRF to the visit schedule as a PRN, for example:

.. code-block:: python

    crfs_prn = FormsCollection(
        ...
        Crf(show_order=70, model="meta_subject.coronakap"),
        name="prn",
    )

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

To include in a screening or subject lsitboard:

.. code-block:: html

        {% if perms.sarscov2 %}
            {% if result.coronavirus_kap %}
            <a class="btn btn-sm btn-success" title="Edit Coronavirus KAP"
               href="{% url 'sarscov2_admin:sarscov2_coronaviruskap_change' result.coronavirus_kap.id %}?next=meta_dashboard:screening_listboard_url">Edit</a>
            {% else %}
            <a class="btn btn-sm btn-warning" title="Add Coronavirus KAP"
               href="{% url 'sarscov2_admin:sarscov2_coronaviruskap_add' %}?screening_identifier={{result.screening_identifier}}&next=meta_dashboard:screening_listboard_url">Add</a>
            {% endif %}
        {% endif %}


.. _EDC: https://github.com/clinicedc

.. _meta_edc: https://meta-trial/meta_edc
