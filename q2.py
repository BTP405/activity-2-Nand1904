import matplotlib.pyplot as plt

def write_specific_entries(file_path, entries):
    """
    Writes a list of specific entries to a file.
    """
    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Loop through each entry in the list
        for entry in entries:
            # Convert the entry to a string and write it to the file
            file.write(str(entry) + '\n')

def graphSnowfall(file_path):
    """
    Reads data from a text file and displays a bar chart showing snowfall accumulation ranges.
    """
    # Initialize variables to store counts for each range
    # [0-10, 11-20, 21-30, 31-40, 41-50]
    ranges = [0] * 5  

    # Read data from the file and update range counts
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Convert the line (string) to an integer (snowfall value)
            snowfall = int(line.strip())
            
            # Check which range the snowfall falls into and update the counts
            if 0 <= snowfall <= 10:
                ranges[0] += 1
            elif 11 <= snowfall <= 20:
                ranges[1] += 1
            elif 21 <= snowfall <= 30:
                ranges[2] += 1
            elif 31 <= snowfall <= 40:
                ranges[3] += 1
            elif 41 <= snowfall <= 50:
                ranges[4] += 1

    # Plot the bar chart
    labels = ['0-10', '11-20', '21-30', '31-40', '41-50']
    plt.bar(labels, ranges, color='Yellow')
    plt.xlabel('Snowfall Accumulation Ranges (in cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Ranges')
    
    # Save the chart as an image file (PNG)
    plt.savefig('snowfall_chart.png')
    
    # Display the chart
    plt.show()

# Example usage:
# Example list of specific entries
specific_entries = [10, 15, 45, 5, 20, 25]

# File path to store the data
file_path = 'snowfall_data.txt'

# Write specific entries to the file
write_specific_entries(file_path, specific_entries)

# Plot the graph using the specific entries
graphSnowfall(file_path)
