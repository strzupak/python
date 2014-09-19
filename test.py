# -*- coding: utf-8 -*-
from piwo import Piwo

def helloWorld(name):
	return "Hello, %s" % (name)
	
if __name__ == "__main__":
	print helloWorld("Denat")
	tyskie = Piwo("Tyskie")
	print tyskie.pokazPiwo()
