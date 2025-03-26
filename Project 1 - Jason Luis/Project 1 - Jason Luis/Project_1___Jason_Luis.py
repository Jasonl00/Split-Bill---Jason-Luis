#Dinner Check Spilt 
# Jason Luis 
# Professor Ghaforyfard 
# February 13, 2024 
# This program will present a check that three individuals have split to see how much each person will pay for their meal and the total cost of the bill together. 

from ctypes.wintypes import FLOAT
from string import printable


#Variables

tip = 0.1

total_ind_1 = 0

total_ind_2 = 0

total_ind_3 = 0

subtotal_all = 0 

total_all = 0

final_total_all = 0

tip_all = 0.20 

menu_item_1 = 0 

menu_item_2 = 0 

menu_item_3 = 0 

amount_drink_1 = 0

amount_drink_2 = 0 

amount_drink_3 = 0

total_1 = 0

total_2 = 0

total_3 = 0

subtotal_1 = 0

subtotal_2 = 0

subtotal_3 = 0

#Code for the split bill 
print("Individual Bills") 
print("-----------------------------------------------------")

#Person 1

name_1 = input("\nName: ") 

menu_item_1 = input("\nAmount of Lunch Menu Item: $")

amount_drink_1 = input("\nAmount of Drink: $") 

total_ind_1 = float(menu_item_1) + float(amount_drink_1) #calculation of the items ordered

subtotal_1 = float(total_ind_1 * tip) #calculating the subtotal with the tip 

total_1 = float(total_ind_1 + subtotal_1) #total bill for the individual

print("\n", name_1,"'s subtotal without 10% tip is: $", total_ind_1) #output of the subtotal

print("\n",name_1,"'s bill with 10% tip included is:$",total_1) #output of the total with 10% tip

print("--------------------------------------------------------")

#Person 2

name_2 = input("\nName: ")

menu_item_2 = input("\nAmount of Lunch Menu Item: $") 

amount_drink_2 = input("\nAmount of Drink: $") 

total_ind_2 = float(menu_item_2) + float(amount_drink_2) #calculation of the items ordered

subtotal_2 = float(total_ind_2 * tip) #calculating the subtotal with the tip 

total_2 = float(total_ind_2 + subtotal_2) #total bill for the individual

print("\n", name_2,"'s subtotal without 10% tip is: $", total_ind_2) #output of the subtotal

print("\n",name_2,"'s bill with 10% tip included is:$",total_2) #output of the total with 10% tip

print("--------------------------------------------------------")

#Person 3

name_3 = input("\nName: ") 

menu_item_3 = input("\nAmount of Lunch Menu Item: $")

amount_drink_3 = input("\nAmount of Drink: $")

total_ind_3 = float(menu_item_3) + float(amount_drink_3) #calculation of the items ordered

subtotal_3 = float(total_ind_3 * tip) #calculating the subtotal with the tip 

total_3 = float(total_ind_3 + subtotal_3) #total bill for the individual

print("\n", name_3,"'s subtotal without 10% tip is: $", total_ind_3) #output of the subtotal

print("\n",name_3,"'s bill with 10% tip included is:$",total_3)  #output of the total with 10% tip

print("--------------------------------------------------------")


#Calcuate total bill altogether 
subtotal_all = float(total_ind_1 + total_ind_2 + total_ind_3) #Calculate the bills togther without the 10% tip

total_all = float(subtotal_all * tip_all) #Calculating the 20% tip total

final_total_all = float(total_all + subtotal_all) # calculating the Final bill total

#output of the bills total 

print("Total Bill")

print("\nThe subtotal of the total bill before the 20% tip is: $",subtotal_all) #output of the subtotal without 20% tip

print("\nThe total bill is with 20% tip is: $", final_total_all) #output of the total with 20% tip
