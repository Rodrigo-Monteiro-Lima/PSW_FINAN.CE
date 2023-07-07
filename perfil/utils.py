from datetime import datetime


def sum_total_value(obj, field):
    total = 0
    for value in obj:
        total += getattr(value, field)
    return total


def calculate_financial_balance():
    from extrato.models import Values

    essential_expenses = (
        Values.objects.filter(date__month=datetime.now().month)
        .filter(value_type="O")
        .filter(category__essential=True)
    )
    non_essential_expenses = (
        Values.objects.filter(date__month=datetime.now().month)
        .filter(value_type="O")
        .filter(category__essential=False)
    )

    total_essential_expenses = sum_total_value(essential_expenses, "value")
    total_non_essential_expenses = sum_total_value(non_essential_expenses, "value")

    total = total_essential_expenses + total_non_essential_expenses
    try:
        percent_essential_expenses = total_essential_expenses * 100 / total
        percent_non_essential_expenses = total_non_essential_expenses * 100 / total

        return percent_essential_expenses, percent_non_essential_expenses
    except:
        return 0, 0
