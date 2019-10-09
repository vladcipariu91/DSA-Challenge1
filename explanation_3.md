# HUFFMAN CODING

## Data Structures
    To build the Huffman tree I used a Priority Queue which uses a MinHeap behind the scenes.
    The reason I used a MinHead is beacause it will contain the character with the lowest
    frequency as the first element.
    
    Creating the Huffman tree requires creating a map of each character and it's number of
    occurrences. Then using this map I create the priority queue and finally use the priority 
    queue to generate the tree. After the tree is created I generate another map where I store
    the character and it's Huffman code.
    
## Time complexity
    Priority Queue using a MinHeap:
        Insertion: O(log(n))
        Deletion: O(log(n))
        
        Every time an element is inserted or deleted we need to heapify the MinHeap, meaning
        we have to make sure the newly inserted element is in the right position. If it's smaller
        than it's parent we need to move it up until it's no longer smaller than the parent.
        
    Building the Huffman tree using the Priority Queue:
        This requires a time complexity of O(nlog(n)) because we need to pop the priority queue
        n times, where n is the is the number of elements in the queue. When the Queue is empty
        the tree is built.
        
    Encoding:
        Requires O(n) because we need to iterate over the input string and get the code from the tree.
        Getting the code requires O(1) because the codes are stored in a map.
        
    Decoding:
        Requires O(n * k) where n is the number of characters in the encoded strings and k is the
        value of the longest path from the root to a leaf node.
 

## Space complexity
    Because we store the codes we use a map which has a space complexity of O(n), where n is the 
    number of unique characters.
    
    Storing the characters in the tree is O(n) where n is the number of unique characters
    plus the extra nodes created to be able to generate unique codes.
    
    

