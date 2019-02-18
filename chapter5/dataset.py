import pandas as pd
from pandas import Series, DataFrame


def create_dataset():
    age_list = []
    for i in range(15):
        if i < 5:
            age = 'young'
        elif i < 10:
            age = 'middle'
        else:
            age = 'old'

        age_list.append(age)

    work_list = []
    for i in range(15):
        if i in (2, 3, 7, 12, 13):
            working = 'Yes'
        else:
            working = 'No'
        work_list.append(working)

    house_list = []
    for i in range(15):
        if i in (3, 7, 8, 9, 10, 11):
            house = 'Yes'
        else:
            house = 'No'
        house_list.append(house)

    cred_list = []
    for i in range(15):
        if i in (1, 2, 6, 7, 11, 12):
            cred = 'Good'
        elif i in (8, 9, 10, 13):
            cred = 'Excellent'
        else:
            cred = 'Normal'
        cred_list.append(cred)

    label_list = []
    for i in range(15):
        if i in (0, 1, 4, 5, 6, 14):
            label = -1
        else:
            label = 1
        label_list.append(label)


    data = {'Age':Series(age_list),
            'Work':Series(work_list),
            'House':Series(house_list),
            'Credit':Series(cred_list),
            'Label':Series(label_list),
            }

    df = DataFrame(data)
    return df