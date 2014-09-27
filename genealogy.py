#!/usr/bin/env python3
import random
import re

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

class Phrase:
	
	def __init__(self, typ):
		self.typ = typ
		self.value = ""
		
class Male:
	
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return self.name
		
class Female:
	
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name
		
class Begat:
	
	def __init__(self, father, son):
		self.father = father
		self.son = son
		
	def __str__(self):
		return str(self.father) + " was the father of "+str(self.son)+",\n"
	
class Stanza:
	
	def __init__(self, opening, begats, closing):
		self.opening = opening
		self.begats = begats
		self.closing = closing
		
	def __str__(self):
		return str(self.opening)+''.join(str(begat) for begat in self.begats)+str(self.closing)
		

class Triple:
	
	def __init__(self, opening, stanzas, closing):
		self.opening = opening
		self.stanzas = stanzas
		self.closing = closing
		
	def __str__(self):
		return str(self.opening)+'\n'.join(str(s) for s in self.stanzas)+str(self.closing)

class Gean:
	
	def __init__(self, males, females):
		self.males = males
		self.females = females
		
	def random_triple(self, first):
		closing = ""
		s1 = self.random_stanza(first)
		s2 = self.random_stanza(s1.begats[-1].son)
		s3 = self.random_stanza(s2.begats[-1].son)
		return Triple('',[s1,s2,s3],closing)
		
	def random_stanza(self, father):
		opening = ""
		closing = ""
		begats = []
		for i in range(13):
			b = self.random_begat(father)
			begats.append(b)
			father = b.son
		return Stanza(opening, begats, closing)
		
	def random_begat(self, father):
		#father = self.random_male()
		son = self.random_male()
		return Begat(father, son)
		
	def random_male(self):
		return Male(random.choice(self.males))
		
	def random_show(self):
		s = self.random_triple('Aaban')
		print(s)
		
class Analyse:
	
	def __init__(self, triple):
		self.triple = triple
		
	def word_list(self):
		s = str(self.triple)
		re_word = re.compile(r'\w+')
		ls = re_word.findall(s)
		return ls
		
	def letter_list(self):
		s = str(self.triple)
		re_word = re.compile(r'\w')
		ls = re_word.findall(s)
		return ls
		
	def words(self):
		return len(self.word_list())
		
	def letters(self):
		return len(self.letter_list())
		
	def vowels(self):
		count = 0
		for v in 'aeiou':
			count += self.letter_list().count(v)
			#print(v,count)
		return count
		
	def consonants(self):
		return self.letters() - self.vowels()
		
	def vowel_start(self):
		#print ([w for w in self.word_list() if w[0].lower() in 'aeiou'])
		return len([w for w in self.word_list() if w[0].lower() in 'aeiou'])
		
	def consonant_start(self):
		#print ([w for w in self.word_list() if w[0].lower() not in 'aeiou'])
		return len([w for w in self.word_list() if w[0].lower() not in 'aeiou'])
	


if __name__ == '__main__':
		
	with open('male.txt') as fid:
		males = [x.strip() for x in fid.readlines()]
		
	with open('female.txt') as fid:
		females = [x.strip() for x in fid.readlines()]
	
	g = Gean(males, females)
	
	t = g.random_triple('Aaban')
	
	#g.random_show()
		
	
	print(t)

	a = Analyse(t)
	
	def show_attr(attr):
		val = getattr(a, attr)()
		print(attr, val, prime_factors(val))
	show_attr('words')	
	show_attr('letters')
	show_attr('vowels')
	show_attr('consonants')
	show_attr('vowel_start')
	show_attr('consonant_start')
	#print ('words:',a.words(),prime_factors(a.words()))
	#print('letters:',a.letters(), 
	#print('vowels:',a.vowels(), prime_factors(a.vowels()))
	
