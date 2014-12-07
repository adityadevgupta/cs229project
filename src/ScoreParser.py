from music21 import *
from util import *
class ScoreParser:

	def __init__(self, file):
		"""
			Initialization that just takes in a music21 score object
		"""
		self.score = midi_to_stream(file)
		add_measures_to_parts(self.score)
		# do the preprocessing
		# measures,
		#self.timeSignature = #get time
		self.min_idea_size = 3
		self.n_parts = len(self.score)
		self.n_measures = min([len(self.score[i]) for i in range(self.n_parts)])
		self.solo_parts = self.get_solo_parts() # array for each measure, gives the soloing part
		# jhust fucking figure out which thing is playing the most notes in different areas

	def extract_training_points(self):
		"""
			Gets all training points for the score, 
			Goes through all measures to get it
		"""
		return x, y		

	def extract_training_points_from_measure(self, measure_index):
		"""
			Uses information about the soloing instrument 
			given in self.soloPart to extract training points
			in an (X, y).
		"""
		chords = [] # stores all the chords found in the measure
		solo_ideas = [] # stores all the 3-5 note ideas found in the measure
		last_chords_of_prev_measure = []
		first_chords_of_next_measure = []

		for part in range(self.n_parts):
			# skip solo part
			if (not part == self.solo_parts[part]) or (self.n_parts == 1) :
				# populate the chords array
				chords += get_chords_from_measure(self.score[part][measure_index])
				last_measure_chords =  get_chords_from_measure(self.score[part][measure_index - 1]) if measure_index - 1 != 0 else None 
				if last_measure_chords != None:
					if len(last_measure_chords) != 0:
						last_chords_of_prev_measure += last_measure_chords[-1] 	
				first_measure_chords = get_chords_from_measure(self.score[part][measure_index + 1])
				if first_measure_chords != None:
					if len(first_measure_chords) != 0:
						first_chords_of_next_measure += first_measure_chords[0]

			if (part == self.solo_parts[part]) :
				# populate the solo_ideas array
				solo_ideas = self.get_solo_ideas_from_measure(self.score[part][measure_index])

				
		# if either the first one or the last one are none, we make it None so that
		# the learning algorithm recognizes that it's the first or last measure in the
		# piece
		if len(last_chords_of_prev_measure) == 0:
			last_chords_of_prev_measure = [None]
		if len(first_chords_of_next_measure) == 0:
			first_chords_of_next_measure = [None]

		# get all combinations of chords and solo_ideas
		print "prev chords: ", last_chords_of_prev_measure
		print "chords: ", chords
		print "next chords: ", first_chords_of_next_measure
		print "solo ideas: ", solo_ideas

	def get_solo_ideas_from_measure(self, measure):
		"""
			Make these optimized for getting solo ideas that are non-trivial
			-- some of these are like mostly rests, and will be really boring to
			listen to.
		"""
		solo_ideas = []

  		idea = []
	  	for elem in measure:
			if (type(elem) is note.Note) or (type(elem) is note.Rest):
				idea += [elem]
			if type(elem) is stream.Voice:
				voice_idea = []
				for thing in elem:
					if (type(thing) is note.Note) or (type(thing) is note.Rest):
						voice_idea += [thing]
				if len(voice_idea) >= self.min_idea_size:
					solo_ideas += [voice_idea]
		if len(idea) >= self.min_idea_size:
			solo_ideas += [idea]
		return solo_ideas


	def get_solo_parts(self):
		solo_parts = []

		for i in range(self.n_measures):
			max_num_notes = -1
			max_part = -1
			for j in range(self.n_parts):
				num_notes = self.notes_in_measure(self.score[j][i]) 
				# print 'Part ', j, ' with ', num_notes, ' notes'
				if  num_notes > max_num_notes:
					max_num_notes = num_notes
					max_part = j
					# print 'max_part is now ', max_part
			solo_parts += [max_part]
		return solo_parts

	def notes_in_measure(self, measure):
	  count = 0
	  for elem in measure:
	    if (type(elem) is note.Note) or (type(elem) is note.Rest):
	    	count += 1
	    if type(elem) is stream.Voice:
	      for thing in elem:
	        if (type(thing) is note.Note) or (type(thing) is note.Rest):
	          count += 1
	  return count

