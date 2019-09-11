import pytest
from caged_nerd import musical_scales as mus


@pytest.mark.parametrize(
    argnames='starting_note, mode, expected_scale',
    argvalues=[
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']),
        ('f', 'major', ['F', 'G', 'A', 'B flat', 'C', 'D', 'E', 'F']),
        ('f', 'minor', ['F', 'G', 'A flat', 'B flat', 'C', 'D flat', 'E flat', 'F']),
        ('e', 'major', ['E', 'F sharp','G sharp', 'A', 'B', 'C sharp', 'D sharp', 'E'])
    ]
)
def test_musical_scales_return_scale(starting_note, mode, expected_scale):
    scale_object = mus.ScaleCreator(starting_note=starting_note, mode=mode)
    breakpoint()
    assert scale_object.scale == expected_scale
