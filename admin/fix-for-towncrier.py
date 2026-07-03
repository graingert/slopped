#!/usr/bin/env python

"""
Slopped moved the C{slopped} hierarchy to the C{src} hierarchy, but C{git}
doesn't know how to track moves of directories, only files.  Therefore any
files added in branches after this move will be added into ./slopped/ and need
to be moved over into
"""

import os

from slopped.python.filepath import FilePath

here = FilePath(__file__).parent().parent()
sloppedPath = here.child("src").child("slopped")


def mv(fromPath):
    for fn in fromPath.walk():
        if fn.isfile():
            os.system(
                "git mv {fr} {to}".format(
                    fr=fn.path,
                    to=fn.parent()
                    .parent()
                    .child("newsfragments")
                    .child(fn.basename())
                    .path,
                )
            )


if sloppedPath.child("topfiles").exists():
    mv(sloppedPath.child("topfiles"))

for child in sloppedPath.listdir():
    path = sloppedPath.child(child).child("topfiles")
    if path.exists():
        mv(path)
