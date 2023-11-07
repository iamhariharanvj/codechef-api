import json

file_path = "problems.txt"  # Replace with the path to your text file

# Difficulty level mapping based on CodeChef's difficulty ratings
difficulty_mapping = {
    "school": (0, 399),
    "basic": (400, 999),
    "easy": (1000, 1499),
    "medium": (1500, 1999),
    "hard": (2000, 5000)
    # Adjust difficulty levels and rating ranges as needed
}

with open(file_path, 'r') as file:
    lines = file.readlines()

data = []
grouped_data = []

for line in lines:
    line = line.strip()
    if line:
        data.append(line)
        if len(data) == 5:
            grouped_data.append(data)
            data = []

result = dict()
for group in grouped_data:
    if group[0] not in result.keys():
        difficulty_rating = int(group[3])
        level = "unknown"

        for tag, (lower, upper) in difficulty_mapping.items():
            if lower <= difficulty_rating <= upper:
                level = tag
                break

        result[group[0]] = {
            "code": group[0],
            "name": group[1],
            "submissions": int(group[2]),
            "difficulty": difficulty_rating,
            "contestcode": group[4],
            "level": level
        }

output_file = "problems.json"  # Replace with the desired file name

with open(output_file, 'w') as json_file:
    json.dump(result, json_file, indent=4)

print(f"Data has been written to {output_file}.")
