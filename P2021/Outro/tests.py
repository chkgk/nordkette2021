from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        pseudo_email = str(str('bot') + str(self.participant.id_in_session) +str("@uibkbot.at"))
        yield(pages.Outro, {"e_mail_address": random.choice(["",pseudo_email])})


