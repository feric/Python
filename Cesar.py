#!/usr/bin/env python
class rotar:
	def __init__(self,rotate):
		self.abc=[]
		self.bca=[]
		self.pos=0
		self.textEncode=[]
		self.textDecode=[]
		import time
		print "Generating alphabet"
		time.sleep(1)
		for i in xrange(65,65+26):
			self.abc.append(chr(i))
		print "Generating alphabet rotate {0} positions".format(rotate)
		pos=0
		for i in self.abc:
			pos=self.abc.index(i)
			if pos+rotate < len(self.abc):
				self.bca.insert(pos+rotate,i)
			else:
				self.bca.insert((pos+rotate)-len(self.abc),i)
		print "This is your new alphabet"
		time.sleep(1)
		print self.abc
		print "====="*len(self.abc)
		print self.bca
	def Encode(self,phrase):
		print "====="*len(self.abc)
		for c in phrase:
			if c in self.abc:
				self.textEncode.append(self.bca[self.abc.index(c)])
			else:
				self.textEncode.append(c)
		print "".join(self.textEncode)
	def ddecode(self,phrase):
		print "====="*len(self.abc)
		for c in phrase:
			if c in self.bca:
				self.textDecode.append(self.abc[self.bca.index(c)])
			else:
				self.textDecode.append(c)
		print "".join(self.textDecode)
rotate = input("How many position do u wnat rotate? > ")
enctexto = raw_input("Text to encode > ")
variable = rotar(rotate)
variable.Encode(enctexto.upper())
dectexto = raw_input("Text to decode > ")
variable.ddecode(dectexto.upper())
