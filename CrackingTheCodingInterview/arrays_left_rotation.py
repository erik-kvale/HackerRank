"""
------------------
Problem Statement
------------------
    A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. FOr example,
    if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. Given an array of n
    integers and a number, d, perform d left rotations on the array. Then print the updated array as a single line of
    space-separated integers.

------------------
Input Format:
------------------
    The first line contains two space-separated integers denoting the respective values of n (the number of integers)
    and d (the number of left rotations you must perform). The second line contains n space-separated integers
    describing the respective elements of the array's initial state.

------------------
Constraints
------------------
    1 <= n <= 10^5
    1 <= d <= n
    1 <= a(sub i) <= 10^6

------------------
Output Format
------------------
    Print a single line of n space-separated integers denoting the final state of the after performing d left rotations.


============================
Solution Statement
============================
After reading in the necessary inputs, we need to simulate a left rotation on the array (Python list). For each rotation
'd' we need to pop off the first element of the array and append it at the last-index position of the array, this
will simulate a left or counter-clockwise rotation. Visualizing the array as circle with its elements on the face of a
clock can be helpful. When I pop off the first element (index=0), I store that value. My array is now length n - first
element at which point I append the popped element to the end, effectively causing each element to shift one index
to the left from its initial state.

"""


def array_left_rotation(num_of_elements, elements, num_of_rotations):
    for rotation in range(num_of_rotations):    # O(n)
        first_element = elements.pop(0)         # O(1)
        elements.append(first_element)          # O(1)
    return elements                             # O(1)


n, d = map(int, input().strip().split())        # O(1)
a = list(map(int, input().strip().split()))     # O(n)
answer = array_left_rotation(n, a, d)           # O(n) = O(n) + O(1) + O(1) + O(1)
print(*answer, sep=' ')                         # O(1)

# The algorithm











