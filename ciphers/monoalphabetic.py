description = """Each letter of the alphabet is replaced according to a static key using another letter or symbol.

This is a classic substitution cipher where each letter maps uniquely to a different character.



Note:
Our version uses a predefined static mapping with both letters and symbols to make decryption possible inside this program. While real monoalphabetic ciphers may vary per message or user, this version keeps the key fixed for simplicity.

Examples of monoalphabetic systems include Caesar Shift and Morse Code.



Program Substitution Map:
- A = @
- B = K
- C = #
- D = L
- E = &
- F = Z
- G = !
- H = Y
- I = %
- J = U
- K = $
- L = Q
- M = *
- N = ^
- O = R
- P = +
- Q = W
- R = =
- S = ~
- T = X
- U = >
- V = <
- W = ?
- X = J
- Y = M
- Z = B
"""

# Static substitution map: A–Z mapped to 26 mixed symbols/letters
SUBSTITUTION_MAP = {
    'A': '@',
    'B': 'K',
    'C': '#',
    'D': 'L',
    'E': '&',
    'F': 'Z',
    'G': '!',
    'H': 'Y',
    'I': '%',
    'J': 'U',
    'K': '$',
    'L': 'Q',
    'M': '*',
    'N': '^',
    'O': 'R',
    'P': '+',
    'Q': 'W',
    'R': '=',
    'S': '~',
    'T': 'X',
    'U': '>',
    'V': '<',
    'W': '?',
    'X': 'J',
    'Y': 'M',
    'Z': 'B'
}

# Reverse map for decryption
REVERSE_MAP = {v: k for k, v in SUBSTITUTION_MAP.items()}

def encrypt(text, shift=None):
    result = ""
    for char in text.upper():
        if char in SUBSTITUTION_MAP:
            result += SUBSTITUTION_MAP[char]
        elif char == ' ':
            result += ' '  # keep spaces
        else:
            result += '?'  # unknown characters
    return result

def decrypt(text, shift=None):
    result = ""
    for char in text:
        if char in REVERSE_MAP:
            result += REVERSE_MAP[char]
        elif char == ' ':
            result += ' '
        else:
            result += '?'  # unknown symbol
    return result
