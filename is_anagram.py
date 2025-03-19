def is_anagram(s1, s2):
    s1 = list(s1.lower())
    s2 = list(s2.lower())

    s1.sort()
    s2.sort()

    s1 = ''.join(s1)
    s2 = ''.join(s2)
    return s1 == s2

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
