import bisect


def bisection_search(a, e, low, high):
    if low >= high:
        return 'not found'
    else:
        m = round((low + high)/2)
        if a[m] == e:
            return m
        elif a[m] > e:
            high = m - 1
            return bisection_search(a, e, low, high)
        elif a[m] < e:
            low = m + 1
            return bisection_search(a, e, low, high)