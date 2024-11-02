from tkinter import *
from tkinter import filedialog
import random

root = Tk()
root.title("Joke Time")
root.geometry("500x400")
root.resizable(0, 0)
#Function to display a random joke
def randomjoke():
    #called punchline variable as global
    global punchline
    txtarea.delete("1.0", 'end')#clear text areas
    with open("RandomJokes.txt") as file_handler:#Open file
        jokes = file_handler.readlines()
        
    setup, punchline = random.choice(jokes).rstrip().split('?')#Stop the read when it detects comma
    txtarea.insert(END, setup + '?')
    joke_btn.pack_forget()  # Hide the "Tell me a joke" button
    punchline_btn.pack(pady=5)  # Show the "Punchline" button

def showPunchline():
    txtarea.delete("1.0", 'end')
    txtarea.insert(END, punchline)
    punchline_btn.pack_forget()  # Hide the "Punchline" button
    joke_btn.pack(pady=5)  # Show the "Tell me a joke" button again
# Define the button style
button_style = {
    'font': ("Helvetica", 12, 'bold'),   # Increased font size and bold
    'bg': "#4682B4",  # Steel blue background
    'fg': "white",    # White text color
    'activebackground': "#5F9EA0",  # Cadet blue on hover
    'activeforeground': "white",    # White text on hover
    'relief': "groove",    # Groove border style
    'bd': 3,               # Border width
    'width': 25,           # Increased width for better visibility
    'highlightbackground': "#4682B4",  # Highlight color to match background
    'padx': 5,             # Padding around text horizontally
    'pady': 5              # Padding around text vertically
}

txtarea = Text(root, height=10, width=40, font=("Helvetica", 14, 'bold'), bg="#E3DFFD", fg="#333333", 
               relief="flat", padx=10, pady=10)
txtarea.pack(pady=20)

joke_btn = Button(root, text="Tell me a joke", command=randomjoke, **button_style)
joke_btn.pack(pady=5)

punchline_btn = Button(root, text="Show Punchline", command=showPunchline, **button_style)

root.mainloop()
