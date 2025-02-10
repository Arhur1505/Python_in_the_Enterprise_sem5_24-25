import json
from decimal import Decimal, ROUND_HALF_UP

def load_data(filename="students_data.txt"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data, filename="students_data.txt"):
    with open(filename, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_student(data, name, surname, scores, attendance):
    data[f"{name} {surname}"] = {"scores": scores, "attendance": attendance}

def add_score(data, name, surname, subject, score):
    student = f"{name} {surname}"
    if student in data:
        if subject not in data[student]["scores"]:
            data[student]["scores"][subject] = []
        data[student]["scores"][subject].append(score)
    else:
        print("Student not found")

def student_total_avg(data, name, surname):
    student = f"{name} {surname}"
    if student in data:
        subject_averages = []
        for scores in data[student]["scores"].values():
            subject_avg = sum(scores) / len(scores)  
            rounded_avg = int(Decimal(subject_avg).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
            subject_averages.append(rounded_avg)
        total_avg = sum(subject_averages) / len(subject_averages) if subject_averages else 0
        return round(total_avg, 2)
    else:
        print("Student not found")
        return 0

def student_subject_avg(data, name, surname, subject):
    student = f"{name} {surname}"
    if student in data and subject in data[student]["scores"]:
        scores = data[student]["scores"][subject]
        return round(sum(scores) / len(scores), 2) if scores else 0
    else:
        print("Student or subject not found")
        return 0

def class_subject_avg(data, subject):
    subject_averages = []
    for student in data.values():
        scores = student["scores"].get(subject, [])
        if scores:
            avg_score = sum(scores) / len(scores)
            rounded_avg = int(Decimal(avg_score).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
            subject_averages.append(rounded_avg)
    return round(sum(subject_averages) / len(subject_averages), 2) if subject_averages else 0

def student_attendance(data, name, surname, increment=False):
    student = f"{name} {surname}"
    if student in data:
        if increment:
            data[student]["attendance"] += 1
        return data[student]["attendance"]
    else:
        print("Student not found")
        return 0

def class_total_avg(data):
    scores = [score for student in data.values() for subject in student["scores"].values() for score in subject]
    return round(sum(scores) / len(scores), 2) if scores else 0

if __name__ == "__main__":
    data = load_data()

    students_info = [
        ("Max", "Verstappen", {"Matematyka": [4, 5, 3], "Biologia": [5, 4]}, 10),
        ("Lando", "Norris", {"Fizyka": [3, 4], "Chemia": [5, 5, 6]}, 8),
        ("Lewis", "Hamilton", {"Historia": [4, 4, 4], "Geografia": [3, 5]}, 12),
        ("Charles", "Leclerc", {"Matematyka": [2, 3, 4], "Fizyka": [5, 5]}, 7),
        ("Oscar", "Piastri", {"Biologia": [5, 4, 4], "Chemia": [2, 3]}, 9),
        ("Carlos", "Sainz", {"Matematyka": [6, 5], "Geografia": [3, 4, 4]}, 11),
        ("George", "Russel", {"Historia": [4, 3, 3], "Biologia": [5, 6]}, 10),
        ("Sergio", "Pérez", {"Chemia": [2, 3, 4], "Fizyka": [5, 5]}, 6),
        ("Fernando", "Alonso", {"Geografia": [4, 4, 4], "Historia": [2, 3]}, 8),
        ("Daniel", "Ricciardo", {"Matematyka": [3, 2, 4], "Biologia": [5, 5]}, 9),
        ("Sebastian", "Vettel", {"Fizyka": [3, 3, 4], "Chemia": [5, 4]}, 7),
        ("Ayrton", "Senna", {"Historia": [4, 5, 5], "Matematyka": [2, 2, 3]}, 10)
    ]

    for name, surname, scores, attendance in students_info:
        add_student(data, name, surname, scores, attendance)

    add_score(data, "Max", "Verstappen", "Matematyka", 5)
    add_score(data, "Lewis", "Hamilton", "Historia", 5)
    student_attendance(data, "Ayrton", "Senna", increment=True)
    student_attendance(data, "Sebastian", "Vettel", increment=True)

    print("Total class average:", class_total_avg(data), "\n")

    for name, surname, _, _ in students_info:
        print(f"{name} {surname}'s attendance:", student_attendance(data, name, surname))
        for subject in data[f"{name} {surname}"]["scores"]:
            print(f"{name} {surname}'s average in {subject}:", student_subject_avg(data, name, surname, subject))
        print(f"{name} {surname}'s total average:", student_total_avg(data, name, surname))
        print()

    all_subjects = set(subject for student in data.values() for subject in student["scores"])
    print("Class averages by subject:")
    for subject in all_subjects:
        print(f"Average for {subject}: {class_subject_avg(data, subject)}")

    save_data(data)