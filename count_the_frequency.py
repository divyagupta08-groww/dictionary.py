dict1 = {"vidit":10, "akshansh": 10, "coding":"love coding", "people":10, "a":2}
print("the original dictionary" + str(dict1))
k = 10
result = 0
for key in dict1:
    if dict1[key]==k:
        result += 1
print("the frequency of 10 is " + str(result))