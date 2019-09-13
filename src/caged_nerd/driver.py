from caged_nerd.musical_scales import ScaleCreator
import random
import time

class ChordsDriver():
    def __init__(self, starting_note, mode, rounds):
        self.starting_note = starting_note
        self.mode = mode
        self.rounds = rounds

    def main(self):
        chords = ScaleCreator(self.starting_note, self.mode).chords
        for i in range(0, self.rounds):
            print(random.choice(chords))
            time.sleep(5)