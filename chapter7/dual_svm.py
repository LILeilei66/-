def dual_svm():
    """
    algorithm:
    ===========
        L(w,b,a) = sum(w**2) - sum(alpha * y * (wx+b)) + sum(alpha)
        max_a{ min_w_b {L(w,b,a)}}

    :return:
    """
    # a1, a2, a3

    L = (18*a1**2 + 25*a2**2 + 2*a3**2+42*a1*a3 - 12*a1*a3 - 14*a2*a3)-a1-a2-a3
    s = 4*a1**2 + 13/2*a2**2 + 10*a1*a2 - 2*a1 - 2*a2

    """
    1. 计算奇点
    2. 由于奇点不满足st，因此极值位于边界上。
    3. 计算得解
    """

