numbers = (5, 2, -2, 7, -8, -9, 1)
sign_changes = 0

for i in range(1, len(numbers)):

    if (numbers[i] > 0 and numbers[i - 1] < 0) or (numbers[i] < 0 and numbers[i - 1] > 0):
        sign_changes += 1
print(f"Количество изменений знака: {sign_changes}")
print()
