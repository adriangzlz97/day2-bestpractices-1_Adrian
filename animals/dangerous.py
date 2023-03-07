#!/bin/env/python
class Mammals:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Tiger', 'Elephant', 'Wild Cat']
	def printMembers(self):
		print('Printing members of the Mammals class')
		for member in self.members:
			print('\t%s ' % member)

class Fish:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Shark', 'Piranha']

	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print('\t%s ' % member)
