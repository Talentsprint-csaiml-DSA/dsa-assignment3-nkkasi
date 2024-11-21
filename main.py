class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def sort_queue(queue):
    # Helper function to maintain a sorted queue based on frequencies
    return sorted(queue, key=lambda node: node.freq)

def build_huffman_tree(frequency):
    queue = [Node(char, freq) for char, freq in frequency.items()]
    queue = sort_queue(queue)

    while len(queue) > 1:
        # Take the two nodes with the smallest frequency
        left = queue.pop(0)
        right = queue.pop(0)

        # Create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node to the queue
        queue.append(merged)
        queue = sort_queue(queue)

    return queue[0]  # Root of the tree

def generate_codes(root, current_code, codes):
    if root is None:
        return

    # If a leaf node is reached, assign its code
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse left and right
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

def huffman_coding(sentence):
    # Step 1: Count frequency of each character
    frequency = {}
    for char in sentence:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Build the Huffman tree
    root = build_huffman_tree(frequency)

    # Step 3: Generate binary codes
    codes = {}
    generate_codes(root, "", codes)

    # Step 4: Encode the input string
    encoded_string = "".join(codes[char] for char in sentence)

    return encoded_string, codes
