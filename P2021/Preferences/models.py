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
Risk and time preferences
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Preferences'
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
    risk_preference = models.IntegerField()
    fail_counter_heads = models.IntegerField()
    fail_counter_tails = models.IntegerField()

    time_preference_1 = models.IntegerField()
    time_preference_2 = models.IntegerField()
    time_preference_3 = models.IntegerField()
    time_preference_4 = models.IntegerField()
    time_preference_5 = models.IntegerField()
    time_preference_6 = models.IntegerField()
