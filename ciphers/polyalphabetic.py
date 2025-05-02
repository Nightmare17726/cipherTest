description = """A cipher in which each letter in the plaintext is encrypted using a different Caesar shift based on a repeating keyword.

Each letter in the keyword defines a shift: A = 0, B = 1, ..., Z = 25. This process repeats across the message.

This technique defeats simple frequency analysis by spreading letter distributions over multiple cipher alphabets. The Vigenère Cipher is the most famous example of this kind.

Note:
This implementation requires an uppercase-only keyword. Non-letter characters in the message are preserved and ignored in the shifting pattern.
"""

def _format_keyword(keyword):
    return [ord(char.upper()) - ord('A') for char in keyword if char.isalpha()]

def encrypt(text, shift=None, key="KEY"):
    if not key or not any(c.isalpha() for c in key):
        return "Error: Keyword must contain at least one letter."

    key_shifts = _format_keyword(key)
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = key_shifts[key_index % len(key_shifts)]
            shifted = chr((ord(char) - base + shift_amount) % 26 + base)
            result.append(shifted)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

def decrypt(text, shift=None, key="KEY"):
    if not key or not any(c.isalpha() for c in key):
        return "Error: Keyword must contain at least one letter."

    key_shifts = _format_keyword(key)
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = key_shifts[key_index % len(key_shifts)]
            shifted = chr((ord(char) - base - shift_amount) % 26 + base)
            result.append(shifted)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)
