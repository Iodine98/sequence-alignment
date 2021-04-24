import datetime


def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    numbers_map = dict()
    for i, num in enumerate(nums):
        if num in numbers_map:
            j = numbers_map[num]
            if abs(i - j) <= k:
                return True
        numbers_map[num] = i
    return False


a = datetime.datetime.now()
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
b = datetime.datetime.now()
c = b - a
print(c.total_seconds())
