import random

description = """A cipher in which each letter is replaced by one of several possible numbers (usually between 01–99).

The number of possible substitutions is based on the frequency of each letter in English. For example, 'E' may have 4 different codes, while rare letters like 'Q' only have one.


Note:
This simplified version uses a static, predefined mapping for clarity and ease of use. In true homophonic systems, these numbers are randomized or rotated for each message, but our version uses fixed numbers to make decryption reliable and beginner-friendly."""

# Static predefined map
HOMOPHONIC_MAP = {
    'A': ['10', '11'],
    'B': ['12'],
    'C': ['13'],
    'D': ['14', '15'],
    'E': ['16', '17', '18', '19'],
    'F': ['20'],
    'G': ['21'],
    'H': ['22', '23'],
    'I': ['24', '25', '26'],
    'J': ['27'],
    'K': ['28'],
    'L': ['29', '30'],
    'M': ['31'],
    'N': ['32', '33'],
    'O': ['34', '35', '36'],
    'P': ['37'],
    'Q': ['38'],
    'R': ['39', '40'],
    'S': ['41', '42', '43'],
    'T': ['44', '45', '46'],
    'U': ['47'],
    'V': ['48'],
    'W': ['49'],
    'X': ['50'],
    'Y': ['51'],
    'Z': ['52']
}

# Reverse lookup for decryption
REVERSE_MAP = {}
for letter, codes in HOMOPHONIC_MAP.items():
    for code in codes:
        REVERSE_MAP[code] = letter

def encrypt(text, shift=None):
    result = []
    for char in text.upper():
        if char in HOMOPHONIC_MAP:
            code = random.choice(HOMOPHONIC_MAP[char])
            result.append(code)
        elif char == ' ':
            result.append('00')  # Optional: encode space as '00'
    return ' '.join(result)

def decrypt(text, shift=None):
    tokens = text.split()
    result = []
    for token in tokens:
        if token == '00':
            result.append(' ')
        elif token in REVERSE_MAP:
            result.append(REVERSE_MAP[token])
        else:
            result.append('?')  # unknown symbol
    return ''.join(result)
