import csv

with open('states1.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# print("Number of Rows:", len(rows))
# print("Columns:", list(rows[0].keys()))

values = []

# for row in rows:
#     value = float(row['SHAPE_Area'])
#     values.append(value)

# values = []

# for row in rows:
#     raw = row['SHAPE_Area'].strip()

#     if not raw:
#         continue

#     values.append(float(raw))

# print("Largest Value:", max(values))
# print("Smallest Value:", min(values))
# print("Count:", len(values))

import csv

def inspect_column(filename, column):
    with open(filename, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []

    for row in rows:
        raw = row[column].strip()

        if not raw:
            continue

        values.append(float(raw))

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }
area_result = inspect_column("states1.csv", "SHAPE_Area")
length_result = inspect_column("states1.csv", "SHAPE_Leng")

print("Area:", area_result)
print("Length:", length_result)
