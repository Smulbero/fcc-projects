def number_pattern(n):
    if not isinstance(n, int):
        return(f'Argument must be an integer value.')
    if n < 1:
        return(f'Argument must be an integer greater than 0.')

    return_str = ""
    for i in range(1, n + 1):
        return_str += str(i)
        if i != n:
            return_str += " "

    return return_str