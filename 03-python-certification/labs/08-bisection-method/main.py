def square_root_bisection(n, tolerance = 0.1, iterations = 100):
    if n < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif n == 0 or n == 1:
        print(f'The square root of {n} is {n}')
        return n
    else:
        low = 0
        high = n if n > 1 else 1

        for _ in range(iterations):
            mid = (low + high) / 2
            mid_sqr = mid ** 2

            if abs(high - low) == 0 or abs(high - low) <= tolerance:
                print(f'The square root of {n} is approximately {mid}')
                return mid
            elif mid_sqr < n:
                low = mid
            else:
                high = mid            

    print(f'Failed to converge within {iterations} iterations')
    return None