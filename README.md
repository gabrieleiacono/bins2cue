# bins2cue

A simple tool for PSX roms that creates a `.cue` file starting from one or more `.bin` files (data and audio files).
It searches for roms matching the pattern `<prefix><BIN_NUMBER><suffix>` in the current directory, given `<prefix>` and `<suffix>`.

Example:
```
$ python bins2cue.py
Please enter the prefix of bin filenames:Mickey's Wild Adventure (Europe) (Track # trailing whitespace
Please enter the suffix of bin filenames:).bin
.cue generated.
Please enter cue filename:Mickey's Wild Adventure.cue
```

