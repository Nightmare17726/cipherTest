# true_codes.py

description = """True Codes use fixed words or phrases to represent pre-agreed meanings.
These codes rely on a shared codebook between sender and receiver.

They are not based on patterns or math — only prearranged meaning.
Example: "Blue Apple" = "Attack", "Red Banana" = "Retreat"."""

# Static sample codebook
codebook = {
    "attack": "Blue Apple",
    "retreat": "Red Banana",
    "north": "Iron Owl",
    "south": "Gold Bear",
    "east": "Silver Fox",
    "west": "Shadow Wolf",
    "now": "Delta Tango",
    "wait": "Hold Zero",
    "target": "Echo Kite",
}

# Reverse codebook for decryption
reverse_codebook = {v.lower(): k for k, v in codebook.items()}

def encrypt(text, shift=None):
    words = text.lower().split()
    return " ".join(codebook.get(word, word) for word in words)

def decrypt(text, shift=None):
    words = text.split(" ")
    result = []
    buffer = []
    for word in words:
        buffer.append(word)
        phrase = " ".join(buffer).lower()
        if phrase in reverse_codebook:
            result.append(reverse_codebook[phrase])
            buffer = []
    if buffer:
        result.extend(buffer)  # any unmatched leftovers
    return " ".join(result)
