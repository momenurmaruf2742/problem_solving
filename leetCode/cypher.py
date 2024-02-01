"""
Consider the plaintext “THE SIMPLEST POSSIBLE TRANSPOSITIONS”,
find out the corresponding Transposition Cipher (Take width as input). 
Then perform the reverse operation to get original plaintext. 
Example: Input: THE SIMPLEST POSSIBLE TRANSPOSITIONS

Output: Key 41532
Cypher Text: STIEH EMSLP STSOP EITLB SRPNA TOIIS XOXSN
"""
# 4 2 1 5 3          1 2 3 4 5 
# S H T I E          T H E S I 
# E P M S L          M P L E S 
# S P T S O          T P O S S 
# E B I T L          I B L E T 
# S A R P N          R A N S P 
# T S O I I          O S I T I 
# X N O X S          O N S X X 


def transposition_cipher(plaintext, key):
    key_str = str(key)

    # Create a matrix based on the given key
    matrix = [list(plaintext[i:i + len(key_str)]) for i in range(0, len(plaintext), len(key_str))]

    # Arrange columns based on the given key and replace empty positions with 'X'
    arranged_matrix = [
        [matrix[row][int(k) - 1] if int(k) - 1 < len(matrix[row]) else 'X' for k in key_str]
        for row in range(len(matrix))
    ]

    # Read the rows to get the ciphered text
    cyphertext = ' '.join([''.join(row) for row in arranged_matrix])

    return cyphertext

# Example usage
plaintext = "THE SIMPLEST POSSIBLE TRANSPOSITIONS"
key = 41532

# Encrypt (Transposition Cipher)
cyphertext = transposition_cipher(plaintext.replace(" ", ""), key)
print("Key:", key)
print(f"Cypher Text: {cyphertext}")





