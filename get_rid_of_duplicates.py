student_data =  {"id1": {"name":"vidit","class":5, "subject": "math"},
                "id2":{"name":"rigiv","class":4, "subject": "SST"},
                "id3":{"name":"himin","class":6, "subject": "english"},
                "id4":{"name":"yip","class":6, "subject": "science"},
                "id5":{"name":"yip","class":6, "subject": "science"}}
result = {}
seen_keys = []
for student_id,details in student_data.items():
    unique_key = (details["name"],details["class"], details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for key, value in result.items():
    print(key,":",value)


