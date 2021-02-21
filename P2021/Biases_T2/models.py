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
    num_rounds = 4

# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            #define page counter and task sequence
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                if p.participant.vars["task_sequence_t1"] == ['A', 'B', 'C', 'D', 'E']:
                    p.participant.vars["task_rounds_t2"] = dict(zip(['A', 'B', 'C', 'D'],round_numbers))

                elif p.participant.vars["task_sequence_t1"] == ['C', 'B', 'A', 'D', 'E']:
                    p.participant.vars["task_rounds_t2"] = dict(zip(['C', 'B', 'A', 'D'],round_numbers))
                else:
                    p.participant.vars["task_rounds_t2"] = dict(zip(["D","C","B","A"],round_numbers))
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
    decoy_t2 = models.StringField()
    anchoring_t2_wtp = models.IntegerField()
    anchoring_t2_buy = models.IntegerField()
    framing_t2 = models.StringField()
    mental_accounting_t2 = models.IntegerField()
