import sys


def calculate_hypotenuse(a, b):
    """
    This function calculates the hypotenuse of a right triangle.

    Args:
        a: The length of one leg of the triangle.
        b: The length of the other leg of the triangle.

    Returns:
        The length of the hypotenuse of the triangle.
    """
    #   Apply Pythagorean theorem to find the hypotenuse (c)
    c = (a * a + b * b)  # power with exponent 0.5
    return c


# Extract Slices method
def extract_slices(s, a, b, c, d):
    first_slice = s[a:b + 1]
    second_slice = s[c:d + 1]
    return first_slice + " " + second_slice


def count_nucleotides(dna_string):
    """
    This function counts the occurrences of A, C, G, and T in a DNA string.

    Args:
        dna_string: The DNA string to analyze.

    Returns:
        A string containing the counts of A, C, G, and T separated by spaces.
    """
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for char in dna_string:
        if char == 'A':
            a_count += 1
        elif char == 'C':
            c_count += 1
        elif char == 'G':
            g_count += 1
        elif char == 'T':
            t_count += 1

    return f"{a_count} {c_count} {g_count} {t_count}"


def transcribe_dna_to_rna(dna_string):
    """
    This function transcribes a DNA string into its corresponding RNA string.

    Args:
        dna_string: The DNA string to transcribe.

    Returns:
        The transcribed RNA string.
    """
    rna_string = ""
    for char in dna_string:
        if char == 'T':
            rna_string += 'U'
        else:
            rna_string += char
    return rna_string


def sum_of_odd_integers(a, b):
    """
    This function calculates the sum of odd integers from a to b (inclusive).

    Args:
        a: Starting integer (inclusive).
        b: Ending integer (inclusive).

    Returns:
        The sum of all odd integers in the range a to b.
    """
    sum = 0
    # Ensure a is odd (if even, add 1 to make it the first odd number)
    if a % 2 == 0:
        a += 1
    # Iterate by 2 to consider only odd numbers
    for num in range(a, b + 1, 2):
        sum += num
    return sum


def count_word_occurrences(text):
    """
    This function counts the occurrences of each word in a string.

    Args:
        text: The string containing words separated by spaces.

    Returns:
        A dictionary containing word counts.
    """
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def main():
    """
    Reads input from a list of lists, calls functions for each problem,
    and writes results to another file.
    """
    if len(sys.argv) != 3:
        print("Usage: python assignment1.py <input_file> <output_file>")
        sys.exit(1)
    # Get input and output file names from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # Try to open the input file and handle the case where it's not found
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    # Handle exceptions in case of any error
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Intialize variable i
        i = 0
        while i < len(lines):
            if lines[i].startswith("##"):  # If it's a problem description
                problem = lines[i].strip()
                if i + 1 < len(lines):  # Ensure we're not at the end of the file
                    data = lines[i + 1].strip()
                    # Handle problem respectively to functions
                    if problem == '##INI2':
                        a, b = map(int, data.split('\t'))
                        result = calculate_hypotenuse(a, b)
                        f.write(f"##INI2\n{result}\n")
                    elif problem == '##INI3':
                        data_list = data.split()  # Split data by whitespace
                        dna_string = data_list[0]
                        result = extract_slices(dna_string, int(data_list[1]), int(data_list[2]), int(data_list[3]),
                                                int(data_list[4]))
                        f.write(f"##INI3\n{result}\n")
                    elif problem == '##RNA':
                        dna_string = data
                        result = transcribe_dna_to_rna(dna_string)
                        f.write(f"##RNA\n{result}\n")
                    elif problem == '##DNA':
                        print(data + ' DNA\n\n')
                        result = count_nucleotides(data)
                        f.write(f"##DNA\n{result}\n")
                    elif problem == '##INI4':
                        data_list = data.split('\t')
                        print(data_list)
                        result = sum_of_odd_integers(int(data_list[0]), int(data_list[1]))
                        f.write(f"##INI4\n{result}\n")
                    elif problem == '##INI6':
                        result = count_word_occurrences(data)
                        f.write(f"##INI6\n{result}\n")
                    else:
                        print(f"Warning: Unknown problem type: {problem}")

                    i += 2  # Move to the next problem
                else:
                    i += 1  # Move to the next line if no data found
            else:
                i += 1  # Move to the next line if not a problem description


if __name__ == "__main__":
    main()
