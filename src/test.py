from util import *

s = midi_to_stream("../midi/autumn_leaves_jpa.mid")

def find_measure(stream):
	if not hasattr(stream, '__iter__'):#not iterable
		return
	for e in stream:
		# if type(e) is Measure:
		# 	print 'found measure'
		print(type(e))
		find_measure(e)