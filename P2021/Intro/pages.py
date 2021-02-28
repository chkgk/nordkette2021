from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass

# ******************************************************************************************************************** #
# *** PAGE SUB INTRO BIASES T1*** #
# ******************************************************************************************************************** #
class SubIntro(Page):
    # time out
    # ----------------------------------------------------------------------------------------------------------------
    timeout_seconds = 30
    timer_text = "Verbleibende Zeit bis du automatisch weitergeleitet wirst:"

page_sequence = [Intro, SubIntro]
