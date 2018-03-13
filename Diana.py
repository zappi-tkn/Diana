from string import ascii_uppercase
from pycipher import ColTrans

#DKey represents the key for DIANA before being prepared for usage.
#TKey represents the key for transposition.

def Diana(text, key):
    return ascii_uppercase[(25 - ord(key) - ord(text)) % 26]

class textmanipulation:
    def CodeGroup(self,text):
        return " ".join("".join(text[i:i+5]) for i in range(0, len(text), 5))
    def PrepareText(self,text):
        return (" ".join("".join(item) for item in text).split())
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
        output += [UpperKeyNS] * TextLength
        return "".join(output)[:TextLength+1]
KeyGen = keygen()

def OnlyAZ(Text):
    Text=Text.upper()
    NText=""
    for char in Text:
        if char in ascii_uppercase:
            NText += char
    return(NText)

def Encrypt(DKey,TKey,Text):
    Text=OnlyAZ(Text)
    DianaKey=KeyGen.MakeDianaKey(DKey,Text)
    CipherText=[]
    for x in range(len(Text)):
        CipherText.append(Diana(Text[x],DianaKey[x]))
    return(ColTrans(TKey).encipher("".join(CipherText)))
    
def Decrypt(DKey,TKey,Text):
    Text=OnlyAZ(Text)
    Text=ColTrans(TKey).decipher(Text)
    DianaKey=KeyGen.MakeDianaKey(DKey,Text)
    CipherText=[]
    for x in range(len(Text)):
        CipherText.append(Diana(Text[x],DianaKey[x]))
    return("".join(CipherText))
    



            
            