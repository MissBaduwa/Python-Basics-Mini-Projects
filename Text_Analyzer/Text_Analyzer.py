# ===============================
# Text Analyzer - Covers Week 1 Python concepts
# ===============================


#Goal: Practice Python basics (variables, conditionals, dictionaries,
# loops, functions, modules, file handling, exception handling, and classes).


# --------- Imports ----------
import string                     # For punctuation removal


# --------- TextAnalyzer Class ---------
class TextAnalyzer:

    # Initialize the TextAnalyzer object
    def __init__(self, text=""):
        self.text = text          # Store the text input as an instance variable
        self.words = []           # List to store individual words after processing

    # Let user choose how to provide input: manually or via a file.
    def read_input(self):
        print("Welcome to Text Analyzer!")

        print("Choose input method:")

        print("1. Enter text manually")

        print("2. Read text from a file")

        choice = input("> ")                      # Take user input to choose method

        if choice == "1":
            self.text = input("Enter your text:\n> ")

        elif choice == "2":
            filename = input("Enter file name (with extension):\n> ")

            try:
                # Try opening and reading the file
                with open(filename, "r", encoding="utf-8") as f:
                    self.text = f.read()     # Store file contents in self.text

            except FileNotFoundError:
                # Handle error if file does not exist
                print(f"Error: File '{filename}' not found. Exiting program.")
                exit()                       # Exit the program gracefully

        else:
            # Handle invalid choice input
            print("Invalid choice. Exiting program.")
            exit()                           # Exit the program gracefully


    # Preprocess text (lowercasing, splitting, removing punct)
    def clean_text(self):
        text_lower = self.text.lower()      # Convert all letters to lowercase

        # Remove punctuation using str.translate() and string.punctuation
        text_no_punct = text_lower.translate(str.maketrans("", "", string.punctuation))

        self.words = text_no_punct.split()   # Split the cleaned text into a list of words


    # Calculate total number of words in the text
    def total_words(self):
        return len(self.words)               # Return the length of the words list


    # Calculate number of unique words
    def unique_words(self):
        return len(set(self.words))          # Convert list to set (removes duplicates) and count


    # Find the most common word in the text and its frequency
    def most_common_word(self):
        word_counts = {}                     # Create an empty dictionary to store word counts

        # Loop through each word in the words list
        for word in self.words:
            if word in word_counts:
                word_counts[word] += 1        # Increment count if word already exists
            else:
                word_counts[word] = 1         # Initialize count if word is new

        # Find the word with the maximum count using max() with key
        most_common = max(word_counts, key=word_counts.get)
        return most_common, word_counts[most_common]  # Return word and count

    # Run full analysis ( clean, calculate total words, calculate unique words, etc.)
    def analyze(self):

        self.clean_text()                                    # First, clean and preprocess the text
        total = self.total_words()                           # Get total number of words
        unique = self.unique_words()                         # Get number of unique words
        common_word, common_count = self.most_common_word()  # Get most common word and frequency

        # Print results in a readable format
        print("\n--- Text Analysis Results ---")
        print(f"Total words: {total}")
        print(f"Unique words: {unique}")
        print(f"Most common word: '{common_word}' ({common_count} times)")
        print("------------------------------")


# ===============================
# Main program execution
# ===============================

# Check if this script is run directly (not imported)
if __name__ == "__main__":
    analyzer = TextAnalyzer()  # Create an instance of TextAnalyzer
    analyzer.read_input()      # Prompt user for text input
    analyzer.analyze()         # Perform analysis and print results