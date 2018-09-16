from glob import glob
from six.moves import input

FIRSTCUE = r"""FILE "{0}" BINARY
TRACK 01 MODE1/2352
INDEX 01 00:00:00"""

NEXTCUES = r"""
FILE "{0}" BINARY
TRACK 02 AUDIO
INDEX 00 00:00:00
INDEX 01 00:02:00"""

prefix = input("Please enter the prefix of bin filenames:")
suffix = input("Please enter the suffix of bin filenames:")

gamefiles = sorted(glob(prefix+'*'+suffix))

try:
    cue = FIRSTCUE.format(gamefiles[0])
except IndexError:
    print("No files matching pattern in current directory.")

if len(gamefiles) > 1:
    for file in gamefiles[1:]:
        cue += NEXTCUES.format(file)

print(".cue generated.")
savepath = input("Please enter cue filename:")
filehandle = open(savepath, "w")
filehandle.write(cue)
filehandle.close()
