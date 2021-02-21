from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE RISK PREFERENCE *** #
# ******************************************************************************************************************** #
class RiskPreference(Page):
    #specify form models and form fields
    form_model = models.Player
    form_fields = []

    def vars_for_template(self):
        # specify info for task progress
        section = 3
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 2
        page = 1
        progress = page / total * 100

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class TimePreference(Page):
    #specify form models and form fields
    form_model = models.Player
    form_fields = []

    def vars_for_template(self):
        # specify info for task progress
        section = 3
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 2
        page = 2
        progress = page / total * 100

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }


page_sequence = [RiskPreference, TimePreference]
