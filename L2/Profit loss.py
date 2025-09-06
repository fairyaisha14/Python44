#Write to check if a person is buying oranges at 100 rs and later selling it at 120 rs. Find that he has profit or loss?
costprice =int(input("enter the cp"))
sellingprice =int(input("enter the sp"))

if(sellingprice>costprice):
    print("profit")
    pt=sellingprice-costprice
    print(pt)
else :
    print("No profit")