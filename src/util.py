import os
from music21 import *
import numpy as np
import pickle

#				C 	C#	D 	Eb	E 	F 	F# 	G 	Ab 	A 	Bb 	B
CIRCLE_POS =   [0, 	7, 	2, 	9, 	4,  11, 6,	1, 	8, 	3, 	10, 5]

def get_solo_part(score, treble):
  return None

def get_training_point(measure):
	return None

def get_time_signature(measure):
  return s[0][0][1]

def store_arr(arr, name):
	f = open(name, 'w')
	pickle.dump(arr, f)

def get_arr(name):
	f = open(name, 'r')
	return pickle.load(f)

def get_fifths_distance(one, two):
	"""
		Takes in two Note.note objects and returns the circle 
		of fifths distance between them.
		This takes the pitch classes, and then takes the counter-
		clockwise rotational distance from one note to the other.
	"""
	diff = (CIRCLE_POS[two.pitchClass] - CIRCLE_POS[one.pitchClass]) % 12
	return diff + 0.0 if diff <= 6 else 12.5 - diff

def convert_chord(c):
	if c is None:
		return None
	a = []
	for i in range(len(c)):
		a += [convert_note_or_rest(c[i])]
	return chord.Chord(a)

def convert_idea(idea):
	a = []
	for i in range(len(idea)):
		a += [convert_note_or_rest(idea[i])]
	return a

def convert_note_or_rest(n):
	if type(n) is note.Note:
		good = note.Note()
		good.pitch = n.pitch
		good.quarterLength = n.quarterLength	
		return good
	elif type(n) is note.Rest:
		good = note.Rest()
		good.quarterLength = n.quarterLength
		return good

def get_chords_from_measure(measure, min_len):
  chords = []
  for elem in measure:
    if type(elem) is chord.Chord and len(elem) >= min_len:
      chords += [elem]
    if type(elem) is stream.Voice:
      for thing in elem:
        if type(thing) is chord.Chord and len(thing) >= min_len:
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
	try:
		s = midi.translate.midiFilePathToStream(filename_path)
		add_measures_to_parts(s)
		return s
	except (Exception):
		return None
