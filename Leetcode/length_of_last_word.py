def length_of_last_word(string: str) -> int:
    ans = string.split()
    return len(ans[-1])


if __name__ == "__main__":
    print(length_of_last_word("SKAUL 05"))
