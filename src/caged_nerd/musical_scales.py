# this module contains all the musical intervals

major_scale = 'T, T, S, T, T, T, S'

class Intervals(object):
    def __init__(self, starting_note):
        self._starting_note = starting_note

    notes = 'A, B flat, B, C, D flat, D, E flat, E, F, G flat, G'.split(', ')

    def tone(self):
