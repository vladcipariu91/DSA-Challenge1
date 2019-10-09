# UNION AND INTERSECTION USING LINKED LISTS

## Data Structures
    In order to optimise the search I used binary trees. Search in a 
    binary tree requires O(log(n)).  
    The lists also contain duplicates and the binary tree helps in
    solving the problem of removing them. If a node with the value
    already exists it's discarded.
    
## Time complexity
    Intersection:
    
    To implement the intersection I build a tree out of the biggest
    linked list. This requires O(n) where n is the number of nodes in
    the biggest list.
    
    For each node in the smaller list I do a search in the tree.
    A search is O(log(n)), since I'm doing this for every node
    the complexity is O(nlog(n)).
    
    The result is stored in another tree since the smaller list may
    also contain duplicates, creating the second tree is O(nlog(n))
    
    Union:
    
    I only create one tree which has a complexity of O(nlog(n))
    Then convert this back into a linked list which is also O(nlog(n)).
    The overall complexity is O(nlog(n)).
    n is the combined number of nodes from linked lists 1 and 2.

## Space complexity
    Ignoring the input this uses two binary trees.
    
    Intersection:
         
    The overall complexity is O(n) since two binary trees are used.
        
    Union:
    
    The overall complexity is also O(n). Only one tree is used that
    contains the unique elements of both lists.
    