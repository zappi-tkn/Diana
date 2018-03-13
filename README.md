# Diana
The Diana cipher, using both NSA's DIANA OTP system and columnar transposition.
This employs both diffusion and confusion, strengthing both the polyalphabetic and transposition sections against their own weaknesses.

# Example usage
Plaintext: A quick brown fox jumps over the lazy dog.

The first step is to decide on two keys: one for DIANA and the other for the columnar transposition. It is best if they are not the same length.
Example: MASTERMIND, AWAKENING.

Then, to encrypt using DIANA (see diana.txt for table), one must find their plaintext letter's row / column and travel across / down to the first key letter and write the corresponding letter.
Example (using diana.txt): Column A, Row M = N. 
This is done to every letter, leaving: NJNYTYMAYAAUTJMOBCUISVQNOECRNYKLB

Then, a columnar transposition using its key is performed, without null characters. 
This gives us our final result: JUVLAIYTMOACRNASKMBCYUNYOENTQBYJN

Decryption is this done in the opposite order. As DIANA is reciprocal, encryption is the same as decryption. However, columnar transposition is not.

# Program usage
Encryption: `Diana.Encrypt("MASTERMIND", "AQUICKBROWNFOXJUMPSOVERTHELAZYDOG")`

Decryption: `Diana.Decrypt("MASTERMIND", "JUVLAIYTMOACRNASKMBCYUNYOENTQBYJN")`

# Prerequisites
PyCipher (https://pypi.python.org/pypi/pycipher)
