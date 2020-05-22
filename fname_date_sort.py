#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' given a directory as an argument, modifies the dates of the files in
that directory such that ls -tr and ls give the same listing.
this is useful for some media players that sort the files wrt to date
rather than filename.
future features:
    --- recursively doing this for directories
    --- accepting a list of filenames instead of a directory
'''

import argparse, os
from pathlib import Path
import time

parser = argparse.ArgumentParser(description='modify dates of files to alphabetical order of filenames.')
parser.add_argument('path', metavar='path', nargs=1,
                    help='the path to the directory')
args = parser.parse_args()

fhead = args.path[0]
file_list = os.listdir(fhead)
file_list.sort()
for ftail in file_list:
    fpath = os.path.join(fhead, ftail)
    Path(fpath).touch()
    time.sleep(1)
