#Create two fruits baskets as sets
basket1 = {"mango", "pineapple", "apple","guava"}
basket2 = {"melon", "pineapple", "watermelon","banana"}
print(basket1)
print(basket2)
#add a new fruit to basket1
basket1.add("orange")
print(basket1)
#find fruits common to both baskets\
print(basket1.intersection(basket2))
#create an array of fruit counts using the array module
import array as arr
fruit_counts = arr.array('i',[1,3,7,9,3])
print(fruit_counts)
#add new fruit count to array
fruit_counts.insert(0,1)
fruit_counts.append(4)
print(fruit_counts)
#count the number of ocarances of the number 3
print(fruit_counts.count(3))
#reverse the order of the array
fruit_counts.reverse()
print(fruit_counts)
