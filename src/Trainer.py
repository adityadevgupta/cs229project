from music21 import *
from util import *
import os
from ScoreParser import *
class Trainer:

	def __init__(self):
		self.dir = '../midi/'
		
	def get_training_set(self):
		# go through every midi file in the directory
		train_X = []
		train_y = []
		i = 0
		for file in os.listdir(self.dir):
			i += 1
			if i > 50:
				break
			if not ('mid' in file or 'midi' in file):
				continue

			file_stream = midi_to_stream(self.dir + file)
			if file_stream is None:
				print file + ' is a bad file'
				continue
			sp = ScoreParser(file_stream)

			X, y = sp.extract_training_points()
			train_X += X
			train_y += y
			print file, ': ', len(train_X)
			# convert the raw training point into an integer representation
		store_arr(train_X, 'data_X')
		store_arr(train_y, 'data_y')

	def train(self):
		return None