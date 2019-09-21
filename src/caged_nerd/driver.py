import random
import time
import pandas as pd
from collections import namedtuple

from caged_nerd.musical_scales import ScaleCreator, CagedMapping
from caged_nerd.utils import get_execution_time

class ChordsDriver():
    def __init__(self, starting_note, mode, rounds):
        self.starting_note = starting_note
        self.mode = mode
        self.rounds = rounds
        self._message = 'Play {} in the {} form'

    ChordFormTime = namedtuple('ChordFormTime', 'chord, form, time')

    def main(self):
        chords = ScaleCreator(self.starting_note, self.mode).chords
        user_results = []
        for i in range(0, self.rounds):
            # make this a random choice with weights
            chord = random.choice(chords)
            form = self._choose_form(chord)
            # user input goes here
            time_to_find_chord = time_user_execution(self._message, chord, form)
            user_results.append(self.ChordFormTime(chord, form, time_to_find_chord))
            time.sleep(0)

        df_results = pd.DataFrame.from_records(user_results,
                                               columns=self.ChordFormTime._fields)
        print(df_results)


    def _choose_form(self, chord):
        if 'Minor' in chord:
            return random.choice(CagedMapping.minor)
        elif 'Major' in chord:
            return random.choice(CagedMapping.major)
        else:
            return 'x'

@get_execution_time
def time_user_execution(message, *args):
    print(message.format(*args))
    timed_input = input('Then press enter...')


