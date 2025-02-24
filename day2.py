# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:14:50 2024

@author: raj
"""
sent1="I vistited MY from IND on 14-02-19"
normal_sent=sent1.replace("MY", "Maiaysia").replace("IND", "India")
print(normal_sent)
print("hellow world")
#atocorrect
from autocorrect import Speller
spell =Speller(lang="en")
spell("Engilish")
spell("ind")
spell("comuter")

import nltk
nltk.download('punkt')
from nltk import word_tokenize
s1="ntural langgag process deals withi"
s1=word_tokenize(s1)
cor=" ".join([spell(i)for i in s1])
cor
#lemiter
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer as w1
lemiter=w1()
lemiter.lemmatize("programed")


#chunker is use for get main word in sentence






#Sentence tokenization
from nltk import sent_tokenize
sentt=sent_tokenize("We are learning NLP in python. Do you knoe where it is located? Yes u are right. It is in Kopargaon")
sentt

#
from nltk.wsd import lesk
nltk.download("lesk")
s22="keep your saving in the bank"
print(lesk(word_tokenize(s22),"bank"))

s3="It is risky to driver over the bank of river"
print(lesk(word_tokenize(s2),"bank"))









