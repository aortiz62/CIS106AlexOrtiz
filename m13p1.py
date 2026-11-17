students = {
    "Smith": 88,
    "Johnson": 92,
    "Williams": 79,
    "Brown": 95,
    "Jones": 84,
    "Garcia": 91,
    "Miller": 76,
    "Davis": 89,
    "Rodriguez": 94,
    "Martinez": 82
}

print(f"{'Student Name':<15} {'Grade':<10}")
print("-" * 25)

total = 0
for name, grade in students.items():
    print(f"{name:<15} {grade:<10}")
    total += grade
