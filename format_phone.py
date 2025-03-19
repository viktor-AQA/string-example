def format_phone_number(digits):

    first_code = digits[:3]
    second_part = digits[3:6]
    thread_part = digits[6:]

    print(f"({first_code}) {second_part}-{thread_part}")

format_phone_number("1234567890")  # "(123) 456-7890”