def verify_card_number(digits: str):

    reversed_digits = digits[::-1]
    clean_string = reversed_digits.replace("-", "").replace(" ", "")
    number_list = [int(x) for x in clean_string]
    count = 0
    for i, n in enumerate(number_list):
        if i % 2 == 1:
            number_list[i] = n * 2 if n * 2 < 9 else n * 2 - 9
        count += number_list[i]

    return "VALID!" if count % 10 == 0 else "INVALID!"
