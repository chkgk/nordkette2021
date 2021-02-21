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
    poss_task_sequences = [["A","B","C","D","E"], ["D","C","B","A","E"], ["C","B","A","D","E"]]
    num_rounds = 5

# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            #define page counter and task sequence
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                task_sequence = random.choice(Constants.poss_task_sequences)
                p.participant.vars["task_sequence_t1"] = task_sequence
                p.participant.vars["task_rounds"] = dict(zip(task_sequence,round_numbers))
                p.participant.vars["page_count"] = 0


# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    task_sequence = models.StringField()
    decoy_t1 = models.StringField()
    anchoring_t1_wtp = models.IntegerField()
    framing_t1 = models.StringField()
    mental_accounting_t1 = models.IntegerField()
    conjunction_fallacy = models.IntegerField()



