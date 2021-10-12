tickets = int(input("Количество билетов: "))

total = 0

for i in range(tickets):
    age = int(input(f"Возраст {i + 1}-го посетителя: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total += 990
    else:
        total += 1390

if tickets > 3:
    print("Сумма к оплате с учëтом скидки 10%: ", total - total / 100 * 10)
else:
    print("Сумма к оплате:", float(total))
