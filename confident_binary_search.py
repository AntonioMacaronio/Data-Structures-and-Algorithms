# This is based of Tyler Hou's Blog: https://blog.tylerhou.io/posts/binary-search-with-confidence/#user-content-fnref-2
def binary_search(array, is_green):
    """
    Computes the index in which if is_green's number is inserted, the array remains sorted
    If there are multiple places to insert the number, we will insert at the beginning of the pack.
    
    Input: 
        1. array - sorted array
        2. is_green - boolean function for green area (values less than what we're searching for)
        Red refers to values greater than or equal to the number we are searching for.
    Output: 
        1. Index value in the range [0, len(array)] (inclusive endpoints)
    """
    left, right = 0, len(array) - 1
    if not array:
        return 0
    if not is_green(array[left]):
        return 0
    if is_green(array[right]):
        return len(array)
    # Main loop which narrows our search range.
    while right - left > 1:
        mid = (left + right) // 2
        if is_green(array[mid]):
            left = mid
        else:
            right = mid
    return right

print(binary_search([0,2,3,6,6,6,9,10,20,58,60], lambda x: x < 6))