# caesar.py

description = """A substitution cipher that shifts each letter in the alphabet by a fixed number of positions (1–25).

There are 25 possible Caesar ciphers for the English alphabet.

It is the foundation of many more advanced encryption techniques but offers minimal security on its own."""

def encrypt(text, shift, **kwargs):
    return _caesar(text, shift)

def decrypt(text, shift, **kwargs):
    return _caesar(text, -shift)

def _caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
