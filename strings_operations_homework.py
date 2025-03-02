import string
import re

homework_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

#Normalize the text to lowercase and replace " iz " with " is "
normalized_text = homework_text.lower().replace(" iz ", " is ")

# Using regex to split after '.', '!', or '?' followed by whitespace
splited_text = re.split(r'(?<=[.!?])\s+', normalized_text.strip())

#Extract the last word of each sentence
last_words = [sentence.rstrip(string.punctuation).split()[-1].rstrip(string.punctuation) for sentence in splited_text]
last_sentence = " ".join(last_words)

#Capitalize the first letter of each sentence
splited_text = [sentence.capitalize() for sentence in splited_text]

#Append the new sentence made from the last words to the list of sentences
splited_text.append(last_sentence.capitalize())

#Combine all sentences into a final formatted text with paragraph spacing
final_text = '\n\n\t'.join(splited_text)

#Count all whitespace characters (spaces, tabs, newlines, etc.) in the original text
count_whitespaces = sum(1 for char in homework_text if char.isspace())

print("Normalized text:")
print(final_text)

print(f'\nNumber of whitespaces in homework_text: {count_whitespaces}')
