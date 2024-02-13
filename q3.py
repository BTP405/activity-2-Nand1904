def wordCount(file_path):
    """
    Retrieves data from a text file and returns a dictionary with unique words and their line numbers.
    """
    word_dict = {}  # Dictionary to store unique words and their line numbers

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()  # Split the line into words

            for word in words:
                # If the word is not in the dictionary, add it with the current line number
                if word not in word_dict:
                    word_dict[word] = [line_number]
                else:
                    # If the word is already in the dictionary, append the current line number
                   '''append in python is a pre-defined method used to add a single item 
                    to certain collection types'''
                word_dict[word].append(line_number)

    return word_dict

# Example usage:
def create_sample_text(file_path):
    """
    Creates a sample text file with some content for testing.
    """
    content = """
    This is a sample text file.
    It contains some words, and each line has different words.
    The words can appear multiple times.
    """

    with open(file_path, 'w') as file:
        file.write(content)

# Example usage:
sample_file_path = 'sample_text.txt'
create_sample_text(sample_file_path)

# Call wordCount function with the created file
result = wordCount(sample_file_path)
print(result)
