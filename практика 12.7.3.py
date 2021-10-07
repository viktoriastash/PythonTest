money = int(input("Введите сумму:"))
print(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
накопленные_средства_TKB = money / 100 * per_cent['ТКБ']
накопленные_средства_SKB = money / 100 * per_cent['СКБ']
накопленные_средства_VTB = money / 100 * per_cent['ВТБ']
накопленные_средства_SBER = money / 100 * per_cent['СБЕР']
deposit.append(int(накопленные_средства_TKB))
deposit.append(int(накопленные_средства_SKB))
deposit.append(int(накопленные_средства_VTB))
deposit.append(int(накопленные_средства_SBER))
bank_deposit['ТКБ'] = накопленные_средства_TKB
bank_deposit['СКБ'] = накопленные_средства_SKB
bank_deposit['ВТБ'] = накопленные_средства_VTB
bank_deposit['СБЕР'] = накопленные_средства_SBER
max_bank_deposit = max(bank_deposit, key=bank_deposit.get)
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', str(max(deposit)),)
