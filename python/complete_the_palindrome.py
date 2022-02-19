from modules.palindrome import is_palindrome


def complete_the_palindrome_from_right(word: str) -> (int, str):
    """Determine the minimum number of chars to add to the right
    of the word to make it a palindrome.
    returns (number of chars to add, the_palindrome)
    """
    if is_palindrome(word):
        return (0, word)
    for i in range(1, len(word) - 1):
        if is_palindrome(word[i:]):
            return (i, word + word[i - 1 :: -1])
    return (len(word) - 1, word + word[-2::-1])


def complete_the_palindrome(word: str) -> (int, str):
    """Determine the minimum number of chars to add at any point
    of the word to make it a palindrome.
    returns (number of chars to add, the_palindrome)
    """
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            chunk = word[i:-i] if i > 0 else word
            n, m = complete_the_palindrome_from_right(chunk)

            l = len(chunk)
            for j in range(l - 1, l - n, -1):
                if is_palindrome(chunk[:j]):
                    n, m = (l - j, chunk[j:][::-1] + chunk)

            s = word[:i]
            return (n, s + m + s[::-1])
    return (0, word)


while True:
    print(complete_the_palindrome(input()))
