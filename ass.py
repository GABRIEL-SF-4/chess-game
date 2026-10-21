my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

precision = 10000
pie_sum = 0

for i in range(precision):
    pie_sum += (-1)**i / (2*i+1)

pie = 4 * pie_sum
print(pie)

my_list = ['a', 'b', 'c']
new_list = my_list.copy()
even_newer_list = my_list

my_list.pop(2)

print(my_list)
print(new_list)
print(even_newer_list)