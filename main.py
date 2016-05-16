class Level:

	def __init__(self, file, score):
		self.file = file
		self.score = score

	def play(self):
		# Plays the level??

class Score:
	"""
	'Score' refers to the music notes on a staff. This class defines the note positions for a piece.
	"""

	def __init__(self):
		self.beats_per_measure = 4	# Top number of meter.
		self.beat_value = 4			# Bottom number of meter.
		self.tempo = 120			# Beats per minute.
		self.notes = []				# All notations on the staff.
		



"""
The make it go stuff
"""

ode_to_joy = new Score()
melody = []
melody.append(('B5', 1))
melody.append(('B5', 1))
melody.append(('C5', 1))
melody.append(('D5', 1))
melody.append(('D5', 1))
melody.append(('C5', 1))
melody.append(('B5', 1))
melody.append(('A5', 1))
melody.append(('G5', 1))
melody.append(('G5', 1))
melody.append(('A5', 1))
melody.append(('B5', 1))
melody.append(('B5', 1.5))
melody.append(('A5', .5))
melody.append(('A5', 2))
ode_to_joy.notes = melody
level1 = new Level('/mp3s/odetojoy.mp3', ode_to_joy)
level1.play()