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
Introduction
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['task'] = []
            p.participant.vars['task_total'] = 6



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
