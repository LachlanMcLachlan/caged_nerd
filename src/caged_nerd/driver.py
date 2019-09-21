from caged_nerd.musical_scales import ScaleCreator, CagedMapping
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
            # make this a random choice with weights
            chord = random.choice(chords)
            form = self._choose_form(chord)
            # user input goes here
            print(f'Play {chord} in the {form} form')
            input('Press enter once you\'ve found the chord...)
            time.sleep(2)


    def _choose_form(self, chord):
        if 'Minor' in chord:
            return random.choice(CagedMapping.minor)
        elif 'Major' in chord:
            return random.choice(CagedMapping.major)
        else:
            return 'x'
