import itertools as it


def checksolution(perm, n):
    c = list(range(n))
    sol = [(i, j) for i, j in zip(perm, c)]
    a = sol[:]

    for i in a:
        for j in a:
            if i == j:
                continue

            elif abs(i[0] - j[0]) == abs(i[1] - j[1]):
                return False

    else:
        return True


def perms(n):
    row = list(range(n))
    solutions = []
    sol = it.permutations(row)

    for i in sol:
        s = next(sol)
        if checksolution(s, n):
            solutions.append(s)

    return solutions, len(solutions)


print(perms(8))