def is_palindrome(s):
    s = list(s.lower())
    s = "".join(s)
    s_new = s.replace(",", " ")
    s_new2 = s_new.replace(":", " ")
    joined_text = "".join(s_new2.split())
    reversed_text = joined_text[::-1]
    print(reversed_text == joined_text)



is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("racecar")                         # True
is_palindrome("hello")                           # False