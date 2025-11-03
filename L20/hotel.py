def hotel_cost(nights):
    return 140*nights

#Define a function called plane ride cost that takes a string, city, as input
def plane_rice_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angles" == city:
        return 475
    
#Define a function called rental_car_cost with an argument called days
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50   
     if days>=7 :
        return 40*days - 50     
    