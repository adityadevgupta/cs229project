import os
from music21 import *
import numpy as np

def midi_to_stream(filename_path):
	"""
		Function: midi_to_stream:
		converts a full filename to a Music21 usable Stream object, 
	"""

	midi_file = midi.MidiFile()
	midi_file.open(filename_path)
	midi_file.read()
	midi_file.close()
	return midi.translate.midiFileToStream(midi_file)