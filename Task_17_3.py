per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
deposit = []
for el in per_cent:
    deposit.append(int(per_cent[el] * money / 100))
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать - " + str(max_deposit))