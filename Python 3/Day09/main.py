some_code = None

names = [
    "averie butler",
    "ryder nielsen",
    "vienna weaver",
    "tucker enriquez",
    "nellie swanson",
    "hugo cantrell",
    "yamileth leach",
    "westin vo",
    "artemis buckley",
    "aryan rhodes",
    "tatum berg",
    "cayson mahoney",
    "promise bryan",
    "jaxtyn kennedy",
    "brianna andersen",
    "alistair ortega",
    "lilah horn",
    "wilson yu",
    "navy torres",
    "jayden ingram",
    "katie moses",
    "niklaus james",
    "quinn kim",
    "roman carroll",
    "zara rice",
    "graham deleon",
    "gabrielle lambert",
    "mario wilcox",
    "ashlyn cardenas",
    "johnathan gordon",
    "taylor frank",
    "braylen schaefer",
    "mavis hartman",
    "baker perez",
    "eleanor bond",
    "roger shah",
    "angelica woodward",
    "jeremias trujillo",
    "danielle miranda",
    "rory cruz",
]
numbers = [
    0,
    2,
    3,
    5,
    12,
    13,
    20,
    21,
    22,
    24,
    26,
    27,
    28,
    33,
    34,
    35,
    37,
    40,
    43,
    44,
    45,
    46,
    48,
    50,
    51,
    52,
    53,
    55,
    56,
    58,
    59,
    60,
    63,
    64,
    70,
    71,
    72,
    73,
    77,
    80,
    83,
    87,
    89,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
]


def add10(x):
    result = x + 10
    return result


# print(add10(10))

add5 = lambda x: x + 5

# print(add5(10))

# ================ DEMO ================

# lambda functions

# sorting

words = ["apple", "orange", "elephant", "banana", "cat"]
# print(words)
# print(sorted(words, key=lambda x: len(x)))

# print(max(names, key=lambda x: len(x)))

name = "averie butler"
# print(name.split(" ")[1])

# mapping
# A = [1 2 3 4 5]
#      V V V V V
# B = [3 4 5 6 7]


# capalise the first letter of the first name and last name of the names
def formatting(name):
    splitName = name.split(" ")
    firstName = list(splitName[0])
    lastName = list(splitName[1])

    firstName[0] = firstName[0].upper()
    lastName[0] = lastName[0].upper()

    firstName = "".join(firstName)
    lastName = "".join(lastName)

    return firstName + " " + lastName


# print(list(map(formatting, names)))

# filtering
# A = [1, 2, 3, 4, 5]
# B = list(filter(lambda x: x > 2, A))
# print(B)

# ============= EXERCISE ===============

# sort the names by length
nameByLength = sorted(names, key=lambda x: len(x))

# sort the names by surname
nameByLastname = sorted(names, key=lambda x: x.split(" ")[1])

# divide all the numbers by 3
dividedBy3 = list(map(lambda x: x // 3, numbers))

# add 10 to all the numbers
# add10toNums = list(map(lambda x: x + 10, numbers))
add10toNums = list(map(add10, numbers))

# check if the numbers are divisible by 5 (a list of True / False)
divisibleBy5 = list(map(lambda x: x % 5 == 0, numbers))

# check if the name has the letter s (a list of True / False)
hasS = list(map(lambda x: "s" in x, names))

# map all the numbers into strings

# filter out all the "string" numbers that are 2 digits (keep single digits)

# map the filtered string numbers back into numbers

# filter out all even numbers (keep odds)

# filter out all odd numbers (keep evens)

# filter out all numbers that are greater than 50 (keep less than 50)
lessThan50 = list(filter(lambda x: x < 50, numbers))
print(lessThan50)

# filter out all names that don't start with a (keep the As)

# filter out all the surnames that don't start with c (keep the Cs)
