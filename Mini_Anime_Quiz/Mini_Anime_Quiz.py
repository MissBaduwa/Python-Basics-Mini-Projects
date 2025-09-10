# ===============================
# Anime Quiz Game – Week 1 Python Project
# ===============================

# --------- Imports ----------
import os
import time                     # For adding small delays for effect


# --------- Question Class ---------
# Define a Question class to store a quiz question
class Question:

    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = options
        self.answer = answer


# -------------------------------
# List of Anime Quiz Questions
# -------------------------------
questions = [
    Question(
        "Which anime features the character 'Tanjiro Kamado'?",
        ["Demon Slayer", "Naruto", "Attack on Titan", "Jujutsu Kaisen"],
        "Demon Slayer"
    ),
    Question(
        "In 'My Hero Academia', what is Deku's real name?",
        ["Katsuki Bakugo", "Izuku Midoriya", "Shoto Todoroki", "All Might"],
        "Izuku Midoriya"
    ),
    Question(
        "Which anime has a high school student with a notebook that can kill people?",
        ["Death Note", "Bleach", "One Piece", "Dragon Ball Z"],
        "Death Note"
    ),
    Question(
        "What is the main goal of the characters in 'One Piece'?",
        ["Become the Pirate King", "Win the tournament", "Save the world", "Find the Philosopher's Stone"],
        "Become the Pirate King"
    ),
    Question(
        "In 'Jujutsu Kaisen', what is Yuji Itadori searching for?",
        ["Sukuna's fingers", "Dragon Balls", "Hollow souls", "Tailed Beasts"],
        "Sukuna's fingers"
    )
]


# --------- Functions ----------
# Function to clear screen for better readability
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to run the quiz
def run_quiz(questions):

    score = 0                                   # Initialize score
    clear_screen()
    print("✨ Welcome to the Anime Quiz Game! ✨")
    print("Test your anime knowledge and have fun! 🤩\n")
    time.sleep(1)                               # Small pause for dramatic effect

    # Loop through all questions
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q.question_text}")       # Display question
        for idx, option in enumerate(q.options, start=1):
            print(f"  {idx}. {option}")         # Display options

        # Get user input with exception handling
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if choice < 1 or choice > 4:
                    raise ValueError("Please enter a number between 1 and 4.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

        # Check if answer is correct
        selected = q.options[choice - 1]
        if selected == q.answer:
            print("✅ Correct! 🎉\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {q.answer}\n")
        time.sleep(0.5)             # Small pause before next question

    # Final Score Display
    print("=====================================")
    print(f"🎯 Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Perfect score! Anime Master! 🌟")
    elif score >= len(questions) // 2:
        print("👍 Nice job! Keep leveling up your anime knowledge!")
    else:
        print("💡 Keep practicing! Every question is a step to mastery!")
    print("=====================================")

    # Save high score to a file
    save_score(score)



# Function to save high score (Saves the player's score to a file called 'high_scores.txt'.)
def save_score(score):

    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{score}/{len(questions)}\n")
        print("\n📄 Your score has been saved to 'high_scores.txt'.")

    except Exception as e:
        print(f"Error saving score: {e}")


# -------------------------------
# Run the game
# -------------------------------
if __name__ == "__main__":
    run_quiz(questions)
