numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

for i in range(len(numbers) - 1):
    if isinstance(numbers[i], int):
        continue
    else:
        num1 = numbers.copy()
        num1.remove(num1[i])
        numbers[i] = sum(num1) / (len(num1) + 1)

print("Измененный список:", numbers)
