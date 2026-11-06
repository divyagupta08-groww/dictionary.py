student_id = {"id1":{'name':'runt', 'grade':'5', 'subject':'math'},
              "id2":{'name':'james', 'grade':'6', 'subject':'english'},
              "id3":{'name':'runt', 'grade':'5', 'subject':'math'},
              "id4":{'name':'linn', 'grade':'10', 'subject':'hindi'}}
print(student_id)
print("details of student ID1 are.....")
print(student_id.get('id1','not found'))
print("details of student ID5 are.....")
print(student_id.get('id5','not found'))

student_id["id5"] ={
    'name':'alex',
    'grade':'1',
    'subject':'arts'
}
print("after adding new ID now it is")
print(student_id)
                  


cleaned_data = {}
seen_records = []
 
for student_data, details in student_id.items():
    unique_key = (details['name'], details['grade'], details['subject'])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_data] = details
 
student_data = cleaned_data
print(cleaned_data)
 
print("")
print("After removing duplicate records:")
print(student_id)
print("removing student id 4")
removed_student = student_id.pop("id4","student not found")
print(removed_student)
print(student_id)

lenght = len(student_id)
print(lenght)
student_id["id2"] ={
    'name':'james',     
    'status':'left school'      
}
print(student_id)
print("="*10,"student subject data","="*10)
for student_data,details in student_id.items():
    print(student_id, ":", details)

