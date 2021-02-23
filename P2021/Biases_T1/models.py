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
Treatment 1 for biases Decoy, Anchoring, Framing, Mental Accounting and Conjunction Fallacy
"""


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Biases_T1'
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
            p.page_sequence_t1 = json.dumps(random.choice([['Decoy','Anchoring','Framing','MentalAccounting','ConjunctionFallacy'],
                                                       ['MentalAccounting','Framing','Anchoring','Decoy','ConjunctionFallacy'],
                                                        ['Framing','Anchoring','Decoy','MentalAccounting','ConjunctionFallacy']]))
            p.participant.vars["page_count"] = 1
            p.participant.vars["task_sequence"] = p.page_sequence_t1



# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    page_sequence_t1 = models.StringField()
    decoy_t1 = models.StringField()
    anchoring_t1_wtp = models.FloatField()
    framing_t1 = models.StringField()
    mental_accounting_t1 = models.IntegerField()
    conjunction_fallacy = models.IntegerField()



