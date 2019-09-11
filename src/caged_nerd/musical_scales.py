import numpy as np

class Modes:
    ionian = 'ionian'
    major = 'major'
    dorian = 'dorian'
    phrygian = 'phrygian'
    lydian = 'lydian'
    mixolydian = 'mixolydian'
    aeolian = 'aeolian'
    minor = 'minor'
    locrian = 'locrian'

class ModeMapping():
    modes = {Modes.major: 0, Modes.ionian: 0, Modes.dorian: 1, Modes.phrygian: 2,
             Modes.lydian: 3, Modes.mixolydian: 4,
             Modes.aeolian: 5, Modes.minor: 5, Modes.locrian: 6}

# class ChordMapping():
#     # maps the mode number to the chords available for that mode
#      modes = {
#          ModeMapping.modes[Modes.ionian]: ['major', 'maj7'],
#          ModeMapping.modes[Modes.major]: ['major', 'maj7'],
#          ModeMapping.modes[Modes.dorian]: ['m', 'm7'],
#          ModeMapping.modes[Modes.phrygian]: ['m', 'm7'],
#          ModeMapping.modes[Modes.lydian]: ['major', 'maj7'],
#          ModeMapping.modes[Modes.mixolydian]: ['major', '7'],
#          ModeMapping.modes[Modes.aeolian]: ['m', 'm7'],
#          ModeMapping.modes[Modes.minor]: ['m', 'm7'],
#          ModeMapping.modes[Modes.locrian]: ['dim', 'dim7']
#      }


def mode_starting_degree(mode_name):
    mode_name = mode_name.lower()
    if mode_name not in ModeMapping.modes.keys():
        raise ValueError('Mode {} not recognised. Please choose from'
                         '{}'.format(mode_name, ModeMapping.modes.keys()))
    return ModeMapping.modes[mode_name]

major_scale = 'T,T,S,T,T,T,S'.split(',')
major_chords = 'Major, Minor, Minor, Major, Major, Minor, Dim'.split(', ')

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
note_numbers = [1, 3, 4, 6, 8, 9, 11]
d_note_numbers = {
    1: 'A',
    2: ('A Sharp', 'B Flat'),
    3: 'B',
    4: 'C',
    5: ('C Sharp', 'D Flat'),
    6: 'D',
    7: ('D Sharp', 'E Flat'),
    8: 'E',
    9: 'F',
    10: ('F Sharp', 'G Flat'),
    11: 'G',
    12: ('G Sharp', 'A Flat')
}


class ScaleCreator(object):

    def __init__(self, starting_note, mode):
        self._starting_note = starting_note.upper()
        # get the numerical position of the starting note
        self._starting_note_number = self._get_note_number()
        # get the starting number of the mode we're in
        self._mode_starting_degree = mode_starting_degree(mode)
        # get the tone-semitone sequence for the mode we're in
        self._intervals = self._circular_index(self._mode_starting_degree,
                                               major_scale)
        self.scale = self._get_scale()
        self.chords = self._get_chords(self.scale)


    def _get_note_number(self):
        '''gets the starting note number from 1 to 12'''
        note_position = notes.index(self._starting_note[0])
        note_number = note_numbers[note_position]
        note_number += 1 if 'SHARP' in self._starting_note else 0
        note_number -= 1 if 'FLAT' in self._starting_note else 0
        note_number %= 12
        return note_number


    def _get_scale(self):
        # get the cumulative sum of note distances given the list of intervals
        distances_from_start = self._intervals_to_distances(self._intervals)
        note_numbers = [
            (self._starting_note_number) + d % 12 for d in distances_from_start]
        note_numbers.insert(0, self._starting_note_number)
        return self._note_numbers_to_notes(note_numbers)


    def _note_numbers_to_notes(self, note_numbers):
        '''iteratively builds up a scale, adding sharps and flats where
        appropriate'''
        notes = []
        notes.append(self._starting_note)
        for num in note_numbers:
            note = d_note_numbers[num]
            if isinstance(note, tuple):
                # decide whether to use sharp or flat based on previous note values
                previous_letter = notes[-1][0]
                note = note[0] if note[1].startswith(previous_letter) else note[1]
            notes.append(note)
        return notes

    def _intervals_to_distances(self, intervals):
        message = 'Interval not recognised. Intervals must be either \'T\' or \'S\''
        distances = [2 if interval == 'T' else 1 if interval == 'S' \
            else ValueError(message) for interval in intervals]
        return np.cumsum(distances)

    def _get_chords(self, scale):
        # find the starting degree
        index = self._mode_starting_degree % 12
        major_minor = self._circular_index(index, major_chords)
        return [f'{note} {chord}' for (note, chord) in zip(scale, major_minor)]

    @staticmethod
    def _circular_index(index, input_list):
        '''starts on an index in a list'''
        return input_list[index: ] + input_list[ :index]


