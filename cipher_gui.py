# Cipher Tests program. Written by Chase Franse & Chat-GPT4o

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from ciphers import caesar  # External Caesar Cipher logic
from ciphers import homophonic # External Homophonic Substitution logic
from ciphers import monoalphabetic # External Monoalphabetic Substitution logic
from ciphers import nomenclator # External Nomenclator Cipher logic
from ciphers import polyalphabetic # External Polyalphabetic Cipher logic
from ciphers import transposition # External Transposition Cipher logic
from ciphers import stenography # External Stenography Explaination

# Cipher registry
CIPHERS = {
    "Caesar Cipher": {
        "description": caesar.description,
        "encrypt": caesar.encrypt,
        "decrypt": caesar.decrypt,
        "uses_shift": True
    },
    "Homophonic Substitution": {
        "description": homophonic.description,
        "encrypt": homophonic.encrypt,
        "decrypt": homophonic.decrypt
    },
    "Monoalphabetic Substitution": {
        "description": monoalphabetic.description,
        "encrypt": monoalphabetic.encrypt,
        "decrypt": monoalphabetic.decrypt
    },
    "Nomenclator Cipher": {
        "description": nomenclator.description,
        "encrypt": nomenclator.encrypt,
        "decrypt": nomenclator.decrypt
    },
    "Polyalphabetic Cipher": {
        "description": polyalphabetic.description,
        "encrypt": polyalphabetic.encrypt,
        "decrypt": polyalphabetic.decrypt,
        "uses_keyword": True
    },
    "Transposition Cipher": {
        "description": transposition.description,
        "encrypt": transposition.encrypt,
        "decrypt": transposition.decrypt,
        "uses_keyword": True
    },
    "Stenography (Explination)": {
        "description": stenography.description,
        "encrypt": stenography.encrypt,
        "decrypt": stenography.decrypt
    },
    "Null Cipher": {
        "description": "Coming soon.",
        "encrypt": lambda text, shift=None: "Not implemented",
        "decrypt": lambda text, shift=None: "Not implemented"
    },
    "True Codes": {
        "description": "Coming soon.",
        "encrypt": lambda text, shift=None: "Not implemented",
        "decrypt": lambda text, shift=None: "Not implemented"
    },
}

# GUI Setup
root = tk.Tk()
root.title("Cipher Tester")
root.geometry("1000x500")

# Dark Mode Detection
try:
    bg_rgb = root.winfo_rgb(root.cget("bg"))
    brightness = sum(bg_rgb) / (3 * 65535)
    DARK_MODE = brightness < 0.5
except:
    DARK_MODE = True

# Theme colors
DARK_BG = "#1e1e1e" if DARK_MODE else "white"
LIGHT_TEXT = "white" if DARK_MODE else "black"
DIVIDER_COLOR = "white" if DARK_MODE else "black"
ENTRY_BG = "#2b2b2b" if DARK_MODE else "white"
ENTRY_TEXT = "white" if DARK_MODE else "black"

root.configure(bg=DARK_BG)

# Layout
main_frame = tk.Frame(root, bg=DARK_BG)
main_frame.pack(fill=tk.BOTH, expand=True)

# LEFT PANEL
left_frame = tk.Frame(main_frame, width=330, bg=DARK_BG)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
left_frame.pack_propagate(False)

tk.Label(left_frame, text="Cipher Name:", font=("Helvetica", 14, "bold"), fg=LIGHT_TEXT, bg=DARK_BG).pack(pady=10)
cipher_name_label = tk.Label(left_frame, text="", font=("Helvetica", 12), fg=LIGHT_TEXT, bg=DARK_BG)
cipher_name_label.pack()

tk.Label(left_frame, text="Description:", fg=LIGHT_TEXT, bg=DARK_BG).pack(pady=5)
description_text = tk.Text(left_frame, height=15, wrap='word', state='disabled',
                           bg=ENTRY_BG, fg=ENTRY_TEXT, insertbackground=ENTRY_TEXT)
description_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# DIVIDER
divider = tk.Frame(main_frame, width=2, bg=DIVIDER_COLOR)
divider.pack(side=tk.LEFT, fill=tk.Y)

# RIGHT PANEL
right_frame = tk.Frame(main_frame, bg=DARK_BG)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(right_frame, text="Choose a Cipher:", bg=DARK_BG, fg=LIGHT_TEXT).pack(pady=5)
cipher_var = tk.StringVar()
cipher_menu = tk.OptionMenu(right_frame, cipher_var, *CIPHERS.keys())
cipher_menu.config(bg=ENTRY_BG, fg=ENTRY_TEXT, highlightbackground=DIVIDER_COLOR)
cipher_menu.pack()
cipher_var.set("Caesar Cipher")

# Message input
message_label = tk.Label(right_frame, text="Enter your message:", bg=DARK_BG, fg=LIGHT_TEXT)
message_label.pack(pady=5)
input_box = tk.Text(right_frame, height=5, width=70, bg=ENTRY_BG, fg=ENTRY_TEXT, insertbackground=ENTRY_TEXT)
input_box.pack()

# Output
tk.Label(right_frame, text="Output:", bg=DARK_BG, fg=LIGHT_TEXT).pack(pady=5)
output_box = tk.Text(right_frame, height=5, width=70, state='disabled', bg=ENTRY_BG, fg=ENTRY_TEXT)
output_box.pack()

# Shift Input
shift_label = tk.Label(right_frame, text="Shift Amount (1–25):", bg=DARK_BG, fg=LIGHT_TEXT)
shift_var = tk.StringVar(value="3")
shift_entry = tk.Entry(right_frame, textvariable=shift_var,
                       bg=ENTRY_BG, fg=ENTRY_TEXT, insertbackground=ENTRY_TEXT)

# Keyword Input
keyword_label = tk.Label(right_frame, text="Enter Keyword:", bg=DARK_BG, fg=LIGHT_TEXT)
keyword_var = tk.StringVar(value="KEY")
keyword_entry = tk.Entry(right_frame, textvariable=keyword_var,
                         bg=ENTRY_BG, fg=ENTRY_TEXT, insertbackground=ENTRY_TEXT)

# Buttons
button_frame = tk.Frame(right_frame, bg=DARK_BG)
encrypt_btn = ttk.Button(button_frame, text="Encrypt", command=lambda: run_cipher(False))
decrypt_btn = ttk.Button(button_frame, text="Decrypt", command=lambda: run_cipher(True))

# Style
style = ttk.Style()
style.theme_use('alt')
style.configure("TButton", background=ENTRY_BG, foreground=LIGHT_TEXT)
style.map("TButton", background=[("active", ENTRY_BG), ("pressed", ENTRY_BG)])

def update_description(*_):
    selected = cipher_var.get()
    cipher = CIPHERS[selected]
    cipher_name_label.config(text=selected)
    description_text.config(state='normal')
    description_text.delete("1.0", tk.END)
    description_text.insert(tk.END, cipher["description"])
    description_text.config(state='disabled')

    message_label.config(text="Enter Image Size (e.g., 1920x1080):" if "sten" in selected.lower() else "Enter your message:")

    # Clear shift/keyword first
    shift_label.pack_forget()
    shift_entry.pack_forget()
    keyword_label.pack_forget()
    keyword_entry.pack_forget()

    # Show inputs in correct order
    if cipher.get("uses_keyword"):
        keyword_label.pack(pady=(10,0))
        keyword_entry.pack()
    if cipher.get("uses_shift"):
        shift_label.pack(pady=(10,0))
        shift_entry.pack()

    # Always pack buttons last
    button_frame.pack_forget()
    button_frame.pack(pady=10)
    encrypt_btn.pack(side=tk.LEFT, padx=10)
    decrypt_btn.pack(side=tk.LEFT, padx=10)

def run_cipher(decrypt=False):
    selected = cipher_var.get()
    cipher = CIPHERS[selected]
    input_text = input_box.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showwarning("Input Required", "Please enter a message.")
        return

    kwargs = {}
    if cipher.get("uses_shift"):
        try:
            shift = int(shift_var.get())
            if not 1 <= shift <= 25:
                raise ValueError
            kwargs["shift"] = shift
        except ValueError:
            messagebox.showerror("Invalid Shift", "Shift must be 1–25.")
            return

    if cipher.get("uses_keyword"):
        keyword = keyword_var.get().strip()
        if not keyword or not keyword.isalpha():
            messagebox.showerror("Invalid Keyword", "Keyword must contain only letters.")
            return
        kwargs["keyword"] = keyword

    func = cipher["decrypt"] if decrypt else cipher["encrypt"]
    try:
        result = func(input_text, **kwargs)
    except Exception as e:
        result = f"Error: {e}"

    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)
    output_box.config(state='disabled')

cipher_var.trace_add("write", update_description)
update_description()
root.mainloop()
