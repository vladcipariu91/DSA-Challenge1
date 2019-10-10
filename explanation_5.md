# BLOCK CHAIN

## Data Structures
    To implement the blockchain I used a map and a linked list.
    The map is used to keep track of the elements by their hash and 
    helps retrieve a block. Otherwise this is just a simple linked list.
    In order to reference the previous block you just need to look it up
    in the map and move on like this until the Genesis block is reached. 
    

## Time complexity

    Insertion is O(1) because this uses a map.
    Finding a block is O(1) given we don't take into account the complexity
    required to calculate the hash function.

## Space complexity

    The space complexity for this problem is O(n) where n is the number
    of items we store in the map. The blockchain object has a map and a reference to it's head.
    