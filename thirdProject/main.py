import collections
import random
from tabulate import tabulate

stream = {}
uniform_positions = []
count_of_elements = 1000000
count_of_variables = 100
count = count_of_elements / count_of_variables
variables = [[0, 0] for i in range(count_of_variables)]


def generating_of_stream():
    l = 0
    j = count
    k = 0
    for i in range(count_of_variables):
        b = random.randint(l, j)
        j += count
        l += count
        uniform_positions.append(b)
    for i in range(count_of_elements):
        a = random.randint(0, 1000)
        if a not in stream.keys():
            stream[a] = 1
        else:
            stream[a] += 1
        # if a in variables.keys():
        #     variables[a] += 1
        # if k < count_of_variables:
        #     if i == uniform_positions[k]:
        #         variables[a] = 1
        #         k += 1
        for p in range(len(variables)):
            if variables[p][0] == a:
                variables[p][1] += 1
        if k < count_of_variables:
            if i == uniform_positions[k]:
                variables[k][0] = a
                variables[k][1] = 1
                k += 1


def calculating_0th_moment():
    return len(stream)


def calculating_1th_moment():
    sum = 0
    for i in range(len(stream)):
        sum += stream[i]
    return sum


def calculating_2th_moment():
    avg = 0
    for i in range(count_of_variables):
        avg += count_of_elements * (2 * variables[i][1] - 1)
    avg = avg / count_of_variables
    return avg


if __name__ == '__main__':
    generating_of_stream()
    print('0th moment: ' + str(calculating_0th_moment()))
    print('1th moment: ' + str(calculating_1th_moment()))
    print('2th moment with ' + str(count_of_variables) + ' variables: ' + str(calculating_2th_moment()))
    f = open('result_map.txt', 'w')
    headers = ["Value", "Quantity"]
    result_stream = collections.OrderedDict(sorted(stream.items()))
    f.write(tabulate(result_stream.items(), headers=headers, tablefmt="grid"))
    f.close()
