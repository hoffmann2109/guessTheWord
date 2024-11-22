import random
import nltk
import tkinter as tk
from tkinter import messagebox

nltk.download("words")

# Load words from the provided German word file (nouns with 5 letters)
def load_german_words():
    with open("five_letter_german_nouns.txt", "r", encoding="utf-8") as file:
        german_words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return german_words

# Load solution words from the list with more common nouns (solution_words.txt)
def load_solution_words():
    with open("solution_words.txt", "r", encoding="utf-8") as file:
        solution_words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return solution_words

# Feedback colors
COLORS = {
    "correct": "green",
    "misplaced": "yellow",
    "absent": "gray",
    "default": "white"
}

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deutsches Wordle")

        # Load words for guesses and solutions
        self.word_list = load_german_words()  # Full list for guesses
        self.solution_list = load_solution_words()  # Curated list for solutions
        self.target_word = random.choice(self.solution_list)  # Select a target word
        self.attempts = 6
        self.current_attempt = 0
        self.guess = ""

        # Set up grid for guesses
        self.grid = [[None for _ in range(5)] for _ in range(self.attempts)]
        self.create_grid()

        # Set up keyboard input
        self.root.bind("<Key>", self.on_key_press)

    def create_grid(self):
        for row in range(self.attempts):
            for col in range(5):
                label = tk.Label(self.root, text="", width=4, height=2, font=("Helvetica", 18), bg=COLORS["default"],
                                 borderwidth=2, relief="solid")
                label.grid(row=row, column=col, padx=5, pady=5)
                self.grid[row][col] = label

    def on_key_press(self, event):
        if event.char.isalpha() and len(self.guess) < 5:
            self.guess += event.char.lower()  # Store lowercase
            self.update_grid(uppercase=True)  # Display uppercase
        elif event.keysym == "BackSpace" and len(self.guess) > 0:
            self.guess = self.guess[:-1]
            self.update_grid(uppercase=True)
        elif event.keysym == "Return" and len(self.guess) == 5:
            self.check_guess()

    def update_grid(self, uppercase=False):
        for col in range(5):
            char = self.guess[col].upper() if uppercase and col < len(self.guess) else ""
            self.grid[self.current_attempt][col].config(text=char)

    def check_guess(self):
        if self.guess not in self.word_list:
            messagebox.showinfo("Kein Wort!", "Wort ist nicht in Wortliste enthalten.")
            return

        feedback = self.get_feedback(self.guess)
        for col, color in enumerate(feedback):
            self.grid[self.current_attempt][col].config(bg=color)

        if self.guess == self.target_word:
            messagebox.showinfo("Gratuliere!", f"Du hast das Wort '{self.target_word}' erraten!")
            self.root.quit()
        elif self.current_attempt + 1 == self.attempts:
            messagebox.showinfo("Game Over", f"Das gesuchte Wort war '{self.target_word}'. Viel Glück beim nächsten Mal!")
            self.root.quit()
        else:
            self.current_attempt += 1
            self.guess = ""
            self.update_grid()

    def get_feedback(self, guess):
        feedback = []
        for i, char in enumerate(guess):
            if char == self.target_word[i]:
                feedback.append(COLORS["correct"])  # Correct letter in the correct position
            elif char in self.target_word:
                feedback.append(COLORS["misplaced"])  # Correct letter but in the wrong position
            else:
                feedback.append(COLORS["absent"])  # Letter not in the word
        return feedback


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
