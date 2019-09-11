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

class ChordMapping():
    # maps the mode number to the chords available for that mode
     modes = {
         ModeMapping.modes[Modes.ionian]: ['major', 'maj7'],
         ModeMapping.modes[Modes.major]: ['major', 'maj7'],
         ModeMapping.modes[Modes.dorian]: ['m', 'm7'],
         ModeMapping.modes[Modes.phrygian]: ['m', 'm7'],
         ModeMapping.modes[Modes.lydian]: ['major', 'maj7'],
         ModeMapping.modes[Modes.mixolydian]: ['major', '7'],
         ModeMapping.modes[Modes.aeolian]: ['m', 'm7'],
         ModeMapping.modes[Modes.minor]: ['m', 'm7'],
         ModeMapping.modes[Modes.locrian]: ['dim', 'dim7']
     }


def mode_starting_degree(mode_name):
    mode_name = mode_name.lower()
    if mode_name not in ModeMapping.modes.keys():
        raise ValueError('Mode {} not recognised. Please choose from'
                         '{}'.format(mode_name, ModeMapping.modes.keys()))
    return ModeMapping.modes[mode_name]

major_scale = 'T,T,S,T,T,T,S'.split(',')
major_chords = 'Major, Minor, Minor, Major, Major, Minor, Dim'.split(', ')
notes = ['A', ('A sharp', 'B flat'), 'B', 'C',
         ('C sharp', 'D flat'), 'D', ('D sharp', 'E flat'), 'E', 'F',
         ('F sharp, G flat'), 'G', ('G sharp', 'A flat')]



class ScaleCreator(object):

    def __init__(self, starting_note, mode):
        self._starting_note = starting_note.upper()
        self._mode_starting_degree = mode_starting_degree(mode)
        self.index = self._mode_starting_degree % 12
        self._intervals = self._circular_index(self.index, major_scale)
        self.scale = self._get_scale()
        self.chords = self._get_chords(self.scale)

    def _get_intervals(self):
        index = self._mode_starting_degree % 12
        intervals = major_scale[index:] + major_scale[:index]
        return intervals

    def _get_scale(self):
        distances = self._intervals_to_distances(self._intervals)
        return self._scale_as_list(distances)

    def _scale_as_list(self, distances):
        note_index = notes.index(self._starting_note)
        scale = [notes[note_index]]
        for distance in distances:
            note_index = (note_index + distance) % 12
            note = notes[note_index]
            # update the note if it's a sharp of the same note
            flat_or_sharp = isinstance(note, tuple)
            if flat_or_sharp and distance == 1:
                note = note[1]
            elif flat_or_sharp:
                note = note[0]
            scale.append(note)
        return scale

    def _intervals_to_distances(self, intervals):
        message = 'Interval not recognised. Intervals must be either \'T\' or \'S\''
        return [2 if interval == 'T' else 1 if interval == 'S' \
            else ValueError(message) for interval in intervals]

    def _get_chords(self, scale):
        # find the starting degree
        index = self._mode_starting_degree % 12
        major_minor = self._circular_index(index, major_chords)
        return [f'{note} {chord}' for (note, chord) in zip(scale, major_minor)]

    @staticmethod
    def _circular_index(index, input_list):
        '''starts on an index in a list'''
        return input_list[index: ] + input_list[ :index]

'''
I can make scales - I put the starting note and the desired scale degree into 
that class and it makes a list of notes
'''

