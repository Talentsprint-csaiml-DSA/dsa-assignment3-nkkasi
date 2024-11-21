import heapq
from collections import Counter

def huffman_coding(input_string):
    # Count frequency of each character in the input string
    freq_tab = dict(Counter(input_string))
    huff_tree = [[freq, [char,""]] for char, freq in freq_tab.items()]

    # Build a Huffman Tree based on the character encodings
    heapq.heapify(huff_tree)
    
    while len(huff_tree) > 1:
        # pull out the lowest two nodes
        low1 = heapq.heappop(huff_tree)
        low2 = heapq.heappop(huff_tree)
    
        # Append the 0 code for the left and right branches
        for pair in low1[1:]:
            pair[1] = "0" + pair[1]

        for pair in low2[1:]:
            pair[1] = "1" + pair[1]

        accrued_val = low1[0] + low2[0]
        heapq.heappush(huff_tree, [accrued_val] + low1[1:] + low2[1:])
    
# Generate Binary codes for the Character tree
    huff_tree = huff_tree[0][1:]

# Encode the input string
    huff_codes = {char:code for char, code in huff_tree}
    encoded_string = "".join(huff_codes[char] for char in input_string)
    return encoded_string
    
# encoded_string = huffman_coding('hello')
# print(encoded_string)