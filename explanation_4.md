# ACTIVE DIRECTORY

## Data Structures
    I didn't use any data structures other than the provided ones.
    

## Time complexity
    In order to find a user we need to iterate over the list of 
    users of each group. Each group may have other subgroups so we need
    to go deeper and deeper.
    
    I only visit each element once so the time complexity is O(n * k)
    where n is the number of users and k is the number of groups.
    This is O(n) in total.
    

## Space complexity 
    
    This is O(1) since there's nothing stored to solve this problem.
    