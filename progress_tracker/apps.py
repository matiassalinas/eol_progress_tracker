# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import PluginSettings, PluginURLs, ProjectType, SettingsType


class ProgressTrackerConfig(AppConfig):
    name = u'progress_tracker'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: u'',
                PluginURLs.REGEX: r'^progresstracker/',
                PluginURLs.RELATIVE_PATH: u'urls',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: u'settings.common'},
            },
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: u'settings.common'},
            },
        }
    }

    def ready(self):
        pass
