# au to wav converter

## A dead simple conversion script wrapped in a Tkinter interface

After installing the soundfile requirement, the other libraries should just work. You can initiate this from a terminal by simply typing `python3 ooconvert.py`. 

## Creating a standalone MacOS app from this code

It's pretty easy to wrap this up as a `*.app` package for MacOS. 

1. In a termal window, install `pyinstaller` with the command `pip install pyinstaller`.
1. Create a single-file, windowed version of the app with the command `pyinstaller --windowed --onefile ooconvert.py`
1. Copy the `dist/ooconvert.app` file to wherever you want to keep it and run it like a regular executable