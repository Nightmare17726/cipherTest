description = """A mixture of codes and ciphers. Mary Queen of Scots used this cipher when plotting the assassination of Queen Elizabeth I.

The system uses a cipher alphabet with substitutions for each letter from A–Z, and also includes code numbers (nomenclators) for the most common words.

Note:
This version uses a simplified, static substitution map and supports uppercase-only word codes. Lowercase letters are ignored, and only full-uppercase common words will be replaced with their numeric code.

Common words like THE, AND, and OF are replaced with numbers for better security."""

# Word-level codes (only matches ALL UPPERCASE words)
NOMENCLATORS = {
    "THE": "101",
    "AND": "102",
    "OF": "103",
    "TO": "104",
    "IN": "105"
}

# Letter-level cipher substitutions
LETTER_MAP = {
    'A': '@',
    'B': '#',
    'C': '*',
    'D': '&',
    'E': '1',
    'F': '2',
    'G': '%',
    'H': '3',
    'I': '4',
    'J': '!',
    'K': '+',
    'L': '=',
    'M': '$',
    'N': '^',
    'O': '5',
    'P': '?',
    'Q': '/',
    'R': '<',
    'S': '>',
    'T': '6',
    'U': '7',
    'V': '8',
    'W': '9',
    'X': '[',
    'Y': ']',
    'Z': '~'
}

# Reverse lookups
REVERSE_WORDS = {v: k for k, v in NOMENCLATORS.items()}
REVERSE_LETTERS = {v: k for k, v in LETTER_MAP.items()}

def encrypt(text, shift=None):
    words = text.split()
    result = []

    for word in words:
        if word in NOMENCLATORS:
            result.append(NOMENCLATORS[word])
        else:
            encrypted = ""
            for char in word:
                if char.upper() in LETTER_MAP:
                    encrypted += LETTER_MAP[char.upper()]
                else:
                    encrypted += char  # Keep punctuation or unknown chars
            result.append(encrypted)

    return ' '.join(result)

def decrypt(text, shift=None):
    tokens = text.split()
    result = []

    for token in tokens:
        if token in REVERSE_WORDS:
            result.append(REVERSE_WORDS[token])
        else:
            decrypted = ""
            for char in token:
                if char in REVERSE_LETTERS:
                    decrypted += REVERSE_LETTERS[char]
                else:
                    decrypted += char
            result.append(decrypted)

    return ' '.join(result)
