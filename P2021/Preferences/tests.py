from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        yield (pages.RiskPreference, {"risk_preference": random.randint(0,6),
                                      "fail_counter_heads": random.randint(0,2),
                                      "fail_counter_tails": random.randint(0,2)})
