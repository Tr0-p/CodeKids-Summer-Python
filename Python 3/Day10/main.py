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


# ================ DEMO ================

# lambda functions

# sorting

# mapping

# filtering

# ============= EXERCISE ===============

# sort the names by length
sorted(names, key=len)

# sort the names by surname
sorted(names, key=lambda x: x.split(" ")[1])

# add 10 to all the numbers
list(map(lambda x: x + 10, numbers))

# divide all the numbers by 3
list(map(lambda x: x / 3, numbers))

# check if the numbers are divisible by 5 (a list of True / False)
list(map(lambda x: x % 5, numbers))

# check if the name has the letter s (a list of True / False)
list(map(lambda x: "s" in x, names))

# map all the numbers into strings
strNum = list(map(str, numbers))
# print(strNum)

# filter out all the "string" numbers that are 2 digits (keep single digits)
singleNum = list(filter(lambda x: len(x) == 1, strNum))
# print(singleNum)

# map the filtered string numbers back into numbers
fltrNum = list(map(int, singleNum))
# print(fltrNum)

# filter out all even numbers (keep odds)
odd = list(filter(lambda x: x % 2 == 1, numbers))
print(odd)

# filter out all odd numbers (keep evens)
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# filter out all numbers that are greater than 50 (keep less than 50)
list(filter(lambda x: x < 50, numbers))

# filter out all names that don't start with a (keep the As)
aNames = list(filter(lambda x: x.startswith("a"), names))
print(aNames)

# filter out all the surnames that don't start with c (keep the Cs)
list(filter(lambda x: x.split(" ")[1].startswith("c"), names))
