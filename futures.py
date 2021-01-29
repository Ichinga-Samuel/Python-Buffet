import concurrent.futures as cf


def add(a, b):
    return a + b


def r_factorize(n):
    stop = round(n / 2) + 1
    result = []
    for i in range(1, stop):
        if n % i == 0:
            result.append(i)
    return result


exec = cf.ThreadPoolExecutor(10)

values = [25535, 4544, 543, 43586, 92312, 7342, 4434, 546347]
result = exec.map(r_factorize, values, timeout=3)  # result is a generator object
for i in result:
    print(i)

t = exec.submit(add, 4, 5)
t.result()
