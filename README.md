# Deutsches Wordle

A German language adaptation of the popular Wordle game. This version allows players to guess 5-letter German nouns, with color-coded feedback after each guess.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Customization](#customization)
- [Technologies Used](#technologies-used)

## Features
- **German Word Base**: 
  - Uses a full list of 5-letter German nouns (`five_letter_german_nouns.txt`) for guesses.
  - The target word is selected from a curated list of common German nouns (`solution_words.txt`), ensuring fair and challenging gameplay.
- **Interactive GUI**: Built with Tkinter for an intuitive, grid-based display.
- **Color-Coded Feedback**:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter, wrong position.
  - **Gray**: Letter not in the word.
- **Six Attempts**: Players have up to six attempts to guess the target word.
- **Keyboard Input**: Uses keyboard inputs to type, delete, and submit guesses.
- **In-Game Alerts**: Messages for win/lose conditions and invalid words.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/german-wordle.git
   ```
2. Navigate to the project directory:
   ```bash
   cd german-wordle
   ```
3. Install the required dependencies:
   - The `nltk` package is required for word handling.
   - Install it using:
     ```bash
     pip install nltk
     ```

4. Download the `words` dataset used by nltk:
   ```python
   import nltk
   nltk.download("words")
   ```

5. Ensure the following files are in the project directory:
   - `five_letter_german_nouns.txt`: Full list of 5-letter German nouns for guesses.
   - `solution_words.txt`: Curated list of 5-letter German nouns for target words.

6. (Optional) If you need to generate a new `solution_words.txt` file, run:
   ```bash
   python generate_solution_words.py
   ```

## Usage
1. Run the game using Python:
   ```bash
   python wordle_game.py
   ```

2. Type a 5-letter German word (noun) using your keyboard.
3. Press **Enter** to submit the word.
4. Use **Backspace** to delete letters.

## Game Rules
- Enter a valid 5-letter German noun from the full list (`five_letter_german_nouns.txt`).
- If the guess matches the target word (from `solution_words.txt`), the game will display a congratulatory message.
- If the word is incorrect, color feedback will indicate letter positions.
- Players have six attempts to guess the word correctly.

## Customization
### Using a Different Guess Word List
1. Replace `five_letter_german_nouns.txt` with your own list of 5-letter German nouns.
2. Ensure each word is unique and begins with a capital letter.

### Creating a Custom Solution Word List
1. Edit or regenerate `solution_words.txt` using the provided `generate_solution_words.py` script.
2. This script filters nouns based on frequency and excludes words with umlauts or dots.

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI framework for Python.
- **NLTK**: Natural Language Toolkit for word list handling.


Happy playing and viel Spaß!