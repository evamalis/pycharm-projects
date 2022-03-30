data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

sorted(data, key = lambda x: x[0] / x[1] ** 2)
print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу

