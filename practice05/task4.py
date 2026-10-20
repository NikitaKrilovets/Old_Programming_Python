# Task 4 - Krilovets - IT-31

last_name = "Krilovets"

a = 8
b = 5
c = len(last_name)

greater_result = a > b
less_result = b < c
range_result = 1 <= b <= c

equal_result = a == b
not_equal_result = a != a
greater_equal_result = b >= c

print(f"a > b: {greater_result}, type: {type(greater_result)}")
print(f"b < c: {less_result}, type: {type(less_result)}")
print(f"1 <= b <= c: {range_result}, type: {type(range_result)}")
print(f"a == b: {equal_result}, type: {type(equal_result)}")
print(f"a != a: {not_equal_result}, type: {type(not_equal_result)}")
print(f"b >= c: {greater_equal_result}, type: {type(greater_equal_result)}")