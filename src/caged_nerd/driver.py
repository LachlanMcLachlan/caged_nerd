import random
import time
from collections import namedtuple

import pandas as pd
from caged_nerd.musical_scales import CagedMapping, ScaleCreator
from caged_nerd.utils import get_execution_time

class ChordsDriver:
    def __init__(self, starting_note, mode, rounds):
        """
        Driver containing functionality for testing how quickly the user can find
        forms of chords in a given key using the CAGED system.
        Args:
            starting_note (str): the root note of the scale
            mode (str): the mode in which to play
            rounds (int): the number of chords to test
        """
        self.starting_note = starting_note
        self.mode = mode
        self.rounds = rounds
        self._message = "Play {} in the {} form"
        self._chords = ScaleCreator(self.starting_note, self.mode).chords

    ChordFormTime = namedtuple("ChordFormTime", "chord, form, time")

    def main(self):
        """
        Runs the ChordDriver pipeline: asks the user to play a certain number
        of chords in a given key and summarizes results.
        Returns:
            None

        """
        self.print_starting_message()
        user_results = []
        for i in range(0, self.rounds):

            # choose a chord and a form
            chord = random.choice(self._chords)
            form = self._choose_form(chord)

            # test the user
            print("-" * 80)
            print(" ... get ready ... ")
            print("-" * 80)
            time.sleep(5)
            time_to_find_chord = user_execution(self._message, chord, form)

            user_results.append(self.ChordFormTime(chord, form, time_to_find_chord))

        df_results = pd.DataFrame.from_records(
            user_results, columns=self.ChordFormTime._fields
        )

        df_results.sort_index(by="time", axis=0, ascending=True, inplace=True)

        print("Well done! Here's how you did, from fastest to slowest ... ")

        print(df_results)

    def print_starting_message(self):
        chords = ", ".join(self._chords)
        print(
            f"You're gonna be asked to find {self.rounds} chords "
            f"in {self.starting_note} {self.mode}... \n"
            f"The chords in {self.starting_note} {self.mode} are: "
            f"{chords}"
        )
        input("Press enter/return to begin...")

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
    input("Then press enter ... ")
    print("Nice!")
