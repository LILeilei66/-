from numpy import arange
def cal_svm():
    """
    algorithme:
    ===========
        min: sum(w ** 2)/2
        s.t. ...
        
    :return: w, b
    """
    """
    已知 x1, x2, x3;
    求 max_margin support vector

    """


    min_dist = 100.0

    MAX = 5.0
    MIN = -5.0
    STEP = 0.5

    for w1 in arange(MIN, MAX, STEP):
        for w2 in arange(MIN, MAX, STEP):
            for b in arange(MIN,MAX, STEP):
                if (3 * w1 + 3 * w2 + b -1 <0):
                    continue
                if (4 * w1 + 3 * w2 + b -1 <0):
                    continue
                if (- w1 - w2 - b -1 <0):
                    continue
                if (w1 ** 2 + w2 ** 2) / 2 < min_dist:
                    w_0 = [w1, w1]
                    b_0 = b
                    min_dist = (w1 ** 2 + w2 ** 2) / 2

    return w_0, b_0, min_dist

if __name__ == '__main__':
    w_0, b_0, min_dist = cal_svm()
    print(w_0, b_0, min_dist)
    """
    [0.5, 0.5] -2.0 0.25
    """