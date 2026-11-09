habit_info = ("reading",True,2,0.9)
print(habit_info)
habits = (1,0,1,0,1,1,0)
print(habits)
lenght = len(habits)
print("total days tracked:", lenght)
print("day1 status",habits[0])
print("day5 status",habits[4])
print("first three days status ", habits[0:3])
weekend_habits = habits[5:7]
print(weekend_habits)
habits = habits + (1,)
print("after add new day,", habits)
completed = habits.count(1)
incompleted = habits.count(0)
print("completed",completed)
print("incomplete",incompleted)
done  = 0
not_done = 0
for i in range(0, len(habits)):
    if habits[i] == 1:
        done += 1
        not_done +=1
if done > not_done:
    print("great keep up the good work")
else:
    print("keep working hard")
print("final status")
print("habits", habits)
print("weekend habits", weekend_habits)
print("first three days",habits[0:3])
print("completed",completed)
print("incomplete",incompleted)