#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: Sebastian Stetter  (DJ5SE)
#License GPL v3
#pygerke is a morse code tool and example collection for python

import pysine, time

#freq = 600.0

morse = {
	"0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....",
	"6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.",
	"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.",
	"h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.",
	"o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-",
	"v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..", "=" : "-...-",
	"/" : "-..-.", "+" : ".-.-.", "-" : "-....-", "." : ".-.-.-", "," : "--..--", "?" : "..--..",
	":" : "---...", "!" : "-.-.--", "'" : ".----."
  }

def send_text(text, wpm=15, farnsworth = 0, freq=550.0):
	lastchar = None
	for c in text:
		c = c.lower()

		if c == ' ':
			wordspace(wpm,farnsworth)
		else:
			if lastchar !=' ':
				charspace(wpm,farnsworth)		
			if c in morse:
				for m in morse[c]:
					if m == '.':
						#if lastchar != ' ':
						time.sleep(ditlen(wpm))
						dit(wpm,freq)
						
					if m == '-':
						#if lastchar != ' ':
						time.sleep(ditlen(wpm))
						dah(wpm,freq)
			else:
				#unknown character
				wordspace(wpm,farnsworth)
				for i in range(4):	
					dit(wpm,freq)
					wordspace(wpm,farnsworth)
		lastchar = c

def ditlen(wpm):
	#PARIS incl. Abstände == 50 ditlängen -> 1 ditlänge@1wpm = 60s / (50 * wpm)
	return 60 / (50 * wpm)

def dit(wpm,freq):
	duration = ditlen(wpm)
	pysine.sine(freq, duration)
	#time.sleep(duration)

def dah(wpm,freq):
	duration =  ditlen(wpm)*3
	pysine.sine(freq,duration)
	#time.sleep(duration)

def charspace(wpm, farnsworth):
	if farnsworth:
		wpm = farnsworth
	time.sleep(ditlen(wpm)*2)

def wordspace(wpm, farnsworth):
	if farnsworth:
		wpm = farnsworth
	time.sleep(ditlen(wpm)*6)





def sample_qso():
	send_text('cq cq cq de dl1aaa dl1aaa dl1aaa pse k',wpm=18)
	wordspace(10,None)

	send_text('dl2bbb',wpm=15, freq=650)
	wordspace(10,None)

	send_text('?',wpm=18)
	wordspace(10,None)

	send_text('dl2bbb',wpm=15, freq=650)
	wordspace(10,None)

	send_text('?se',wpm=18)
	wordspace(10,None)

	send_text('dl2bbb dl2bbb',wpm=15, freq=650)
	wordspace(10,None)

	send_text('dl2bbb de dl1aaa ge rst 589 589 op chris chris k',wpm=18)
	wordspace(10,None)

	send_text('dl1aaa de dl2bbb ge ur rst 5?n 5?n op joe joe+ k dl1aaa de dl2bbb K',wpm=15, freq=650)
	wordspace(10,None)

	send_text('r r tnx rpt es qso 73 k',wpm=18)
	wordspace(10,None)

	send_text('tnx fer contact 73 tu k',wpm=15, freq=650)
	wordspace(10,None)

	send_text('73 tu ee',wpm=18)
	wordspace(10,None)

	send_text('tu ee',wpm=15, freq=650)
	wordspace(10,None)

def creed():
	send_text('Accuracy Transcends Speed = Courtesy at All Times',wpm=18, farnsworth=0,freq=550.0)


if __name__ == '__main__':
	#sample_qso()
	creed()