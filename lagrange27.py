# -*- coding: utf-8 -*-
from sympy import *
from IPython.display import display
syms = "xtuvfghprs"


def replacement(M):
    n = M.rows
    C = eye(n)
    for i in xrange(n):
        if M[i, i] != 0 and sum(M[i, :]) != M[i, i]:
            C[:, i] = Matrix([M[i, j]/M[i, i] for j in xrange(n)])
            C **= -1
            return C, True
    else:
        for i in xrange(n):
            for j in xrange(i):
                if M[i, j] != 0:
                    C[i, j] = 1
                    C[j, i] = -1
                    return C, False


def lagrange27(Q):
    latex = ""
    n = Q.rows
    syms_c = 0
    M = Q.copy()
    P = eye(n)
    R = eye(n)
    while not M.is_diagonal():
        C, quad = replacement(M)
        M = C * M * C.T
        P = C * P
        if quad:
            R = C * R
            print(lets_latex((M, R**-1), syms[syms_c]))
        else:
            syms_c += 1
            R = eye(n)
            print(lets_latex((M, R), syms[syms_c]))
            # print заменим переменные
    return P


def lets_latex((M, C), symbol):
    latex_str = ''
    n = M.rows
    FIRST = True
    for i in range(n):
        q = ''
        first = True
        for j in range(n):
            if C[j, i] > 0:
                if not first:
                    q += '+'
                else:
                    first = False
            if C[j, i] != 0:
                q += "{} {}_{}".format(
                    latex((C)[j, i]) if C[j, i] != 1 else '',
                    symbol, j+1)

        if M[i, i] > 0:
            if not FIRST:
                latex_str += '+'
            else:
                FIRST = False

        if M[i, i] != 0:
            if M[i, i] != 1:
                latex_str += latex(M[i, i])
            latex_str += " [{}]^2".format(q)

    for i in range(n):
        for j in range(i):
            coeff = M[i, j] + M[j, i]
            if coeff != 0:
                latex_str += "{0} {s}_{1} {s}_{2}".format(
                    latex(simplify(coeff)),
                    j+1, i+1, s=symbol
                )
    return latex_str
