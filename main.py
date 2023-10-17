import random
import tkinter as tk

import openai


def generate_sentences(word):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f"Generate a sentence using the word user gives, and add a translation to english next to "
                           f"each sentence in()'. don't number the lines. one sentence each time"
            },
            {
                "role": "user",
                "content": word[0]
            }
        ],

        max_tokens=50,
        n=3,
        # stop=None,
        temperature=0.7
    )
    sentences = [choice['message']['content'].strip() for choice in response['choices']]
    return sentences


word_list = [
    'здравейте', 'благодаря', 'моля', 'добър', 'лош', 'голям', 'малък', 'нов', 'стар',
    'горещ', 'студен', 'дълъг', 'къс', 'красив', 'грозен', 'прав', 'грешен', 'ясен',
    'замъглен', 'бърз'
]

# Create the Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Word Generator Widget")


# Define the function to generate and display sentences
def generate_and_display():
    word = random.sample(word_list, k=1)
    sentences = generate_sentences(word)
    sentence_format = "Word: {}\n\nSentences:\n{}\n{}\n{}"
    display_text.set(sentence_format.format(word, sentences[0], sentences[1], sentences[2]))


# Create a button widget
generate_button = tk.Button(window, text="Generate", command=generate_and_display)
generate_button.pack(pady=10)

# Create a label widget to display the output text
display_text = tk.StringVar()
output_label = tk.Label(window, textvariable=display_text, font=("Arial", 12), justify="left")
output_label.pack(pady=10)


# Define the function to copy the text
def copy_text():
    window.clipboard_clear()
    window.clipboard_append(display_text.get())


# Create a button widget to copy the text
copy_button = tk.Button(window, text="Copy", command=copy_text)
copy_button.pack(pady=5)

# Configure the window with a custom style
window.configure(bg="#f0f0f0")
window.geometry("600x250")
output_label.configure(bg="#f0f0f0", relief="groove")

# Run the Tkinter event loop
window.mainloop()
