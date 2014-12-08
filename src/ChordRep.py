from music21 import *
from util import *

class ChordRep:
	def __init__(self, c=None):
		self.fifths_intervals = None
		self.c = convert_chord(c)
		if not c is None:
			self.add_fifths_intervals()

	def add_fifths_intervals(self):
		ind_of_last_note = -1
		arr = []
		for i in range(len(self.c)):
			if ind_of_last_note == -1 and type(self.c[i]) == note.Note:
				ind_of_last_note = i
			elif type(self.c[i]) == note.Note:
				arr += [get_fifths_distance(self.c[ind_of_last_note], self.c[i])]
				ind_of_last_note = i
		self.fifths_intervals = arr

	# def output(self):
	# 	return [self.fifths_intervals.tolist(), self.c.tolist()]