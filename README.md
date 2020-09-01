# pygerke
a colection of morse code tools and examples for python
pygerke is named after Friedrich Clemens Gerke, the man who simplified and improved the morse code developed by Alfred Veil. He defined the international morse code, we use today.

## pygerke.py
This is the main module which contains basic morse functions. If run as script, it plays the FISTS creed.

### Function: send_text(text,wpm,farnsworth,freq)
A text to morse code generator. PLays given text as morse code via soundcard.

text: A string to send as morse code
wpm: speed in words per minute
farnsworth: if not 0, the the speed in word per minute is used for character spaces and word spaces.
freq:the frequency of the tone sinewave

## morseclock.py
A morse clock script. It announces the current time (q-code QTR) in format "QTR HHMM" at startup and then every quarter hour. (Intervals can be changed in the list 'intervals' in the script.)

#dependencies
This module uses PySine https://pydigger.com/pypi/pysine for tone generation.

