from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):

        yield (pages.Field_Behavior, {"gambling": random.randint(1,5),
                                     "general_risk": random.randint(0,10),
                                     "saving": random.randint(1,5),
                                     "temptation": random.randint(1,5)})

        yield (pages.Perception_Questions, {"financial_troubles": random.randint(1,5),
                                            "fin_education_school": random.randint(1,5),
                                            "fin_education_parents": random.randint(1,5)})

        yield (pages.SubIntroB2)
