"""
Settings and configuration for FastAPI.

Read values from the module specified by the XIAOAPI_SETTINGS_MODULE environment
variable, and then from xiaoapi.conf.global_settings; see the global_settings.py
for a list of all possible variables.

参考django源码：https://github.com/django/django/blob/main/django/conf/__init__.py
"""

import importlib
import os

from . import global_settings


ENVIRONMENT_VARIABLE = "XIAOAPI_SETTINGS_MODULE"


class Settings:
    def __init__(self, settings_module):
        # update this dict from global settings (but only for ALL_CAPS settings)
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))

        # store the settings module in case someone later cares
        self.SETTINGS_MODULE = settings_module

        mod = importlib.import_module(self.SETTINGS_MODULE)

        tuple_settings = (
            "EVENTS",
            "MIDDLEWARES",
        )
        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                if setting in tuple_settings and not isinstance(
                    setting_value, list
                ):
                    raise ValueError(
                        "The %s setting must be a list." % setting
                    )
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            "cls": self.__class__.__name__,
            "settings_module": self.SETTINGS_MODULE,
        }


def get_settings(name=None):
    settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
    if not settings_module:
        desc = ("setting %s" % name) if name else "settings"
        raise ValueError(
            "Requested %s, but settings are not configured. "
            "You must define the environment variable %s "
            "before accessing settings."
            % (desc, ENVIRONMENT_VARIABLE)
        )

    return Settings(settings_module)


settings = get_settings()
