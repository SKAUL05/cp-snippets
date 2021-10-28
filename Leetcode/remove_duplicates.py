from typing import List


def remove_duplicates(nums: List[int]) -> int:
    ans = set(nums)
    nums[: len(ans)] = sorted(ans)
    return ans


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 3, 4, 5]))
