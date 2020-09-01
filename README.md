# pygerke
a colection of morse code tools and examples for python
pygerke is named after Friedrich Clemens Gerke, the man who simplified and improved the morse code developed by Alfred Veil. He defined the international morse code, we use today.

##send_text(text,wpm,farnsworth,freq)
text: A string to send as morse code
wpm: speed in words per minute
farnsworth: if not 0, the the speed in word per minute is used for character spaces and word spaces.
freq:the frequency of the tone sinewave

##morseclock.py
A morse clock. I announces the current time (QTR) in format "QTR HHMM" at startup and then every quarter hour. Intervals can be changed in the list 'intervals' in the script.

#dependencies
This module uses PySine https://pydigger.com/pypi/pysine for tone generation.

