# this module contains all the musical intervals

class ModeMapping():
    modes = {'major': 0, 'dorian': 1, 'phrygian': 2, 'lydian': 3, 'mixolydian': 4,
             'aeolian': 5, 'minor': 5, 'locrian': 6}

class DistanceMapper():
    distances = {1: 'minor_second'}
def mode_starting_degree(mode_name):
    mode_name = mode_name.lower()
    if mode_name not in ModeMapping.modes.keys():
        raise ValueError('Mode {} not recognised. Please choose from'
                         '{}'.format(mode_name, ModeMapping.modes.keys()))
    return ModeMapping.modes[mode_name]


class ScaleCreator(object):
    def __init__(self, starting_note, mode):
        self._starting_note = starting_note
        self.notes = 'A, B flat, B, C, D flat, D, E flat, E, F, G flat, G, A Flat'.split(', ')
        self.major_scale = 'T,T,S,T,T,T,S'.split(',')
        self.mode_starting_degree = mode_starting_degree(mode)
        self.scale = self._get_scale(self.mode_starting_degree)

    def _get_scale(self, n):
        index = n % 12
        intervals = self.major_scale[index:] + self.major_scale[:index]
        distances = self._intervals_to_distances(intervals)
        return self._scale_as_list(distances)

    def _scale_as_list(self, distances):
        note_index = self.notes.index(self._starting_note)
        scale = [self.notes[note_index]]
        for distance in distances:
            note_index += distance
            scale.append(self.notes[note_index])
        return scale

    def _intervals_to_distances(self, intervals):
        message = 'Interval not recognised. Intervals must be either \'T\' or \'S\''
        return [2 if interval == 'T' else 1 if interval == 'S' \
            else ValueError(message) for interval in intervals]



'''
I can make scales - I put the starting note and the desired scale degree into 
that class and it makes a 
'''

