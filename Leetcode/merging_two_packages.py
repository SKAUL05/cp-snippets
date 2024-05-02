"""Given a package with a weight limit limit and an array arr of item weights, implement a function
getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should
return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist,
return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
"""


def get_indices_of_item_wights(arr, limit):
    """
    Get the indices of two item weights in an array that add up to a specific limit.

    Args:
        arr (List[int]): A list of integers representing the item weights.
        limit (int): The target sum of two item weights.

    Returns:
        List[int]: A list containing the indices of the two item weights that add up to the limit, or an empty list if no such pair exists.
    """
    counter = {}
    for index, weight in enumerate(arr):
        complement = limit - weight
        if complement in counter:
            return [index, counter[complement]]
        else:
            counter[weight] = index
    return []


print(get_indices_of_item_wights([4, 6, 10, 15, 16], 21))
print(get_indices_of_item_wights([4, 4, 1], 5))
