"""Functions for Nintendo DS Roms"""

import os
import re

EXTENSIONS = r".(zip|7z|rar)$"
REGEX_NUMBERING = re.compile(r"^([0-9]{4} ).*?" + EXTENSIONS)
REGEX_NUMBERING_WITH_DASH = re.compile(r"^([0-9]{4} - ).*?" + EXTENSIONS)
REGEX_RELEASE_GROUP = re.compile(r"^[0-9]{4} - .*? \([EJU]\)(\(.*?\))" + EXTENSIONS)


def add_ds_dash(romdir):
    """Add a dash to Nintendo DS releases that start with ####"""
    roms = [rom for rom in os.listdir(romdir) if rom[5] != '-']
    for rom in roms:
        if REGEX_NUMBERING.match(rom).group(1):
            os.rename(
                os.path.join(romdir, rom),
                os.path.join(romdir, rom.replace(' ', ' - ', 1))
            )
