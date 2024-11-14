# Filter and save 5-letter German words that start with a capital letter
def filter_five_letter_capital_words(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        words = [
            line.strip()
            for line in file
            if len(line.strip()) == 5 and line.strip()[0].isupper()
        ]

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(words))

    print(f"Filtered words saved to {output_file}")


# Usage
input_file = "german_words.txt"  # Original file with all German words
output_file = "five_letter_german_nouns.txt"  # Filtered file
filter_five_letter_capital_words(input_file, output_file)