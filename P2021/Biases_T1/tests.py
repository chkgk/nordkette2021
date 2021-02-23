from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.participant.vars["task_sequence"][:3] == """["D""":
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'decoy_t1': random.choice(['C', 'D', 'T'])}) #Decoy
            yield (pages.Page_1, {'anchoring_t1_wtp': random.randint(0,100)}) #Anchoring
            yield (pages.Page_2, {'framing_t1': random.choice(['A','B'])}) #Framing
            yield (pages.Page_3, {'mental_accounting_t1': random.randint(0,1)}) # MA
            yield (pages.Page_4, {'conjunction_fallacy': random.randint(0,1)})# CJ

        elif self.participant.vars["task_sequence"][:3] == """["M""":
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'mental_accounting_t1': random.randint(0,1)}) # MA
            yield (pages.Page_1, {'framing_t1': random.choice(['A','B'])}) #Framing
            yield (pages.Page_2, {'anchoring_t1_wtp': random.randint(0, 100)})  # Anchoring
            yield (pages.Page_3, {'decoy_t1': random.choice(['C', 'D', 'T'])})  # Decoy
            yield (pages.Page_4, {'conjunction_fallacy': random.randint(0,1)})# CJ

        elif self.participant.vars["task_sequence"][:3] == """["F""":
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'framing_t1': random.choice(['A','B'])}) #Framing
            yield (pages.Page_1, {'anchoring_t1_wtp': random.randint(0, 100)})  # Anchoring
            yield (pages.Page_2, {'decoy_t1': random.choice(['C', 'D', 'T'])})  # Decoy
            yield (pages.Page_3, {'mental_accounting_t1': random.randint(0,1)}) # MA
            yield (pages.Page_4, {'conjunction_fallacy': random.randint(0,1)})# CJ


