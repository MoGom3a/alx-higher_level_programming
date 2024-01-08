#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        leng = len(sentence)
    else:
        leng = 0
    return (leng, sentence if not sentence else sentence[:1])
