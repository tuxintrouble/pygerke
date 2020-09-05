#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: Sebastian Stetter  (DJ5SE)
#License GPL v3


from tkinter import *
import os, time
from pygerke import dit, dah, ditlen

class KeyboardPaddle():

    def __init__(self,dit_func, dah_func, left_key='l', right_key='p',wpm=15,freq=550.0,farnsworth=0):


        self.dit_func=dit_func
        self.dah_func=dah_func
        self.l_key = left_key
        self.r_key = right_key
        self.wpm = wpm
        self.freq = freq
        self.farnsworth = farnsworth

        self.l_down = False
        self.r_down = False
        self.last_down = None

        self.setup_ui()

    def setup_ui(self):
        self.window = Tk()
        self.window.title('Keyboard Paddle')
        self.window.bind('<KeyPress>', self.on_key_press)
        self.window.bind('<KeyRelease>', self.on_key_release)
        self.window.bind_all("<FocusIn>", self.on_focus_in)
        self.window.bind_all("<FocusOut>", self.on_focus_out)
        self.window.wm_protocol("WM_DELETE_WINDOW", self.quit)
        self.window.after(1,self.process) #do stuff along mainloop
        self.window.mainloop()

    def on_focus_in(self,e):
        #prevent system from re-sending key events while holding down
        os.system('xset r off')
        print("got focus")

    def on_focus_out(self,e):
        #xset works globally, so we need to turn it on again when we lose focus
        os.system('xset r on')
        print("lost focus")

    def on_key_press(self,e):
        
        if e.char == self.l_key:
            self.l_down = True
            self.last_down='l'
            

        if e.char == self.r_key:
            self.r_down = True
            self.last_down='r'
            
    def on_key_release(self,e):
        
        if e.char == self.l_key:
            self.l_down = False

        if e.char == self.r_key:
            self.r_down = False

    def process(self):
        #do keying logic here
            if self.r_down & self.l_down:
                if self.last_down == 'r':
                    self.dah_func(self.wpm,self.freq)
                    time.sleep(ditlen(self.wpm))
                    self.dit_func(self.wpm,self.freq)
                    time.sleep(ditlen(self.wpm))
                    
                if self.last_down == 'l':
                    self.dit_func(self.wpm,self.freq)
                    time.sleep(ditlen(self.wpm))
                    self.dah_func(self.wpm,self.freq)
                    time.sleep(ditlen(self.wpm))                        

            elif self.l_down: 
                self.dit_func(self.wpm,self.freq)
                time.sleep(ditlen(self.wpm))
                
            elif self.r_down: 
                self.dah_func(self.wpm,self.freq)
                time.sleep(ditlen(self.wpm))

            else:
                pass
            
            self.window.after(1,self.process)
            

    def quit(self):
        #xset works globally, so we need to turn it on again when we quit the application
        os.system('xset r on')
        self.window.destroy()


kp = KeyboardPaddle(dit, dah, wpm=15)
