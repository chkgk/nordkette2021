from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        # ------------------------------------------------------------------------------------------------------------ #
        # submit Intro page
        # ------------------------------------------------------------------------------------------------------------ #
        yield (pages.Intro, {"class_identifier": "TestKlasse",
                             "school_identifier": "BotSchule"})
        yield (pages.SubIntro)
