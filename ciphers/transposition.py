# transposition.py

def encrypt(text, **kwargs):
    key = kwargs.get("key")
    if not key:
        return "Keyword required."

    # Clean key: remove duplicates and non-alpha
    key = ''.join(sorted(set(key), key=key.index)).upper()
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    key_indices = [i for i, _ in key_order]

    # Create the matrix
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    padded = text.ljust(rows * cols)
    matrix = [padded[i:i + cols] for i in range(0, len(padded), cols)]

    # Read columns in key order
    result = ""
    for idx in key_indices:
        for row in matrix:
            result += row[idx]
    return result.strip()

def decrypt(text, **kwargs):
    key = kwargs.get("key")
    if not key:
        return "Keyword required."

    key = ''.join(sorted(set(key), key=key.index)).upper()
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    key_indices = [i for i, _ in key_order]

    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    full_len = rows * cols
    padded_text = text.ljust(full_len)

    # Determine column lengths
    num_full_cols = len(text) % cols
    col_lengths = [rows] * cols

    # Fill columns
    result_matrix = [''] * rows
    i = 0
    columns = {}
    for idx in key_indices:
        columns[idx] = padded_text[i:i + rows]
        i += rows

    for r in range(rows):
        result_matrix[r] = ''.join(columns[c][r] for c in range(cols))

    return ''.join(result_matrix).rstrip()

description = """A more complex cipher than monoalphabetic substitution, this method rearranges
letters of the plaintext instead of replacing them.

It uses a keyword to determine the order of columns in which letters are read out. The
rule is similar to the Caesar Shift Cipher, except the transformation changes with
every letter based on the keyword.

This cipher is designed to mask character frequency. The Vigenère Cipher, used by the
Confederates during the Civil War, is one of the most famous forms of transposition.



Note:
This implementation uses a user-supplied keyword and performs a columnar
transposition. Spaces are preserved, and non–letter characters are included in their
position.
"""
