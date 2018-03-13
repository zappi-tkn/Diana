from string import ascii_uppercase
from pycipher import ColTrans

class transposition:  
 
    def encrypt(self, text, key):
        return ColTrans(key).encipher(text)
    def decrypt(self, text, key):
        return ColTrans(key).decipher(text)
    def num(self, x):
        return x+1
Trans = transposition()

def Diana(text, key):
    return ascii_uppercase[(25 - ord(key) - ord(text)) % 26]

class textmanipulation:
    def CodeGroup(self,text):
        return " ".join("".join(text[i:i+5]) for i in range(0, len(text), 5))
    def PrepareText(self,text):
        return (" ".join("".join(text[i]) for i in range(0, len(text), 1)).split())
TextManip = textmanipulation()

class keygen:
    def MakeDianaKey(self, PreKey, text):
        output = []
        TextLength = len(text)
     
        if(PreKey.isalpha() is False):
            print("Key is not alphanumeric! Result will not be decryptable...")
       
        UpperKey = PreKey.upper()
        UpperKeyNS = UpperKey.replace(" ","")
        UpperKeyNS = UpperKeyNS.replace("\n","")
        for TextLength in range(TextLength):
            output.append(UpperKeyNS)
        return "".join(output)[:TextLength+1]
KeyGen = keygen()

def OnlyAZ(Text):
    Text=Text.upper()
    ValidLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NText=""
    for char in Text:
        if char in ValidLetters:
            NText += char
    return(NText)

def Encrypt(Key,Text):
    Text=OnlyAZ(Text)
    DianaKey=KeyGen.MakeDianaKey(Key,Text)
    CipherText=[]
    for x in range(len(Text)):
        CipherText.append(Diana(Text[x],DianaKey[x]))
    return(Trans.encrypt("".join(CipherText),Key))
    
def Decrypt(Key,Text):
    Text=OnlyAZ(Text)
    Text=Trans.decrypt(Text, Key)
    DianaKey=KeyGen.MakeDianaKey(Key,Text)
    CipherText=[]
    for x in range(len(Text)):
        CipherText.append(Diana(Text[x],DianaKey[x]))
    return("".join(CipherText))
    



            
            
