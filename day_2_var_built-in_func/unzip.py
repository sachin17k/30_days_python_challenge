data = [
    ("Tom", 85),
    ("Jerry", 90),
    ("Spike", 88)
]
names, marks = zip(*data)

print(f"names:{names}")
print(f"marks:{marks}")