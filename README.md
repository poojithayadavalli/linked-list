# problem statement # linked-list #sorting

Arya is fond of linked lists. He is given with a task as follows:

There are N number of similar boxes with different sizes such that the box with small size fits into the box with a size larger than it.He needs to arrange the boxes in such a 

way that any box except the large box can be opened only if all the boxes larger than it are opened.He thought linked list would be a great approach to solve this task.

Input: 
The input consists of different sizes of N boxes.

Output:
The output should be a linked list containing small box at head and large box at last

Note:

The sizes of the boxes must be positive and unique

Example 1

Input:

10 5 7 1 3 9

Output:

1->3->5->7->9->10

Example 2:

Input:

412

Output:

1->2->4

Example 3:

Input:

4 1 6

output:

1->4->6

