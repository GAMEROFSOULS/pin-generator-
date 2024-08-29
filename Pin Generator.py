import tkinter as tk
import random
import string

def generate_pin(length):
    characters = string.ascii_letters + string.digits
    pin = [random.choice(characters) for _ in range(length)]
    return ''.join(pin)

def on_generate_button_click():
    length = int(length_entry.get())
    pin = generate_pin(length)
    pin_label.config(text=f"Generated PIN: {pin}")

# Set up the main window
window = tk.Tk()
window.title("PIN Generator")
window.geometry("300x200")

# Add a label
title_label = tk.Label(window, text="PIN Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

# Add an entry for PIN length
length_label = tk.Label(window, text="Enter PIN Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(window, width=10)
length_entry.pack(pady=5)

# Add a button to generate the PIN
generate_button = tk.Button(window, text="Generate PIN", command=on_generate_button_click)
generate_button.pack(pady=10)

# label to display the generated PIN
pin_label = tk.Label(window, text="Generated PIN: ", font=("Helvetica", 14))
pin_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
