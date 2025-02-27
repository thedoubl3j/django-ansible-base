from django.apps import AppConfig

import ansible_base.lib.checks  # noqa: F401 - register checks


class RestFiltersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ansible_base.rest_filters'
    label = 'dab_rest_filters'
