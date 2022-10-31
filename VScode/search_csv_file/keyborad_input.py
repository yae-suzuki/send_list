

from ctypes.wintypes import WORD
###keyborad input word 
def __init__(self,input_word,word):
    self.input_word = input_word
    self.word = word   

def kye_inp():
    input_word = str(input())   
    return input_word

if __name__ == '__main__':
    word = kye_inp()
    print(word)
