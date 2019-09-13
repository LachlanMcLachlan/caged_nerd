import argparse
import sys
import logging

from caged_nerd.musical_scales import Modes
from caged_nerd import driver

CHORDS = 'chords'

logger = logging.getLogger(__name__)


def get_parser():
    """

    Returns:

    """
    parser = argparse.ArgumentParser(description="A Python interface for caged_nerd. ")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    parser_chords = subparsers.add_parser(
        CHORDS,
        help="Tests you to find chords from a key and mode of your choice.",
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
        "--starting_note",
        "-sn",
        dest="starting_note",
        required=False,
        type=str,
        help="The note you want to start on. e.g. B flat",
        default='C'
    )

    parser_chords.add_argument(
        "--mode",
        "-m",
        dest="mode",
        required=False,
        type=str,
        help="The mode in which you want to play. e.g. Lydian/ Major/ Minor",
        default=Modes.major
    )

    parser_chords.add_argument(
        "--rounds",
        "-r",
        dest="rounds",
        required=False,
        type=int,
        help="How many times to test you.",
        default=10
    )

    return parser


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    parser = get_parser()
    args = parser.parse_args(args)
    command = args.command

    if command == CHORDS:
        driver.ChordsDriver(starting_note=args.starting_note,
                            mode=args.mode,
                            rounds=args.rounds).main()


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
