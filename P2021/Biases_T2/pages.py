from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import json

# ******************************************************************************************************************** #
# *** PAGE DECOY *** #
# ******************************************************************************************************************** #
class Decoy(Page):
    def before_next_page(self):
        self.participant.vars["page_count"] += 1

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
        page = self.participant.vars["page_count"]
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
    def before_next_page(self):
        self.participant.vars["page_count"] += 1

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
        page = self.participant.vars["page_count"]
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
    def before_next_page(self):
        self.participant.vars["page_count"] += 1

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
        page = self.participant.vars["page_count"]
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
    def before_next_page(self):
        self.participant.vars["page_count"] += 1

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
        page = self.participant.vars["page_count"]
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }


initial_page_sequence = [
    Decoy,
    Anchoring,
    Framing,
    MentalAccounting,
]

#compute page sequence
page_sequence = [

]

class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence_t2)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])
