# решим задачу через defaultdict

from collections import defaultdict
from collections import OrderedDict
num = int(input('Введите количество предприятий: '))
result_dict = defaultdict(list)
avg_profit = 0
for i in range(num):
    company = input('Введите название предприятия: ')
    profit = [int(j) for j in input('Введите прибыль предприятия за 4 квартала через пробел: ').split( )]
    avg_profit += sum(profit) / num
    result_dict[company].append(sum(profit))
company_profit_less_avg = []
company_profit_more_avg = []
for i in result_dict:
    if result_dict[i][0] < avg_profit:
        company_profit_less_avg.append(i)
    else:
        company_profit_more_avg.append(i)
print(f'Cредня годовая прибыль всех предприятий {avg_profit}')
print(f'Предприятия, с прибылью выше среднего значения:{",".join(company_profit_more_avg)}')
print(f'Предприятия, с прибылью ниже среднего значения:{",".join(company_profit_less_avg)}')
