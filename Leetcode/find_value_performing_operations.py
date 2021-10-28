from typing import List

def final_value_after_operation(operations: List[str]) -> int:
    op = 0
    for operation in operations:
        if operation in ["--X", "X--"]:
            op -= 1
        else:
            op += 1
    return op

if __name__ == "__main__":
    print(final_value_after_operation(["X--","--X","--X"]))