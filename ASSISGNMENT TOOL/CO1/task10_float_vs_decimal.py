# Task 10 - Performance Comparison: Float and Decimal
from decimal import Decimal
from time import perf_counter

# Float calculation
start = perf_counter()
float_result = 0.1 + 0.2
float_time = perf_counter() - start

# Decimal calculation (construct from strings for exact decimal values)
start = perf_counter()
decimal_result = Decimal("0.1") + Decimal("0.2")
decimal_time = perf_counter() - start

print("Float result:", float_result)
print("Decimal result:", decimal_result)
print(f"Float execution time: {float_time:.8f} seconds")
print(f"Decimal execution time: {decimal_time:.8f} seconds")
print("Note: timings vary by computer; Decimal is useful when decimal precision matters.")
