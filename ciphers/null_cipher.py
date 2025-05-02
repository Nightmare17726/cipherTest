# null_cipher.py

description = """A form of steganography where the message is hidden within an innocent-looking sentence.

In this simplified version, the hidden message is revealed by reading the first letter of each word.
Historically used when encryption was too dangerous or forbidden.


NOTE: In this version, we do *not* use AI to make the sentences make sense, so if it come out as garbage (encryped garbage), that's why."""

def encrypt(message, shift=None):
    """
    Hides the message using the Null Cipher technique:
    Inserts each letter of the message as the first letter of a word in a cover sentence.
    """
    words = []
    for letter in message:
        if letter.isalpha():
            filler = "apple" if letter.islower() else "Banana"
            word = letter + filler[1:]  # Replace first letter
        else:
            word = "xenon"
        words.append(word)
    return " ".join(words)

def decrypt(text, shift=None):
    """
    Extracts the first letter of each word to recover the hidden message.
    """
    words = text.split()
    return "".join(word[0] for word in words if word)
