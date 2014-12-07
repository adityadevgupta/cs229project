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
			if i > 20:
				break
			if not ('mid' in file or 'midi' in file):
				continue
			if file == 'a_cottage_for_sale_rs.mid':
				continue
			print file, ': ', len(train_X)
			sp = ScoreParser(self.dir + file)
			X, y = sp.extract_training_points()
			train_X += X
			train_y += y
			# convert the raw training point into an integer representation
		print len(train_X)

	def train(self):
		return None