# -*- coding: utf-8 -*-
class Whisky(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def pokazWhisky(self):
		return self.name + " " + str(self.age)
