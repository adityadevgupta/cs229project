from music21 import *
from util import *
import os
from ScoreParser import *
from sklearn.cluster import KMeans

class Trainer:

	def __init__(self):
		self.dir = '../midi/'
		self.n_idea_cluster = 100
		self.n_chord_cluster = 100
		self.train_X_loc = 'data_X'
		self.train_y_loc = 'data_y'
		
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
		store_arr(train_X, self.train_X_loc)
		store_arr(train_y, self.train_y_loc)

	def train(self):
		X, y = get_arr(self.train_X_loc), get_arr(self.train_y_loc)

		chord_fifths = get_chord_fifths(X)
		idea_fifths = get_idea_fifths(y)

		print chord_fifths
		print idea_fifths

		chord_kmeans = KMeans(n_clusters=self.n_chord_cluster)
		idea_kmeans = KMeans(n_clusters=self.n_idea_cluster)

		chord_kmeans.fit(chord_fifths)	
		idea_kmeans.fit(idea_fifths)

	def get_chord_fifths(self, X):
		arr = []
		for chord_trip in X:
			for chord_rep in chord_trip:
				if chord_rep.fifths_intervals != None:
					arr += [chord_rep.fifths_intervals]
		return np.array(arr) 

	def get_idea_fifths(self, y):
		idea_fifth_list = [idea.fifths_intervals for idea in y]
		return np.array(idea_fifth_list)




