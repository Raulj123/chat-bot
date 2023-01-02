import re
import random

R_EATING = "I dont like eating anything cus I am a Bot"

def unkown():
    response= ['Could you please re-phrase that?',
               "....huh",
               "Whatchu mean",
               "What does that mean?"][random.randrange(4)]
    return response