import tkinter as tk
from tkinter import messagebox

# Function to perform Caesar cipher encryption
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Function to perform Caesar cipher decryption
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle button click (encryption)
def encrypt_message():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

# Function to handle button click (decryption)
def decrypt_message():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

# Creating the main Tkinter window
root = tk.Tk()
root.title("Caesar Cipher Tool")

# Input area for the plaintext
input_label = tk.Label(root, text="Enter your message:")
input_label.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Shift input
shift_label = tk.Label(root, text="Enter the shift (0-25):")
shift_label.pack()

shift_entry = tk.Entry(root)
shift_entry.pack()

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.pack()

# Output area for the encrypted/decrypted text
output_label = tk.Label(root, text="Result:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Start the Tkinter main loop
root.mainloop()
