import pandas as pd

def create_solution_words(input_file, output_file):
    # Load the frequency file
    try:
        frequency_data = pd.read_csv(input_file, sep='\t', encoding='utf-8', header=None)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Ensure column 0 (words) is treated as strings
    frequency_data[0] = frequency_data[0].astype(str)

    # Filter for nouns (POS == 'NN') with exactly 5 letters, no umlauts, and no dots
    filtered_data = frequency_data[
        (frequency_data[2] == 'NN') &
        (frequency_data[0].str.len() == 5) &
        (~frequency_data[0].str.contains('[äöüÄÖÜ.]', regex=True))  # Exclude umlauts and dots
    ].copy()

    # Sort by frequency (column 3) in descending order and select the top 2000
    filtered_data = filtered_data.sort_values(by=3, ascending=False).head(2000)

    # Extract the 'Word' column (column 0) and save to the output file
    filtered_data[0].to_csv(output_file, index=False, header=False, encoding='utf-8')
    print(f"File '{output_file}' created successfully with the top 2000 words.")

if __name__ == "__main__":
    # Define input and output file paths
    input_file = "DeReKo-2014-II-MainArchive-STT.100000.freq"  # Adjust path if needed
    output_file = "solution_words.txt"

    # Create the solution words file
    create_solution_words(input_file, output_file)
