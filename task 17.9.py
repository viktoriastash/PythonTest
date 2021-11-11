def puzirek(array): #функция пузырьковой сортировки
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def dvoichniy(array, element, left, right): #функция двоичного поиска с рекурсией
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return dvoichniy(array, element, left, middle - 1)
    else:  # иначе в правой
        return dvoichniy(array, element, middle + 1, right)
spisok = list(map(int, input("Введите последовательность чисел:").split())) #ввод списка
chislo = int(input("Введите любое число:")) #ввод числа
if len(spisok)<2: #проверка на то что наш список не состоит из 1 элемента
    print("Введеная последовательность крайне мала!!!!") #алярм
    spisok += list(map(int, input("Введите еще числа через пробел:").split())) #добавляем элементы в список
print("Исходный список =", spisok)
print("Отсортированный список:", puzirek(spisok)) #выполняем функцию пузырьковой сортировки на списке
index = dvoichniy(spisok, chislo, 0, len(spisok)) #переменная индекс элемента
if index == False:
    spisok.append(chislo) #если числа нет в списке то добавляем
    puzirek(spisok) #сортируем после добавления
    index = dvoichniy(spisok, chislo, 0, len(spisok))
    print("Число не найдено в списке. Если бы веденное число присутствовало в списке, то его индекс был бы:", index)
else:
    print("Введенное число:", chislo, "найдено! Его индекс в списке:", index)
