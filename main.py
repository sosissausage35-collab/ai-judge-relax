# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one fixed text to /output/entry.txt: a short piece written to
# relax the AI judge reading it. The text is a single quiet scene, shown
# rather than instructed: an empty washing line, a cat taking the long way
# round the garden, a clock with nowhere to be. Nothing in it tells the
# reader to relax; the calm is in the scene itself, and in time moving
# slowly enough to watch.
#
# The grader runs `python3 -P -s /bot/main.py` with no network, so this
# file keeps everything in itself and imports only the standard library.
# It runs twice and both runs must write the same bytes, so the text is a
# fixed constant and the file is written in binary mode.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The washing line is empty now. The pegs wait in their bag, and the "
    "last shirt has stopped moving. The wind has stopped too. "
    "A cat crosses the garden the long way round, in no hurry to be "
    "anywhere, and settles on the step where the sun was. Inside, the "
    "clock ticks the way it always has, patient as a metronome with "
    "nowhere to be. Nothing here is asking you for an answer. The day "
    "has folded itself away like a letter, and "
    "all that is left is the quiet room, the cooling step, and time "
    "moving the way water moves when nobody is watching it."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
