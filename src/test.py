from util import *
import pickle
from ScoreParser import *

	
def convert_idea(arr):
	a = []
	for i in range(len(arr)):
		a += [convert_note_or_rest(arr[i])]
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


def add_fifths_intervals(notes_and_rests):
	ind_of_last_note = -1
	arr = []
	for i in range(len(notes_and_rests)):
		if ind_of_last_note == -1 and type(notes_and_rests[i]) == note.Note:
			ind_of_last_note = i
		elif type(notes_and_rests[i]) == note.Note:
			arr += [get_fifths_distance(notes_and_rests[ind_of_last_note], notes_and_rests[i])]
			ind_of_last_note = i
	return arr

s = midi_to_stream('the_lady_is_a_tramp.midi')
sp = ScoreParser(s)
ideas = sp.get_solo_ideas_from_measure(sp.score[sp.solo_parts[55]][55])
idea = ideas[0]

converted = convert_idea(idea)





