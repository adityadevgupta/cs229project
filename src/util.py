import os
from music21 import *
import numpy as np

def midi_to_stream(filename_path):
	"""
		Function: midi_to_stream:
		converts a full filename to a Music21 usable Stream object, 
	"""

	midi_file = midi.midiFile()
	midi_file.open()
	midi_file.read()
	midi_fileg.close()
	return midi.translate.midiFileToStream(mf)