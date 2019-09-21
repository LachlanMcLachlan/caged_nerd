import argparse
import sys
import logging

from caged_nerd.musical_scales import Modes, ModeMapping
from caged_nerd import driver

# available - these allow the `main` function to call the correct driver
CHORDS = "chords"

logger = logging.getLogger(__name__)


def get_parser():
    """
    Sets up parsers in order to accept arguments from the command line.
    Returns (ArgumentParser): parser object containing parsers and subparsers.

    """
    parser = argparse.ArgumentParser(description="A Python interface for caged_nerd. ")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    parser_chords = subparsers.add_parser(
        CHORDS, help="Tests you to find chords from a key and mode of your choice."
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
        default=logging.INFO,
    )

    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    parser_chords.add_argument(
        "--start-on",
        "-sn",
        dest="starting_note",
        required=False,
        type=str,
        help="The note on which you want to start. e.g. B flat",
        default="C",
    )

    parser_chords.add_argument(
        "--mode",
        "-m",
        dest="mode",
        required=False,
        type=str,
        help="The mode in which you want to play. Choose from: {}".format(
            ", ".join(list(ModeMapping.modes.keys()))
        ),
        default=Modes.major,
    )

    parser_chords.add_argument(
        "--rounds",
        "-r",
        dest="rounds",
        required=False,
        type=int,
        help="How many times to test you.",
        default=10,
    )

    return parser


def main(args):
    """
    Main entrypoint. Its functionality is minimal. Its job is to parse arguments
    from the command line and call the correct driver. That's it!

    Args:
      args ([str]): command line parameter list
    """
    parser = get_parser()
    args = parser.parse_args(args)
    command = args.command

    if command == CHORDS:
        driver.ChordsDriver(
            starting_note=args.starting_note, mode=args.mode, rounds=args.rounds
        ).main()


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
