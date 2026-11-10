# create the stores item names and stock counts
items = ["pencil", "pen", "eraser", "marker"]
stock_counts = [10,20,0,30]
# pair items with stock count into a dictionary
invertory = {item:count for item,count in zip(items,stock_counts)}
print("full inventory", invertory)
# filter only the items that are only in stock
in_stock_counts = [item for item in items if invertory[item]>0]
print("These are items in stock",in_stock_counts)
# ask the shopper which item they want to buy
choice = input("choose your item")
#stop the checker early if the choosen item is out of stock
if choice not in invertory or invertory[choice]==0:
    print(f"out of stock {choice}")
    exit()
#create prices and ask for a markup amount
prices = [10,5,2,15]                             
markup = int(input("enter the markup amount to add to every price"))  
# apply the markup to every price using map function
markup_prices = list(map(lambda p:p+markup,prices))
print("markup price are:",markup_prices)
# find the markup price of the chosen items
item_index = items.index(choice)
print("price of your choice after markup", markup_prices[item_index])
#reduce the stock count after the purchase
invertory[choice] = invertory[choice]-1
print(f"remaining stock of {choice} is ", invertory[choice])