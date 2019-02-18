from dataset import create_dataset
import math
from math import log
from numpy import sort

df = create_dataset()

def cross_entropy(probas1, probas2):
    """
    Description:
    ============
        其用来衡量在给定的真实分布下，使用非真实分布所指定的策略消除系统的不确定性所需要付出的努力的大小.

    Formula:
    ========
        CEH(p, q) = -SIGMA_x(p(x) * log(q(x)))

    Data elements:
    ==============
        Age:    [Young, Middle, Old]
        Work:   [Yes, No]
        House:  [Yes, No]
        Credit: [Normal, Good, Excellent]
    :param label: [1, -1]
    :param data: age, work house, credit, label
    :return: Cross entropy
    """
    # e.g. Work
    CEH = 0
    for p1, p2 in zip(probas1, probas2):
        CEH -= p1 * math.log(p2,2)

    return CEH

def entropy(probas):
    EH = 0
    for proba in probas:
        EH -= proba * math.log(proba, 2)
    return EH

def probability(data1, data2=None):
    """
    If only one series of data is given, calculate the probability;
    else, calculate the conditional probabilit, with data1 noted as label.
    :param data1: Label(For data2 not None)
    :param data2:
    :return: Probability(list type), dictionary
    """

    dictionary = {}
    if data2 is None:

        for datum in data1:
            if datum in dictionary.keys():
                dictionary[datum] += 1
            else:
                dictionary[datum] = 1
        proba = []
        for key in dictionary.keys():
            proba.append(dictionary[key]/len(data1))

        return proba, dictionary
    else:
        for datum1, datum2 in zip(data1, data2):
            if (datum1, datum2) in dictionary.keys():
                dictionary[(datum1, datum2)] += 1
            else:
                dictionary[(datum1, datum2)] = 1

        proba = []
        for key in dictionary.keys():
            proba.append(dictionary[key] / len(data1))

        return proba, dictionary

def relative_entropy(probas1, probas2):
    """
    Description:
    ============
        其用来衡量两个取值为正的函数或概率分布之间的差异.

    Formula:
    ========
        D_KL(p||q) = SIGMA_x(p(x) * log(p(x)/q(X)))

    Data elements:
    ==============
        Age:    [Young, Middle, Old]
        Work:   [Yes, No]
        House:  [Yes, No]
        Credit: [Normal, Good, Excellent]
    :param label: [1, -1]
    :param data: age, work house, credit, label
    :return: Relative entropy
    """
    REH = 0
    for p1, p2 in zip(probas1, probas2):
        REH += p1 * math.log(p1/p2, 2)

    return REH

def cond_entropy(dict_cond, dict_var):

    """
    H(Y|X) = SIGMA_i(p_i * H(Y|X=x_i))
           = SIGMA_i(p_i * ( - SIGMA_j(p(y_j|x_i) * log(p(y_j|x_i)))
    此处y为label, 取值范围为{-1, 1}, 因此，可写作:
           =  SIGMA_i{ p（xi）
           * (- p(1|x_i) * log(p(1|x_i)) - p(-1|x_i) * log(p(-1|x_i))}

    换言之，对于dict_cond中的任意一项，找其对应的条件的发生概率。

    :param dict_cond: 条件概率.
    :param dict_var: 条件发生概率.
    :return: 条件熵.
    """
    cond_eh = 0
    for cond_var in dict_cond.keys():
        proba_cond = dict_cond[cond_var] / 15
        proba_var = dict_var[cond_var[0]]/15
        cond_eh -= proba_cond * math.log(proba_cond/proba_var, 2)

    return cond_eh

class gain_entropy():
    def __init__(self, D, A):
        """

        :param D: Label list.
        :param A: Feature list.
        self.Ag: Feature name which has the largest gained entropy.
        """
        self.D = D
        self.A = A
        self.Ag = None

    def gain_DA(self):
        num_positive = (15 + self.D.sum()) / 2
        p_positive = num_positive / 15
        H_D = - ( p_positive * log(p_positive, 2) ) - ( (1-p_positive) * log(1-p_positive, 2) )
        for a in self.A:  # a: Age, Work, House ...
            # 计算经验条件熵：
            da = self.A[a] # da: [Yes, No, ...]
            dict = {}
            for i, a_value in enumerate(da):
                label = self.D[i]
                value = a_value # value: 'Yes'
                if (value, label) in dict.keys():
                    dict[(value, label)] += 1
                else:
                    dict[(value, label)] = 1

                H_Da = 0
                for key in dict.keys(): # key: ('Yes', 1), ...
                    p_cond = dict[key] / 15

                    label = key[1]
                    if label == 1:
                        p_label = p_positive
                    else:
                        p_label = 1 - p_positive
                    feat = key[0]
                    p_feat = 0
                    for item in da:
                        if item == feat:
                            p_feat += 1/15
                    H_Da -=
#                     TODO: 太难////






def print_EH():
    proba_label, dict_label = probability( df['Label']) # 0.971

    print('===exp_entro=====')
    print(entropy(proba_label))

    print('===cond_entro=====')
    for key in df.keys()[:-1]:
        _, dict_key = probability(df[key])
        _, dict_cond = probability(df[key], df['Label'])
        print('Key: ', key)
        print('Gained Entropy: ',entropy(proba_label) - cond_entropy(dict_cond, dict_key))

"""
===exp_entro=====
0.9709505944546686
===cond_entro=====
Key:  Age
Gained Entropy:  0.08300749985576894
Key:  Work
Gained Entropy:  0.32365019815155627
Key:  House
Gained Entropy:  0.4199730940219749
Key:  Credit
Gained Entropy:  0.36298956253708536
"""

def demo_proba():
    p1 = [0.5, 0.25, 0.125, 0.125]
    p2 = [0.25, 0.25, 0.25, 0.25]
    print(cross_entropy(p1, p2)) # 2
    print(relative_entropy(p1, p2)) # 0.25

if __name__ == '__main__':
    print(df)
    print_EH()