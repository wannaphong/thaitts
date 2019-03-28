# -*- coding: utf-8 -*-
from __future__ import absolute_import,print_function,unicode_literals
from pythainlp.tokenize import word_tokenize
from pythainlp.transliterate import transliterate
import subprocess
import sys
from .thai2ipa import word_tokenize_to_g2p

class TTS(object):
    def __init__(self,file=False,alphabet="ipa"):
        self.file=file
        self.alphabet=alphabet
    def speak(self,text):
        #self.list_word=word_tokenize(text)
        self.cmd="espeak-ng -m '"+'<phoneme alphabet="ipa">'+' '.join(word_tokenize_to_g2p(text))+"</phoneme>'"
        print(self.cmd)
        try:
            getoutput = subprocess.getoutput(self.cmd)
        except subprocess.CalledProcessError:
            print('plase install espeak-ng')
if __name__ == "__main__":
    print("hi")