def is_palindrome(word: str) -> bool:
    """from https://stackoverflow.com/a/39829879"""
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
