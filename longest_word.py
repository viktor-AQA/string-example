def longest_word(s):
    s_new = s.replace(",", " ")
    print(s_new)
    new = s_new.split()
    print(new)

    max_lenth = 0
    longest_i = ""
    for i in new:
        if len(i) > max_lenth:
            max_lenth = len(i)
            longest_i = i
    print(longest_i)


longest_word("In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinary”