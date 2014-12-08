from music21 import *
from util import *

class MusicalIdea:
	def __init__(self, note_arr=None):
		self.fifths_intervals = None
		self.notes_and_rests = convert_idea(note_arr)
		if not note_arr is None:
			self.add_fifths_intervals()

	def add_fifths_intervals(self):
		ind_of_last_note = -1
		arr = []
		for i in range(len(self.notes_and_rests)):
			if ind_of_last_note == -1 and type(self.notes_and_rests[i]) == note.Note:
				ind_of_last_note = i
			elif type(self.notes_and_rests[i]) == note.Note:
				arr += [get_fifths_distance(self.notes_and_rests[ind_of_last_note], self.notes_and_rests[i])]
				ind_of_last_note = i
		arr

	# def output_for_storage(self):
	# 	return [self.fifths_intervals(), self.notes_and_rests()]