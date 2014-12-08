# from util import *
# import pickle
# from ScoreParser import *

	
# def convert_idea(arr):
# 	a = []
# 	for i in range(len(arr)):
# 		a += [convert_note_or_rest(arr[i])]
# 	return a

# def get_solo_ideas_from_measure(measure):
# 	"""
# 		Make these optimized for getting solo ideas that are non-trivial
# 		-- some of these are like mostly rests, and will be really boring to
# 		listen to.
# 	"""
# 	solo_ideas = []
# 	full_idea = []
# 	note_indices = []
# 	for elem in measure:
# 		if type(elem) is note.Note:
# 			full_idea += [elem]
# 			note_indices += [len(full_idea) - 1]
# 		if type(elem) is note.Rest:
# 			full_idea += [elem]
# 		if type(elem) is stream.Voice:
# 			solo_ideas += get_ideas_from_voice(elem)

# 	solo_ideas += extract_n_note_ideas(full_idea, 4)
# 	return solo_ideas

# def extract_n_note_ideas(full_idea, n):
# 	solo_ideas = []
# 	for i in range(len(note_indices) - (n-1)):
# 		solo_ideas += [full_idea[note_indices[i]:(note_indices[i + (n-1)] + 1)]]

# def get_ideas_from_voice(voice):
# 	full_idea = []
# 	note_indices = []
# 	for elem in voice:
# 		if type(elem) is note.Note:
# 			full_idea += [elem]
# 			note_indices += [len(full_idea) - 1]
# 		if type(elem) is note.Rest:
# 			full_idea += [elem]
# 	return extract_n_note_ideas(full_idea, 4)

# def convert_note_or_rest(n):
# 	if type(n) is note.Note:
# 		good = note.Note()
# 		good.pitch = n.pitch
# 		good.quarterLength = n.quarterLength	
# 		return good
# 	elif type(n) is note.Rest:
# 		good = note.Rest()
# 		good.quarterLength = n.quarterLength
# 		return good


# def add_fifths_intervals(notes_and_rests):
# 	ind_of_last_note = -1
# 	arr = []
# 	for i in range(len(notes_and_rests)):
# 		if ind_of_last_note == -1 and type(notes_and_rests[i]) == note.Note:
# 			ind_of_last_note = i
# 		elif type(notes_and_rests[i]) == note.Note:
# 			arr += [get_fifths_distance(notes_and_rests[ind_of_last_note], notes_and_rests[i])]
# 			ind_of_last_note = i
# 	return arr

# s = midi_to_stream('the_lady_is_a_tramp.midi')
# sp = ScoreParser(s)
# ideas = sp.get_solo_ideas_from_measure(sp.score[sp.solo_parts[55]][55])
# idea = ideas[0]

# converted = convert_idea(idea)





from Trainer import *
t = Trainer()
t.get_training_set()