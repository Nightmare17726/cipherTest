description = """Steganography is the practice of hiding information inside other files, such as images or audio.

The most common method is Least Significant Bit (LSB) encoding, which hides bits of the secret message in the least significant bits of pixel data—typically in the red, green, or blue (RGB) color channels.

Since changes to the least significant bit do not drastically alter the visual output, this allows messages to be hidden in plain sight.

TO PUT IT MORE SIMPLY: Stenography uses the way computers process colors/images against us; they make tiny, imperceptible changes to each pixel in an image to create space for whatever message, document, or other image someone is trying to hide. 


Note:
- This demo does not implement steganographic encoding.
- Instead, it provides a calculator to estimate the number of pixels (and thus, the data capacity) based on image dimensions.
"""

def encrypt(text, shift=None, **kwargs):
    try:
        width, height = map(int, text.lower().replace("×", "x").split("x"))
        pixels = width * height
        return f"{width:,} × {height:,} = {pixels:,} pixels\nThis could represent up to {pixels * 3:,} bits (1,048,576 pixels = ~393 KB)"
    except:
        return "Please enter a valid resolution (e.g., 1920x1080)."

def decrypt(text, shift=None, **kwargs):
    return "This mode is informational only. No decryption is available."
