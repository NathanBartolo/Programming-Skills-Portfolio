from tkinter import *
import random

# Called global variables for difficulty, score, and number of questions
difficulty = ''
score = 0
num_question = 0

# Function to start the quiz 
def start(level):
    global difficulty, score, num_question
    difficulty = level  # Set difficulty level
    score = 0  # Reset score
    num_question = 0  # Reset question count

    # Clear the screen of previous window
    for widget in root.winfo_children():
        widget.destroy()

    # Display the problem
    displayProblem()

# Function to generate a random integer 
def randomInt():
    if difficulty == "Easy":
        return random.randint(1, 9)
    elif difficulty == "Moderate":
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

# Function to randomly choose an arithmetic operation
def decide_operation():
    return random.choice(['+', '-'])

# Function to display a new math problem and random options
def displayProblem():
    global num_question, score
    num_question += 1  # Increment question count

    # End quiz after 10 questions 
    if num_question > 10:
        display_results(root)
        return

    # Generate two random numbers and an operation
    num1 = randomInt()
    num2 = randomInt()
    operation = decide_operation()

    # Ensure no negative results using minus
    if operation == '-':
        num1, num2 = max(num1, num2), min(num1, num2)

    # Calculate 
    correct_answer = eval(f"{num1} {operation} {num2}")
    question = f"{num1} {operation} {num2} = ?"

    # Create answer multiple choice and ensuring one answer is correct
    options = [correct_answer]
    while len(options) < 4:
        option = correct_answer + random.randint(-10, 10)
        if option not in options and option >= 0:
            options.append(option)

    random.shuffle(options)  # Shuffle options for randomness

    # Clear previous widgets and display the question
    for widget in root.winfo_children():
        widget.destroy()

    question_label = Label(root, text=question, font=("Comic Sans MS", 16), bg="#D0E8F2", fg="#2E86AB")
    question_label.pack(pady=20) 

    # Display answer options as buttons
    for option in options:
        #Button style
        option_button = Button(
            root,
            text=option,
            font=("Comic Sans MS", 14),
            width=10,
            bg="#99C1DE",
            fg="#1F4E79",
            relief="raised",
            bd=2,
            command=lambda opt=option: check_answer(opt, correct_answer, root)  # Check answer when clicked
        )
        option_button.pack(pady=5, padx=10)

    # Add hover effect to buttons
    for button in root.winfo_children():
        if isinstance(button, Button):
            button.bind("<Enter>", lambda e: e.widget.config(bg="#82B3C9"))
            button.bind("<Leave>", lambda e: e.widget.config(bg="#99C1DE")) 

# Function to check if the answer is correct
def check_answer(selected, correct_answer, window):
    global score
    # Increase score if correct
    if selected == correct_answer:
        score += 10
        result_text = "Correct!"
    else:
        result_text = "Wrong!"

    
    result_label = Label(window, text=result_text, font=("Comic Sans MS", 14), bg="#D0E8F2", fg="green" if selected == correct_answer else "red")
    result_label.pack(pady=10)

    # Proceed to the next question after a short delay
    window.after(1000, lambda: displayProblem())

# Function to display final results
def display_results(window):
    global score
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the final score
    final_score = Label(window, text=f"Your final score is: {score}/100", font=("Comic Sans MS", 16), bg="#D0E8F2", fg="#2E86AB")
    final_score.pack(pady=20)

    # Determine the rank based on score
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    else:
        rank = "D"
    
    # Display the rank
    rank_label = Label(window, text=f"Rank: {rank}", font=("Comic Sans MS", 16), bg="#D0E8F2", fg="#2E86AB")
    rank_label.pack(pady=10)

    # Option to play again
    play_again_button = Button(window, text="Play Again", font=("Comic Sans MS", 14), width=15, 
                               command=lambda: reset_quiz(window))
    play_again_button.pack(pady=20)

# Function to reset the quiz and go back to the main menu
def reset_quiz(window):
    for widget in window.winfo_children():
        widget.destroy()
    setup_main_menu(window)

# Function to set up the main menu for selecting difficulty
def setup_main_menu(window):
    l1 = Label(window, text="Select Difficulty", font=("Comic Sans MS", 18, "bold"), bg="#D0E8F2", fg="#2E86AB")
    l1.pack(pady=20)

    # Button style 
    button_style = {
        'font': ("Comic Sans MS", 14),
        'bg': "#99C1DE", 
        'fg': "#1F4E79",
        'activebackground': "#82B3C9",  
        'activeforeground': "#1F4E79",
        'relief': "raised",
        'bd': 2,
        'width': 15,
        'highlightbackground': "#1F4E79"
    }

    # Difficulty selection buttons
    b1_easy = Button(window, text="Easy", command=lambda: start('Easy'), **button_style)
    b1_easy.pack(pady=10)

    b1_moderate = Button(window, text="Moderate", command=lambda: start('Moderate'), **button_style)
    b1_moderate.pack(pady=10)

    b1_advanced = Button(window, text="Advanced", command=lambda: start('Advanced'), **button_style)
    b1_advanced.pack(pady=10)


root = Tk()
root.title("Math Quiz")
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg="#D0E8F2")

# Display the main menu
setup_main_menu(root)


root.mainloop()
