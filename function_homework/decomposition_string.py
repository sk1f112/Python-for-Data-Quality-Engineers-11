import re
import string
from typing import List, Tuple

def normalize_text(text: str) -> str:
    """Normalize the text by converting to lowercase and replacing ' iz ' with ' is '."""
    return text.lower().replace(" iz ", " is ")

def split_into_sentences(text: str) -> List[str]:
    """Split text into sentences based on punctuation."""
    return re.split(r'(?<=[.!?])\s+', text.strip())

def extract_last_words(sentences: List[str]) -> List[str]:
    """Extract the last word from each sentence."""
    return [s.rstrip(string.punctuation).split()[-1] for s in sentences]

def capitalize_sentences(sentences: List[str]) -> List[str]:
    """Capitalize the first letter of each sentence."""
    return [s.capitalize() for s in sentences]

def join_sentences_with_spacing(sentences: List[str]) -> str:
    """Join sentences with double newline and tab spacing."""
    return '\n\n\t'.join(sentences)

def count_whitespaces(text: str) -> int:
    """Count all whitespace characters in a text."""
    return sum(1 for char in text if char.isspace())

def process_string_homework(input_text: str) -> Tuple[str, int]:
    """Process text with normalization, sentence extraction, and whitespace counting."""
    normalized: str = normalize_text(input_text)
    sentences: List[str] = split_into_sentences(normalized)

    last_words_sentence: str = " ".join(extract_last_words(sentences))
    sentences = capitalize_sentences(sentences)
    sentences.append(last_words_sentence)

    final_text: str = join_sentences_with_spacing(sentences)
    whitespace_count: int = count_whitespaces(input_text)

    print("Normalized text:")
    print(final_text)
    print(f'\nNumber of whitespaces in original text: {whitespace_count}')

    return final_text, whitespace_count
