# PROBLEM 6
## Union and Intersection of Two Linked Lists
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.
<br>
### In this problem I have used-
1. Dictionary: To store all unique elements and common elements in two link list
2. LinkList: For which we need to find union and intersection.


### Algorithm:
1. Union:
  • Create an empty dictionary<br>
  • For all elements in both the list if it does not exist in dictionary then add it to dictionary<br>
  and if elements already present in dictionary then skip that element.<br>
  • Dictionary is used over here because it has O(1) complexity to check if any element is
  present in dictionary it takes O(1) complexity.<br>
  • Finally create a link list with the elements of dictionary.<br>
2. Intersection:<br>
  • Create two empty dictionary one for unique elements of list 1 and other for common
  elements of both the list<br>
  • For all elements in list 1 if it does not exist in dictionary then add it to dictionary 1 and if
  elements already present in dictionary 1 then skip that element.<br>
3. For all elements in list 2 if exist in dictionary 1 (i.e my list 1) and does not exist in
dictionary 2 (common elements) then add the element to common elements dictionary.
4. Dictionary is used over here because it has O(1) complexity to check if any element is
present in dictionary it takes O(1) complexity.
5. Finally create a link list with the dictionary of common elements.


### Time Complexity Analysis:
  • Union: O(n) where n= size of list 1 +size of list 2<br>
  • Intersection: O(n) where n=size of list 1 +size of list 2<br>


### Space Complexity Analysis:
  • Space to store dictionary 1: O(no. of unique elements in both list)<br>
  • Space to store dictionary 2: O(no. of common elements in both list)<br>
