def is_unique(s):
    seen = list()

    for char in s:
        if char not in seen:
            seen.append(char)
    final_string = "".join(seen)
    print(s == final_string)

is_unique("abcdef")  # True
is_unique("hello")  # False