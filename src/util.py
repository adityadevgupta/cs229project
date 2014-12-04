import os
from music21 import *
import numpy as np

"""
object

Score (music21 score type)
bass
treble
nParts
nMeasures
time signature

"""

def get_score_object(score):
  return None

def get_training_data(score):

  # basic variables
  nParts = len(score)
  treble = []
  bass = []
  nMeasures = min([len(s[i]) for i in range(nParts)])

  # determine clefs of parts
  for i in range(nParts):
    if type(s[i][0][0]) is clef.TrebleClef:
      treble += i
    if type(s[0][0][0]) is clef.BassClef:
      bass += i

  X_train = []

  # get training point for every measure
  for i in range(nMeasures):
    x = [None]*3
    # not the first measure
    if i != 0:
      # for each bass clef part
      for b in bass:
        chords = get_chords_from_measure(score[b][0])

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

	midi_file = midi.MidiFile()
	midi_file.open(filename_path)
	midi_file.read()
	midi_file.close()
	s = midi.translate.midiFileToStream(midi_file)
	return s
