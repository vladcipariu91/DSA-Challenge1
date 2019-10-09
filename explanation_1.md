# LRU CACHE

## Data Structures
    To implement the LRU Cache I used a dictionary and a doubly linked list.
    These data structures, although increases the space complexity allows to
    manage the least recently used item and makes for finding an item really fast.
    
    The doubly linked list always keeps the least recently used item in it's tail and
    the most recently used item in it's head
    
    The map is used to find the node quickly and then using the doubly linked list we 
    can swap the current node with the head of the list (most recently used)

## Time complexity

    Insertion: O(1) we always insert at the head of the doubly linked list and also in the map
    Deletion: O(1) we just remove the tail of the doubly linked list
    Search: O(1) we use the map to find the item or return -1 if it's not found

## Space complexity 

    This is O(n). Although the list holds the items once and then the map as well.