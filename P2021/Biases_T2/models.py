from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import itertools
import json


author = 'Armando Holzknecht'

doc = """
Treatment 2 for biases Decoy, Anchoring, Framing, Mental Accounting and Conjunction Fallacy
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Biases_T2'
    players_per_group = None
    num_rounds = 1

# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def creating_session(self):
        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
            random.shuffle(pb)
            p.page_sequence_t2 = str(p.participant.vars["task_sequence"][:-23:]) + str(p.participant.vars["task_sequence"][-1:])#without conjunction fallacy

# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    page_sequence_t2 = models.StringField()
    decoy_t2 = models.StringField()
    anchoring_t2_wtp = models.FloatField()
    anchoring_t2_buy = models.IntegerField()
    framing_t2 = models.StringField()
    mental_accounting_t2 = models.IntegerField()
