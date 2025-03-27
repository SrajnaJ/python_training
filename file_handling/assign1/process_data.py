def calculate_total_marks(data):
    for row in data:
        row["Total Marks"] = int(row["Math"]) + int(row["Science"]) + int(row["English"])
    return data
