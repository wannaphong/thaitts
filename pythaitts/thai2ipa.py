# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
import os
import codecs
import pythaitts
from pythainlp.tokenize import dict_word_tokenize,word_tokenize,dict_trie
from pythainlp.transliterate import romanize as romanization
from marisa_trie import Trie
template_file=os.path.join(os.path.dirname(pythaitts.__file__),"thai2ipa.txt")

with codecs.open(template_file, 'r',encoding='utf8') as f:
	lines = f.read().splitlines()
data={}
for t in lines:
	data[t.split(',')[0]]=t.split(',')[1]
DEFAULT_DICT_TRIE = Trie(data.keys())
def word_tokenize_to_g2p(text):
	wordall=dict_word_tokenize(text, custom_dict=DEFAULT_DICT_TRIE)
	list=[]
	for a in wordall:
		try:
			list.append(data[a])#romanization(a,engine='pyicu'))
		except:
			word_list_icu=word_tokenize(a)
			for b in word_list_icu:
				list.append(romanization(b))
	return '|'.join(list).replace("-","|").split('|')
if __name__ == "__main__":
	while True:
		tt=input("Text : ")
		print(word_tokenize_to_g2p(tt))
