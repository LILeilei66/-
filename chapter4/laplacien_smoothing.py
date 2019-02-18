labels = [0]*15
inputs = []
alpha = 1

test = [2,'s']

for i in range(15):
    if i < 5:
        if i == 1 or i == 2:
            inputs.append([1,'m'])
        else:
            inputs.append([1,'s'])

    elif i < 10:
        if i == 5:
            inputs.append([2,'s'])
        elif i < 8:
            inputs.append([2,'m'])
        else:
            inputs.append([2,'l'])

    else:
        if i >= 11 and i<13:
            inputs.append([3,'m'])
        else:
            inputs.append([3,'l'])

for i in range(len(labels)):
    if i == 2 or i == 3:
        labels[i] = 1
    elif i > 6 and i < 14:
        labels[i] = 1
    else:
        labels[i] = -1

positive = []
negative = []
for i,label in enumerate(labels):
    if label == 1:
        positive.append(i)
    else:
        negative.append(i)

p_positive = (len(positive) + 1) / (15 + 2)
p_negative = (len(negative) + 1) / (15 + 2)

p_2_positive = 0
for idx in positive:
    if inputs[idx][0] == 2:
        p_2_positive += 1
p_2_positive = (p_2_positive + alpha) / (len(positive) + 3 * alpha)

p_2_negative = 0
for idx in negative:
    if inputs[idx][0] == 2:
        p_2_negative += 1
p_2_negative = (p_2_negative + alpha) / (len(negative) + 3 * alpha)

p_s_positive = 0
for idx in positive:
    if inputs[idx][1] == 's':
        p_s_positive += 1
p_s_positive = (p_s_positive + alpha) / (len(positive) + 3 * alpha)

p_s_negative = 0
for idx in negative:
    if inputs[idx][1] == 's':
        p_s_negative += 1
p_s_negative = (p_s_negative + alpha) / (len(negative) + 3 * alpha)

p_test_positive = p_positive * p_2_positive * p_s_positive
p_test_negative = p_negative * p_2_negative * p_s_negative

print(p_positive, '|', p_negative)
print(p_test_positive, '|', p_test_negative)