def is_year_leap(year):
    """Возвращает True, если год високосный, иначе False."""
    return year % 4 == 0


year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")
