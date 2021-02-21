from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE DECOY *** #
# ******************************************************************************************************************** #
class Decoy(Page):
    def is_displayed(self):
        self.participant.vars["page_count"] += 1
        return self.round_number == self.participant.vars['task_rounds']['A']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['decoy_t1']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
        self.participant.vars["page_count"] += 1
        return self.round_number == self.participant.vars['task_rounds']['B']


    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['anchoring_t1_wtp']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
        self.participant.vars["page_count"] += 1
        return self.round_number == self.participant.vars['task_rounds']['C']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['framing_t1']

    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
        self.participant.vars["page_count"] += 1
        return self.round_number == self.participant.vars['task_rounds']['D']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['mental_accounting_t1']

    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
# *** PAGE CONJUNCTION FALLACY *** #
# ******************************************************************************************************************** #
class ConjunctionFallacy(Page):
    def before_next_page(self):
        self.player.task_sequence = str(self.participant.vars["task_sequence_t1"])
        #print(str(self.participant.vars["task_sequence_t1"]))
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['E']

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['conjunction_fallacy']

    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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


#compute page sequence
page_sequence = [Decoy,Anchoring,Framing,MentalAccounting,ConjunctionFallacy]
