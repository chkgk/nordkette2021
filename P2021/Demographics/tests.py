from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        #function for generating dictionaries
        def gen_dictionaries(school_type,min_age,max_age, school_level_min, school_level_max):
            return {"age": random.randint(min_age, max_age),
                    "gender": random.choice(["female", "male", "diverse"]),
                    "religion": random.choice(["rom.-cath.", "orthodox", "islamic", "protestant", "other","without"]),
                    "school_type": str(school_type),
                    "school_level": str(random.randint(school_level_min, school_level_max)),
                    "math_skill": random.choice(["1", "2", "3", "4", "5"]),
                    "german_skill": random.choice(["1", "2", "3", "4", "5"]),
                    "education_mother": random.choice(["1", "2", "3", "4", "5", "0"]),
                    "education_father": random.choice(["1", "2", "3", "4", "5", "0"])}

        yield (pages.Demographics, random.choice([gen_dictionaries("ms",8,14,5,8),
                                                  gen_dictionaries("ahs_lower",8,14,5,9),
                                                  gen_dictionaries("poly",14,15,9,9),
                                                  gen_dictionaries("vocational",15,22,10,13),
                                                  gen_dictionaries("ahs_higher",14,22,9,12),
                                                  gen_dictionaries("bms_bhs",14,25,9,13)]))
