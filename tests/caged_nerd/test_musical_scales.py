import pytest
from caged_nerd import musical_scales as mus


@pytest.mark.parametrize(
    argnames='starting_note, mode, expected_scale',
    argvalues=[
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']),
        ('f', 'major', ['F', 'G', 'A', 'B flat', 'C', 'D', 'E', 'F']),
        ('f', 'minor', ['F', 'G', 'A flat', 'B flat', 'C', 'D flat', 'E flat', 'F']),
        ('e', 'major', ['E', 'F sharp','G sharp', 'A', 'B', 'C sharp', 'D sharp', 'E']),
        ('c sharp', 'minor', ['C sharp', 'D sharp', 'E', 'F sharp', 'G sharp', 'A', 'B', 'C sharp']),
        ('a FLAT', 'mixolydian', ['A flat', 'B flat', 'C', 'D flat', 'E flat', 'F', 'G flat', 'A flat'])
    ]
)
def test_musical_scales_returns_scale(starting_note, mode, expected_scale):
    scale_object = mus.ScaleCreator(starting_note=starting_note, mode=mode)
    assert scale_object.scale == expected_scale

@pytest.mark.parametrize(
    argnames='starting_note, mode, expected_chords',
    argvalues=[
        ('C', 'major', ['C Major', 'D Minor', 'E Minor', 'F Major', 'G Major',
                        'A Minor', 'B Dim']),
        ('f', 'major', ['F Major', 'G Minor', 'A Minor', 'B flat Major',
                        'C Major', 'D Minor', 'E Dim']),
        ('f', 'minor', ['F Minor', 'G Dim', 'A flat Major', 'B flat Minor',
                        'C Minor', 'D flat Major', 'E flat Major']),
        ('a FLAT', 'mixolydian', ['A flat Major', 'B flat Minor', 'C Dim',
                                  'D flat Major', 'E flat Minor', 'F Minor',
                                  'G flat Major'])
    ]
)
def test_musical_scales_returns_chords(starting_note, mode, expected_chords):
    scale_object = mus.ScaleCreator(starting_note=starting_note, mode=mode)
    assert scale_object.chords == expected_chords