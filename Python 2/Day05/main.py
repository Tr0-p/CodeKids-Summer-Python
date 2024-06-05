"""

@Author Timothy
@Date 22 May 2024

Printing star patterns with loops

"""

# Demo Shape 1

for num in range(1, 6):
    print("*" * num)

# 2 minutes to work on Shape 2

for num in range(5, 0, -1):
    print("*" * num)

# 5 minutes to work on Shape 3

# Hint no.1
# print(" " * 4 + "*" * 1)
# print(" " * 3 + "*" * 2)

for num in range(1, 6):
    print(" " * (5 - num) + "*" * num)

# 3 minutes to work on Shape 4

for num in range(5, 0, -1):
    print(" " * (5 - num) + "*" * num)

# 5 minutes to work on Shape 5

# 1 = (num - 1) + num
# 3 = (num - 1) + num
# 5 = (num - 1) + num
# 7 = (num - 1) + num
# 9 = (num - 1) + num

for num in range(1, 6):
    print(" " * (5 - num) + "*" * ((num - 1) + num))

# 2 minutes to work on Shape 6A

for num in range(1, 8):
    print(" " * (7 - num) + "*" * num)

# 4 minutes to work on Shape 6B

for num in range(1, 8):
    print(" " * (7 - num) + "* " * num)

# 5 minutes to work on Shape 8

# Hint no.1 - reference shape 5

for num in range(1, 6):
    print(" " * (5 - num) + "*" * ((num - 1) + num))
for num in range(4, 0, -1):
    print(" " * (5 - num) + "*" * ((num - 1) + num))
