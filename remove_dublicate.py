def remove_duplicates(s):
    seen = list()

    for char in s:
        if char not in seen:
            seen.append(char)
            print(seen)
    final_string = "".join(seen)

    print(final_string)

print(remove_duplicates("programming"))
