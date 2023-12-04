from HuffmanCode.huffman_decode import huffman_decode
from build_huffman import build_huffman_tree, generate_huffman_codes
from collections import defaultdict, Counter  # Import defaultdict and Counter for convenient data structures

# Function to encode data using Huffman codes
def huffman_encode(data):
    frequencies = Counter(data)  # Count the frequency of each symbol in the input data
    root = build_huffman_tree(frequencies)  # Build the Huffman tree
    codes = generate_huffman_codes(root)  # Generate Huffman codes from the tree

    encoded_data = "".join(codes[symbol] for symbol in data)  # Encode the input data using Huffman codes
    return encoded_data, root  # Return the encoded data and the Huffman tree root





## Example usage
input_array = ['A', 'B', 'A', 'C', 'B', 'A', 'A']
encoded_data, huffman_tree = huffman_encode(input_array)
decoded_data = huffman_decode(encoded_data, huffman_tree)

print("Original Data:", input_array)
print("Encoded Data:", encoded_data)
print("Decoded Data:", decoded_data)
