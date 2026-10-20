my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

precision = 10000
pie_sum = 0

for i in range(precision):
    pie_sum += (-1)**i / (2*i+1)

pie = 4 * pie_sum
print(pie)