print("="*60)
print(" "*25,"grocery store")
print("="*60)
milk = 85
fruits = 50
chese = 50
grains = 70
no_of_baskets = 4
family_members = 4
costumer_price = (milk+fruits+chese+grains)/no_of_baskets/family_members
print("price per costumer is ",costumer_price)
items = int(input("number of items:"))
members = int(input("number of family members:"))
no_items_per_member = items/members
if no_items_per_member != 0 :
    print("this is non-divisible")
    print(f"you have {no_items_per_member} items per family member")
else:
    print("this is divisible" \
    "")
    print(f"you have {no_items_per_member} items per family member")
recorded_average = 65
total_weeks = 4
wrong_recorded = 70
correct_average = 60
per_week_average = 15
print("the corrected recored average per day is = ", correct_average/per_week_average)
print("average of stores per week =")
store_a = 40
store_b = 90
store_c = 60
print("the average of the stores is", (store_a+store_b+store_c)/3)
print("recipt")
print("price per costumer is ",costumer_price)
print(f"you have {no_items_per_member} items per family member")
print("the corrected recored average per day is = ", correct_average/per_week_average)
print("the average of the stores is", (store_a+store_b+store_c)/3)
print("thank you")