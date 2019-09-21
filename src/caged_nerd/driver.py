import random
import time
import pandas as pd
from collections import namedtuple

from caged_nerd.musical_scales import ScaleCreator, CagedMapping
from caged_nerd.utils import get_execution_time


class ChordsDriver:
    def __init__(self, starting_note, mode, rounds):
        self.starting_note = starting_note
        self.mode = mode
        self.rounds = rounds
        self._message = "Play {} in the {} form"

    ChordFormTime = namedtuple("ChordFormTime", "chord, form, time")

    def main(self):
        chords = ScaleCreator(self.starting_note, self.mode).chords
        user_results = []
        for i in range(0, self.rounds):

            # choose a chord and a form
            chord = random.choice(chords)
            form = self._choose_form(chord)

            # test the user
            print("..get ready...")
            time.sleep(2)
            time_to_find_chord = user_execution(self._message, chord, form)

            user_results.append(self.ChordFormTime(chord, form, time_to_find_chord))

        df_results = pd.DataFrame.from_records(
            user_results, columns=self.ChordFormTime._fields
        )
        print(df_results)

    def _choose_form(self, chord):
        if "Minor" in chord:
            return random.choice(CagedMapping.minor)
        elif "Major" in chord:
            return random.choice(CagedMapping.major)
        else:
            return "x"


@get_execution_time
def user_execution(message, *args):
    print(message.format(*args))
    input("Then press enter...")
    print("-" * 80)
