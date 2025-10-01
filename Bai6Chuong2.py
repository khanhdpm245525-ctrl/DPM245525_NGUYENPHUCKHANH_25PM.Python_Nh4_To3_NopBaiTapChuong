# 1. Toán tử chia '/'
# Chia hai số và trả về kết quả kiểu float.
a = 10
b = 3
result = a / b  # Kết quả: 3.3333333333333335
print("a / b =", result)

# 2. Toán tử chia lấy phần nguyên '//'
# Chia hai số và làm tròn kết quả xuống số nguyên gần nhất.
result = a // b  # Kết quả: 3
print("a // b =", result)

# 3. Toán tử lấy phần dư '%'
# Trả về phần dư của phép chia.
result = a % b  # Kết quả: 1
print("a % b =", result)

# 4. Toán tử lũy thừa '**'
# Tính một số mũ một số khác.
result = 2 ** 3  # Kết quả: 8
print("2 ** 3 =", result)

# 5. Toán tử logic 'and'
# Thực hiện phép toán logic "và". Kết quả trả về True nếu cả hai vế đều là True.
x = True
y = False
result = x and y  # Kết quả: False
print("x and y =", result)

# 6. Toán tử logic 'or'
# Thực hiện phép toán logic "hoặc". Kết quả trả về True nếu ít nhất một trong hai vế là True.
result = x or y  # Kết quả: True
print("x or y =", result)

# 7. Toán tử so sánh 'is'
# Kiểm tra xem hai đối tượng có phải là cùng một đối tượng trong bộ nhớ hay không.
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is b =", a is b)  # Kết quả: False
print("a is c =", a is c)  # Kết quả: True
