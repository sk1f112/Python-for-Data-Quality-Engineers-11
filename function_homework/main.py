from decomposition_dict import process_dict_homework
from decomposition_string import process_string_homework

homework_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

if __name__ == "__main__":
    print("\nHomework dict:\n")
    process_dict_homework()

    print("\nHomework string:\n")
    process_string_homework(homework_text)
