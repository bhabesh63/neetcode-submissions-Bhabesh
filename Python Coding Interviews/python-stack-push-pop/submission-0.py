from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack=[]
    for elm in arr:
        stack.append(elm)
    reversedarr=[]
    while len(stack)>0:
        reversedarr.append(stack.pop())
    return reversedarr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
