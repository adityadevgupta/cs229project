import os
from music21 import *
import numpy as np

def get_solo_part(score, treble):
  return None

def get_training_point(measure):
	return None

def get_time_signature(measure):
  return s[0][0][1]

def get_chords_from_measure(measure):
  chords = []
  for elem in measure:
    if type(elem) is chord.Chord:
      chords += [elem]
    if type(elem) is stream.Voice:
      for thing in elem:
        if type(thing) is chord.Chord:
          chords += [thing]
  return chords
   
def add_measures_to_parts(score):
  for part in score:
    if not part.hasMeasures():
      part.makeMeasures(inPlace=True)

def midi_to_stream(filename_path):
	"""
		Function: midi_to_stream:
		converts a full filename to a Music21 usable Stream object, 
	"""
	# midi_file = midi.MidiFile()
	# midi_file.open(filename_path)
	# midi_file.read()
	# midi_file.close()
	s = midi.translate.midiFilePathToStream(filename_path)
	
	return s
