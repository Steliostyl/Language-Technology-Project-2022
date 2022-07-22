array = [1, 5, 2, 'avg_tf']

for index, el in enumerate(array):
    if type(el) != int:
        array[index] = int(el, 16)

print(sorted(array))