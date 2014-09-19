# -*- coding: utf-8 -*-
from piwa import Piwo
from whisky import Whisky

def helloWorld(name):
	return "Hello, %s" % (name)
	
if __name__ == "__main__":
	print helloWorld("Denat")
	tyskie = Piwo("Tyskie")
	print tyskie.pokazPiwo()
	grants = Whisky("Grants")
	print grants.pokazWhisky()
