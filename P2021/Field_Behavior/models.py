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


author = 'Armando Holzknecht & Emanuel Schöpf'

doc = """
Field Behavior tasks and perception questions
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Field_Behavior'
    players_per_group = None
    num_rounds = 1

# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    pass

# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    gambling = models.IntegerField(blank=True)
    general_risk = models.IntegerField(blank=True)
    saving = models.IntegerField(blank=True)
    temptation = models.IntegerField(blank=True)

    financial_troubles = models.IntegerField(blank=True)
    fin_education_school = models.IntegerField(blank=True)
    fin_education_parents = models.IntegerField(blank=True)
