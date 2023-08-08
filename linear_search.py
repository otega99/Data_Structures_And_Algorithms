def linear_search(list,target):
    """
    Returns the index of the position if found, else returns none
    """
    for i in range(0,len(list)):
        if list[i]==target:
            return i
    return None   



def verify(index):
    if index is not None:
        print(f'Target found at {index}')
    else:
        print("Target not found in list")


numbers=[i for i in range(1,11)]
result=linear_search(numbers,12)
verify(result)
result=linear_search(numbers,6)
verify(result)