from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):

        def gen_dict_tp(a,b):
            tp_dict = dict()
            for k,v in zip(a,b):
                tp_dict[("time_preference_{i}".format(i=k))] = v
            return tp_dict

        yield (pages.RiskPreference, {"risk_preference": random.randint(0,6),
                                      "fail_counter_heads": random.randint(0,2),
                                      "fail_counter_tails": random.randint(0,2)})
        yield (pages.TimePreference, random.choice([
            gen_dict_tp(list(range(1, 7)), ["B", "B", "B", "B", "B", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "B", "B", "B", "B", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "A", "B", "B", "B", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "A", "A", "B", "B", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "A", "A", "A", "B", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "A", "A", "A", "A", "B"]),
            gen_dict_tp(list(range(1, 7)), ["A", "A", "A", "A", "A", "A"]),
        ]))

