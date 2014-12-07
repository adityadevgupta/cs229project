from music21 import *
from util import *

def convert_file_to_measures(file):
	s = midi_to_stream(file)
	add_measures_to_parts(s)

	mf = midi.translate.music21ObjectToMidiFile(s)
	mf.open(fp, 'wb') 
	mf.write()	