import os
import csv
from collections import Counter

TEXT_FILE = "file_module_homework/news_feed_homework.txt"
WORD_COUNT_FILE = "word_count.csv"
LETTER_COUNT_FILE = "letter_count.csv"

def read_text_file():
    #Read all text from the file
    if not os.path.exists(TEXT_FILE):
        print(f"Error: {TEXT_FILE} not found.")
        return ""

    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        return file.read().strip()

def count_words(text):
    #Split sentence to words and count it
    words = text.lower().split()
    return Counter(words)

def count_letters(text):
    #Count letters (upper_case, total, percentage)
    letters_only = [char for char in text if char.isalpha()]
    total_letters = Counter(letters_only)

    uppercase_count = sum(1 for char in text if char.isupper())
    total_count = sum(total_letters.values())

    letter_stats = []
    for letter, count in sorted(total_letters.items()):
        percentage = (count / total_count) * 100 if total_count else 0
        letter_stats.append((letter, count, uppercase_count, round(percentage, 2)))

    return letter_stats

def write_word_count(text):
    #Write words count to the CSV file
    word_counts = count_words(text)

    with open(WORD_COUNT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        writer.writerows(word_counts.items())

def write_letter_count(text):
    #Write letters count to the CSV file
    letter_data = count_letters(text)

    with open(LETTER_COUNT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])
        writer.writerows(letter_data)

def process_text_file():
    #Main function to work with CSV files(write, read)
    text = read_text_file()
    if not text:
        print("No text found to process.")
        return

    write_word_count(text)
    write_letter_count(text)
    print("CSV files have been updated.")

if __name__ == "__main__":
    process_text_file()
