#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def total_calc(bill_amount,tip_perc):
#define fuction to calculate the tip on the bill
     total = bill_amount*(1 + 0.01*tip_perc)
     total = round(total,2)
     print(f"Please pay ${total}")


total_calc(150,20)