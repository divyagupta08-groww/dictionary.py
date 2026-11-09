school_lunchbox1 = {"cookies","apple","juice","lollipop"}
school_lunchbox2 = {"cookies","orange","choclate","popcorn"}
print("snack box 1:",school_lunchbox1)
print("snack box 2:",school_lunchbox2)
school_lunchbox1.add("banana")
print("after adding new snack:",school_lunchbox1)
common_snacks = school_lunchbox1.intersection(school_lunchbox2)
print("the common snacks are ",common_snacks )
import array as arr
snack_counts = arr.array('i', [4,5,6,7,4])
print("snack count is", snack_counts)
snack_counts.insert(0,2)
snack_counts.append(3)
print("after adding new:",snack_counts )
reapet = snack_counts.count(4)
print(reapet)
print("final recipt")
print("snack box 1:",school_lunchbox1)
print("snack box 2:",school_lunchbox2)
print("after adding new snack:",school_lunchbox1)
print("the common snacks are ",common_snacks )
print("snack count is", snack_counts)
print("after adding new:",snack_counts )
print(reapet)


