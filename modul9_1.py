def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)

    return results


# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
