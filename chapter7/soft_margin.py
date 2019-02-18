def cal_soft_margin():
    """
    :return:
    """
    """
    min     sum(w**2)/2 + C*sum(kxi) C：代价系数
    s.t.    y_i(w*x_i + b) >= 1-kxi kxi: 松弛变量
            kxi >= 0
    """
    