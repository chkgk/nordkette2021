from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # ------------------------------------------------------------------------------------------------------------ #
        # make decisions
        # ------------------------------------------------------------------------------------------------------------ #
            yield (pages.FinLit, {'interest_compounding': random.choice([1,0,0,404]),
                                  'real_interest': random.choice([0,0,1,404]),
                                  'diversification': random.choice([0,1,404]),
                                  'bond_pricing': random.choice([0,1,0,0,404]),
                                  'credit_interest': random.choice([1,0,404])})

