
"""
Training data: ([3, 3], 1), ([4, 3], 1), ([1, 1], -1)
Perception model: w * x + b
"""

inputs = [(3,3), (4, 3), (1, 1)]
labels = [1, 1, -1]

w_0 = [1, 1]
b_0 = 1
lr = 1

Loss = 0
while True:
    right_clf = 0
    for input, label in zip(inputs, labels):
        if (w_0[0] * input[0] + w_0[1] * input[1] + b_0) * label <= 0 :
            print('pt: ', input)
            grad_w_0 = -label * input[0]
            grad_w_1 = - label * input[1]
            grad_b = - label

            w_0[0] -= grad_w_0 * lr
            w_0[1] -= grad_w_1 * lr
            b_0 -= grad_b * lr

        else:
            right_clf += 1
    print(right_clf, '|', w_0, '|', b_0)

    if right_clf == 3:
        break