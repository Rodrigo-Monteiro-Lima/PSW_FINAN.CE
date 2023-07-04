def sum_total_value(obj, field):
    total = 0
    for value in obj:
        total += getattr(value, field)
    return total
