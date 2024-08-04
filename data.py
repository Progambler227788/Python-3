import sys

# Read command line parameters
# key_file = sys.argv[1]
# plaintext_file = sys.argv[2]
key_file = "k1.txt"
plaintext_file = "p1.txt"

# Function to read the encryption key file
def read_key_file(key_file):
    with open(key_file, 'r') as f:
        # Read the key size
        key_size = int(f.readline().strip())
        # Read the key matrix
        key_matrix = []
        for _ in range(key_size):
            row = list(map(int, f.readline().strip().split()))
            key_matrix.append(row)
    return key_matrix

# Function to read the plaintext file
def read_plaintext_file(plaintext_file):
    with open(plaintext_file, 'r') as f:
        plaintext = f.read().lower()
    # Filter out non-alphabetic characters
    plaintext = ''.join(filter(str.isalpha, plaintext))
    return plaintext

# Function to pad plaintext if necessary
def pad_plaintext(plaintext, key_size):
    padding_length = key_size - (len(plaintext) % key_size)
    if padding_length != key_size:
        plaintext += 'x' * padding_length
    return plaintext

# Function to perform matrix multiplication

def matrix_multiply(plaintext_matrix, key_matrix):
    ciphertext = ''
    key_size = len(key_matrix)
    for i in range(0, len(plaintext_matrix), key_size):
        # Extract a block of plaintext characters
        block = plaintext_matrix[i:i+key_size]
        # Convert characters to numerical values
        block_values = [ord(char) - ord('a') for char in block]
        # Perform matrix multiplication
        for j in range(key_size):
            value = sum([block_values[k] * key_matrix[j][k] for k in range(key_size)]) % 26
            # Convert value back to a lowercase letter
            ciphertext += chr(value + ord('a'))
    return ciphertext

# Function to output to console
def output_to_console(key_matrix, plaintext, ciphertext):
    print("Key matrix:")
    for row in key_matrix:
        print(' '.join(map(str, row)))
    print("\nPlaintext:")
    print(plaintext)
    print("\nCiphertext:")
    # Print ciphertext in rows of 80 characters per line
    for i in range(0, len(ciphertext), 80):
        print(ciphertext[i:i+80])

# Main function
def main():
    # Read key file
    key_matrix = read_key_file(key_file)
    
    # Read plaintext file
    plaintext = read_plaintext_file(plaintext_file)
    
    # Pad plaintext if necessary
    padded_plaintext = pad_plaintext(plaintext, len(key_matrix))
    
    # Perform matrix multiplication
    ciphertext = matrix_multiply(padded_plaintext, key_matrix)
    
    # Output to console
    output_to_console(key_matrix, plaintext, ciphertext)

if __name__ == "__main__":
    main()
