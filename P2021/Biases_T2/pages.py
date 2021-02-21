from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE DECOY *** #
# ******************************************************************************************************************** #
class Decoy(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds_t2']['A']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['decoy_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }


# ******************************************************************************************************************** #
# *** PAGE ANCHORING *** #
# ******************************************************************************************************************** #
class Anchoring(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds_t2']['B']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['anchoring_t2_buy','anchoring_t2_wtp']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }



# ******************************************************************************************************************** #
# *** PAGE FRAMING *** #
# ******************************************************************************************************************** #
class Framing(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds_t2']['C']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['framing_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }

# ******************************************************************************************************************** #
# *** PAGE MENTAL ACCOUNTING *** #
# ******************************************************************************************************************** #
class MentalAccounting(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds_t2']['D']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['mental_accounting_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }


page_sequence = [Decoy, Anchoring, Framing, MentalAccounting]
