#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: Sebastian Stetter DJ5SE
#License GPL v3

from pygerke import *
from datetime import datetime

def telltime():
	now = datetime.now()
	send_text(now.strftime("QTR %H%M"),wpm=15, freq=520)

def start_clock():
	print("started morse clock. CTRL-C to exit")
	telltime()
	intervals = [00,15,30,45]
	while True:
		now = datetime.now()
		if now.minute in intervals:
			telltime()
			time.sleep(60)
		else:
			time.sleep(1)


if __name__ == '__main__':
	start_clock()