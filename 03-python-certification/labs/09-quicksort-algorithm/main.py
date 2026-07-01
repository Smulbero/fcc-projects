def quick_sort(lst):
    if len(lst) == 0:
        return []

    pivot = lst[0]
    lesserList = [x for x in lst if x < pivot]
    pivotList = [x for x in lst if x == pivot]
    greaterList = [x for x in lst if x > pivot]

    return quick_sort(lesserList) + pivotList + quick_sort(greaterList)