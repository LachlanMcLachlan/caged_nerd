"""There are a few musical """
import numpy as np


class CagedMapping:
    """Lists the forms allowed for playing minor chords and major chords.
    This is just to avoid asking users to play minor chords in awkward shapes."""

    minor = ["A", "E", "D"]
    major = ["C", "A", "G", "E", "D"]


class Modes:
    """
    Naming class to hold the names of the modes
    """

    ionian = "ionian"
    major = "major"
    dorian = "dorian"
    phrygian = "phrygian"
    lydian = "lydian"
    mixolydian = "mixolydian"
    aeolian = "aeolian"
    minor = "minor"
    locrian = "locrian"


class ModeMapping:
    """
    Class containing the index of each of the modes. As an example, traditionally
    you'd think of 'Dorian' as 'starting on the 2nd of the relative major scale'.
    In this class that concept is expressed as setting the major mode to 0,
    and the Dorian mode to 1. This relationship means: the Dorian mode (1) is one note
    in the major scale above the major mode (0), which is indeed the '2nd' in
    musical terms.
    """

    modes = {
        Modes.major: 0,
        Modes.ionian: 0,
        Modes.dorian: 1,
        Modes.phrygian: 2,
        Modes.lydian: 3,
        Modes.mixolydian: 4,
        Modes.aeolian: 5,
        Modes.minor: 5,
        Modes.locrian: 6,
    }

    def mode_starting_degree(self, mode_name):
        """Given a key, extracts the corresponding value from the Modes dictionary"""
        mode_name = mode_name.lower()
        if mode_name not in ModeMapping.modes.keys():
            raise ValueError(
                "Mode {} not recognised. Please choose from"
                "{}".format(mode_name, self.modes.keys())
            )
        return self.modes[mode_name]


class MajorScaleInfo:
    # The intervals of a major scale
    major_scale = "T,T,S,T,T,T,S".split(",")
    # The chords allowed in a major scale
    major_chords = "Major, Minor, Minor, Major, Major, Minor, Dim".split(", ")


class NoteInfo:
    # the list of available notes without flats and sharps
    notes = ["A", "B", "C", "D", "E", "F", "G"]
    # beginning on 'A', list of the number of semitones above 'A'
    note_numbers = [0, 2, 3, 5, 7, 8, 10]
    # mapping the semitones above 'A' to their various notes
    d_note_numbers = {
        0: "A",
        1: ("A sharp", "B flat"),
        2: "B",
        3: "C",
        4: ("C sharp", "D flat"),
        5: "D",
        6: ("D sharp", "E flat"),
        7: "E",
        8: "F",
        9: ("F sharp", "G flat"),
        10: "G",
        11: ("G sharp", "A flat"),
    }


class ScaleCreator(object):
    def __init__(self, starting_note, mode):
        """
        Creates a list of available notes and chords in a given key.
        Args:
            starting_note (str): the root note of the desired key.
            mode (str): the mode in which to construct the scale and chords.
        """
        self._starting_note = self._format_starting_note(starting_note)
        self._starting_degree = ModeMapping().mode_starting_degree(mode)
        self.scale = self._get_scale()
        self.chords = self._get_chords()

    def _get_scale(self):
        """returns the scale you want"""
        starting_note_number = self._get_note_number()
        intervals = self._circular_index(
            self._starting_degree, MajorScaleInfo.major_scale
        )
        distances_from_start = self._intervals_to_distances(intervals)
        note_numbers = [(starting_note_number + d) % 12 for d in distances_from_start]
        return self._note_numbers_to_notes(note_numbers)

    def _format_starting_note(self, starting_note):
        """format the note provided by the user"""
        starting_note = starting_note.lower()
        note = starting_note[0].upper()
        if "flat" in starting_note:
            note = f"{note} flat"
        if "sharp" in starting_note:
            note = f"{note} sharp"
        return note

    def _get_note_number(self):
        """gets the starting note number from 1 to 12"""
        note_position = NoteInfo.notes.index(self._starting_note[0])
        note_number = NoteInfo.note_numbers[note_position]
        note_number += 1 if "sharp" in self._starting_note else 0
        note_number -= 1 if "flat" in self._starting_note else 0
        # deal with edge case if note number is less than 0
        note_number = (note_number % 11) if note_number >= 0 else 11
        return note_number

    def _note_numbers_to_notes(self, note_numbers):
        """iteratively builds up a scale, deciding between sharps and flats
        where appropriate"""
        notes = []
        notes.append(self._starting_note)
        for num in note_numbers:
            note = NoteInfo.d_note_numbers[num]
            if isinstance(note, tuple):
                # decide whether to use sharp or flat based on previous note value
                previous_letter = notes[-1][0]
                note = note[1] if note[0].startswith(previous_letter) else note[0]
            notes.append(note)
        return notes

    def _intervals_to_distances(self, intervals):
        """transforms intervals like T and S to numerical distances on the keyboard"""
        message = "Interval not recognised. Intervals must be either 'T' or 'S'"
        distances = [
            2 if interval == "T" else 1 if interval == "S" else ValueError(message)
            for interval in intervals
        ]
        return np.cumsum(distances)

    def _get_chords(self):
        """get the sequence of major and minor available in this key"""
        index = self._starting_degree % 12
        chord_sequence = self._circular_index(index, MajorScaleInfo.major_chords)
        return [f"{note} {chord}" for (note, chord) in zip(self.scale, chord_sequence)]

    @staticmethod
    def _circular_index(index, input_list):
        """starts on an index, then loops around to meet the same index
        from below"""
        return input_list[index:] + input_list[:index]
