numbers = (5, 2, -2, 7, -8, -9, 1)
sign_changes = 0

for i in range(len(numbers)):

    if (numbers[i] > 0 and numbers[i - 1] < 0) or (numbers[i] < 0 and numbers[i - 1] > 0):
        sign_changes += 1
print(f"Количество изменений знака: {sign_changes}")
print()
some_list_1 = [4,1,6,9]
some_list_2 = [8,7,2,4,1,5,7,6]

min_element_list_1 = some_list_1[0]
for i in some_list_1:
        if i < min_element_list_1:
            min_element_list_1 = i
print(f'minimal value:{min_element_list_1}')

if min_element_list_1 in some_list_2:
 find_index = some_list_2.index(min_element_list_1)
print(f'найдено совпадение. index: {find_index} ')
