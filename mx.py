from sympy import Matrix


def mx(s):
    M = s.split("\n")
    for i, r in enumerate(M):
        M[i] = r.split(" ")
        for l in M[i]:
            if l == '':
                M[i].remove(l)

    for l in M:
        if l == []:
            M.remove(l)
    return Matrix(M)
