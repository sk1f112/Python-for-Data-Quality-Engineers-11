import os
import csv

TEXT_FILE = "file_module_homework/news_feed_homework.txt"
WORD_COUNT_FILE = "word_count.csv"
LETTER_COUNT_FILE = "letter_count.csv"

def read_text_file():
    # Read all text from the file
    if not os.path.exists(TEXT_FILE):
        print(f"Error: {TEXT_FILE} not found.")
        return ""

    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        return file.read().strip()

def count_words(text):
    # Split sentence to words and count it
    word_counts = {}
    words = text.lower().split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def count_letters(text):
    # Count letters (upper_case, total, percentage)
    letter_counts = {}
    uppercase_counts = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1
            total_letters += 1

            if char.isupper():
                uppercase_counts[lower_char] = uppercase_counts.get(lower_char, 0) + 1

    # Prepare letter statistics
    letter_stats = []
    for letter in sorted(letter_counts):
        count_all = letter_counts[letter]
        count_upper = uppercase_counts.get(letter, 0)
        percentage = (count_all / total_letters) * 100 if total_letters > 0 else 0
        letter_stats.append((letter, count_all, count_upper, round(percentage, 2)))

    return letter_stats

def write_word_count(text):
    # Write words count to the CSV file
    word_counts = count_words(text)

    with open(WORD_COUNT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        writer.writerows(word_counts.items())

def write_letter_count(text):
    # Write letters count to the CSV file
    letter_data = count_letters(text)

    with open(LETTER_COUNT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])
        writer.writerows(letter_data)

def process_text_file():
    # Main function to work with CSV files (write, read)
    text = read_text_file()
    if not text:
        print("No text found to process.")
        return

    write_word_count(text)
    write_letter_count(text)
    print("CSV files have been updated.")

if __name__ == "__main__":
    process_text_file()
