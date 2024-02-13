# Define a decorator function to print statistics for a list of numbers
def statistics_decorator(func):
    """
    Decorator function to print statistics for a list of numbers.
    """
    # Wrapper function that adds printing functionality to the original function
    def wrapper(numbers):
        print("Numbers read:", numbers)  # Print the numbers
        print("Count of numbers:", len(numbers))  # Print the count of numbers

        if len(numbers) > 0:
            # If there are numbers, print the average and maximum
            print("Average of numbers:", sum(numbers) / len(numbers))
            print("Maximum of numbers:", max(numbers))
        else:
            # If no numbers were read, print a message
            print("No numbers were read.")

        print("-------------")  # Separate statistics for different lines

    return wrapper  # Return the decorated function

# Apply the decorator to an empty function (it will be replaced later)
@statistics_decorator
def process_line_of_numbers(numbers):
    """
    Function to process a line of numbers and apply the decorator.
    """
    pass  # The decorator is applied directly, so this function is empty

# Main function to read lines of numbers from a text file and apply the decorator
def printStats(file_path):
    """
    Reads lines of numbers from a text file and applies the decorator function to print statistics.
    """
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:  # Loop through each line in the file
            # Convert the line of numbers to a list of floats
            numbers = [float(num) for num in line.strip().split()]

            # Call the decorated function to print statistics
            process_line_of_numbers(numbers)

# Create a sample file with numbers
sample_file_path = 'numbers_data.txt'
sample_content = """
1 2 3 4 5
10 20 30
0.5 0.75 1.0
"""

with open(sample_file_path, 'w') as sample_file:
    sample_file.write(sample_content)

# Example usage:
printStats(sample_file_path)  # Call the main function to print statistics for each line
