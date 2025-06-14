import json
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Load the emoji dictionary
with open("text_to_emoji/emoji.json", encoding="utf8") as file:
    emojis = json.load(file)

def to_emoji(word):
    # Ignore short words
    if len(word) < 3:
        return word

    # Find the best match in the emoji dictionary
    for emoji in emojis:
        # Check if the word is in the emoji's name
        if word.lower() in emoji['name'].lower():
            return emoji['char']

    # If no emoji found, return the original word
    return word

def convert_text_to_emoji(text):
    # Split text into words
    words = text.split(' ')
    # Convert words to emojis where possible
    converted_text = ' '.join([to_emoji(word) for word in words])
    return converted_text

def submit():
    text = input_text.get('1.0', 'end-1c')
    if text:
        emoji_text = convert_text_to_emoji(text)
        result_text.insert(tk.INSERT, emoji_text)
    else:
        messagebox.showinfo("Error", "Por favor, introduzca un texto.")

# Create the tkinter window
window = tk.Tk()
window.title("Conversor de texto a emoji - Versión de prueba (solo inglés)")

input_label = tk.Label(window, text="Introduce un texto en inglés:")
input_label.pack()

input_text = scrolledtext.ScrolledText(window, width=50, height=10)
input_text.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(window, text="Texto convertido a emojis:")
result_label.pack()

result_text = scrolledtext.ScrolledText(window, width=50, height=10)
result_text.pack()

def main():
    # Start the GUI
    window.mainloop()


if __name__ == "__main__":
    main()

