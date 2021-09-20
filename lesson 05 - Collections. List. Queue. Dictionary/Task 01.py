"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict, namedtuple


def get_company_count():
    while True:
        try:
            company_count = int(input("Введите колличество предприятий: "))
            if company_count <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Должно быть положительное целое число предприятий!")
    return company_count


def print_company(company_dict: dict):
    for name, company_performance in company_dict.items():
        print(f"{name} : годовая прибыль {company_performance.annual_profit}")


if __name__ == '__main__':
    Company = namedtuple('Company', 'profit_for_1_quarter profit_for_2_quarter profit_for_3_quarter '
                                    'profit_for_4_quarter annual_profit')
    company_dict = defaultdict(dict)

    count = get_company_count()

    annual_profit_all_companies = 0
    for company in range(1, count + 1):
        print(f"-----> {company} предприятие: ")
        name = str(input("Введите наименование предприятия: "))
        annual_profit = 0
        profit_four_quarter = []
        for quarter in range(1, 5):
            profit_for_this_quarter = float(input(f"Введите прибыль за {quarter} квартал: "))
            profit_four_quarter.append(profit_for_this_quarter)
            annual_profit += profit_for_this_quarter
        company_dict.update({name: Company(
            profit_four_quarter[0],
            profit_four_quarter[1],
            profit_four_quarter[2],
            profit_four_quarter[3],
            annual_profit
        )
        })
        annual_profit_all_companies += annual_profit

    average_profit = annual_profit_all_companies / count
    print(f"\nСредняя годовая прибыль по предприятиям: {average_profit}")

    major_companies = {}
    minor_companies = {}
    for name, company_performance in company_dict.items():
        if company_performance.annual_profit <= average_profit:
            minor_companies.update({name: company_performance})
        else:
            major_companies.update({name: company_performance})

    print("Компании с прибылью выше средней: ")
    print_company(major_companies)

    print("Компании с прибылью ниже средней: ")
    print_company(minor_companies)
