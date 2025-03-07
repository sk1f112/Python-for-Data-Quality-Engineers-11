import re
import string


#Normalize the text to lowercase and replace " iz " with " is "
def normalize_text(text):
    return text.lower().replace(" iz ", " is ")

# Using regex to split after '.', '!', or '?' followed by whitespace
def split_into_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

#Extract the last word of each sentence
def extract_last_words(sentences):
    return [s.rstrip(string.punctuation).split()[-1].rstrip(string.punctuation) for s in sentences]

#Capitalize the first letter of each sentence
def capitalize_sentences(sentences):
    return [s.capitalize() for s in sentences]

#Join all sentences
def join_sentences_with_spacing(sentences):
    return '\n\n\t'.join(sentences)

#Count all whitespace characters (spaces, tabs, newlines, etc.) in the original text
def count_whitespaces(text):
    return sum(1 for char in text if char.isspace())

#The process step by step om homework string using decomposition
def process_string_homework(input_text):
    normalized = normalize_text(input_text)
    sentences = split_into_sentences(normalized)

    last_words_sentence = " ".join(extract_last_words(sentences))
    sentences = capitalize_sentences(sentences)
    sentences.append(last_words_sentence)

    final_text = join_sentences_with_spacing(sentences)
    whitespace_count = count_whitespaces(input_text)

    print("Normalized text:")
    print(final_text)

    print(f'\nNumber of whitespaces in original text: {whitespace_count}')

    return final_text, whitespace_count
