from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.participant.vars["task_sequence_t1"] == ["A","B","C","D","E"]:
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            if self.round_number == 1:
                yield (pages.Decoy, {'decoy_t1': random.choice(['C', 'D', 'T'])})
            elif self.round_number == 2:
                yield (pages.Anchoring, {'anchoring_t1_wtp': random.randint(0,100)})
            elif self.round_number == 3:
                yield (pages.Framing, {'framing_t1': random.choice(['A','B'])})
            elif self.round_number == 4:
                yield (pages.MentalAccounting, {'mental_accounting_t1': random.randint(0,1)})
            elif self.round_number == 5:
                yield (pages.ConjunctionFallacy, {'conjunction_fallacy': random.randint(0,1)})

        elif self.participant.vars["task_sequence_t1"] == ["D","C","B","A","E"]:
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            if self.round_number == 1:
                yield (pages.MentalAccounting, {'mental_accounting_t1': random.randint(0,1)})
            elif self.round_number == 2:
                yield (pages.Framing, {'framing_t1': random.choice(['A','B'])})
            elif self.round_number == 3:
                yield (pages.Anchoring, {'anchoring_t1_wtp': random.randint(0, 100)})
            elif self.round_number == 4:
                yield (pages.Decoy, {'decoy_t1': random.choice(['C', 'D', 'T'])})
            elif self.round_number == 5:
                yield (pages.ConjunctionFallacy, {'conjunction_fallacy': random.randint(0,1)})

        elif self.participant.vars["task_sequence_t1"] == ["C","B","A","D","E"]:
            # ------------------------------------------------------------------------------------------------------------ #
            # make decisions
            # ------------------------------------------------------------------------------------------------------------ #
            if self.round_number == 1:
                yield (pages.Framing, {'framing_t1': random.choice(['A','B'])})
            elif self.round_number == 2:
                yield (pages.Anchoring, {'anchoring_t1_wtp': random.randint(0,100)})
            elif self.round_number == 3:
                yield (pages.Decoy, {'decoy_t1': random.choice(['C', 'D', 'T'])})
            elif self.round_number == 4:
                yield (pages.MentalAccounting, {'mental_accounting_t1': random.randint(0,1)})
            elif self.round_number == 5:
                yield (pages.ConjunctionFallacy, {'conjunction_fallacy': random.randint(0,1)})


