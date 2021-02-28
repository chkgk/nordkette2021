from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.participant.vars["task_sequence"][:3] == """["D""": # Sequence starting with Decoy
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'decoy_t2': random.choice(['C', 'D', 'T'])}) #Decoy
            yield (pages.Page_1, random.choice(({"anchoring_t2_buy" : 0,
                                                 'anchoring_t2_wtp': random.randint(0,75)},
                                                {"anchoring_t2_buy" :1,
                                                 'anchoring_t2_wtp': random.randint(76,100)}))) #Anchoring
            yield (pages.Page_2, {'framing_t2': random.choice(['A','B'])}) # Framing
            yield (pages.Page_3, {'mental_accounting_t2': random.randint(0,1)}) # MA

        elif self.participant.vars["task_sequence"][:3] == """["M""": # Sequence starting with Mental Accounting
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'mental_accounting_t2': random.randint(0,1)}) # MA
            yield (pages.Page_1, {'framing_t2': random.choice(['A','B'])}) # Framing
            yield (pages.Page_2, random.choice(({"anchoring_t2_buy":0,
                                                 'anchoring_t2_wtp': random.randint(0, 75)},
                                                {"anchoring_t2_buy": 1,
                                                 'anchoring_t2_wtp': random.randint(76, 100)}))) # Anchoring
            yield (pages.Page_3, {'decoy_t2': random.choice(['C', 'D', 'T'])})  # Decoy

        elif self.participant.vars["task_sequence"][:3] == """["F""": # Sequence starting with Framing
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.Page_0, {'framing_t2': random.choice(['A','B'])}) #Framing
            yield (pages.Page_1, random.choice(({"anchoring_t2_buy": 0,
                                                 'anchoring_t2_wtp': random.randint(0, 75)},
                                                {"anchoring_t2_buy": 1,
                                                 'anchoring_t2_wtp': random.randint(76, 100)}))) # Anchoring
            yield (pages.Page_2, {'decoy_t2': random.choice(['C', 'D', 'T'])})  # Decoy
            yield (pages.Page_3, {'mental_accounting_t2': random.randint(0,1)}) # MA

