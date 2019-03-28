# -*- coding: utf-8 -*-
from __future__ import absolute_import,print_function,unicode_literals
from pythainlp.tokenize import word_tokenize
from pythainlp.transliterate import transliterate
import subprocess
import sys
from .thai2ipa import word_tokenize_to_g2p

class TTS(object):
    def __init__(self,alphabet="ipa"):
        self.alphabet=alphabet
    def speak(self,text,file=None):
        #self.list_word=word_tokenize(text)
        self.cmd="espeak-ng -m '"+'<phoneme alphabet="ipa">'+' '.join(word_tokenize_to_g2p(text))+"</phoneme>'"
        if file!=None:
            self.cmd+=" -w "+file
        print(self.cmd)
        try:
            getoutput = subprocess.getoutput(self.cmd)
        except subprocess.CalledProcessError:
            print('plase install espeak-ng')
if __name__ == "__main__":
    print("hi")