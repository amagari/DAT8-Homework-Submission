import csv
## Question 1
file_nested_list = []  

with open(r"c:\users\ben\documents\dat8\data\chipotle.tsv", "rU") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        file_nested_list.append(row)

#part 2
header = file_nested_list[0]

data = file_nested_list[1:]

## Part 3
## extracting the order ID number
orderId = []
for order in data:
    orderId.append(order[0])

## extracting the individual prices for each component of each order
itempriceorder = []
for price in data:
    x = price[4].replace("$", "")    
    itempriceorder.append(float(x))

# Calculating average by dividing sum of food prices by the length of the set 
# of order numbersm which only allow ones unique value of each value, giving
# the total orders. Also the Quantity column does matter because it will
# increase the average cost but I ignored it because I was working with the
# other aspects of the problem so far.  
    
averageprice = (sum(itempriceorder)) / len(set(orderId))
print(averageprice)

# Part 4. I pulled out all the occurrences of "canned" and then stuck them into
# a list and then printed the list as a set, since sets only allow unique values
# giving the total number of unique canned drinks.

uniqueCanneddrinks = []
for canneddrinks in data:
    if "canned" in canneddrinks[2].lower():
        uniqueCanneddrinks.append(canneddrinks[3])
        
print(set(uniqueCanneddrinks))


# Part 5. I used the occurence of commas in each line to calculate the number
# of toppings and added a 1 for the trailing item. and used the else statement
# for burritos with only one topping and therefore no commas
totaltoppings = []
for toppings in data:
    if "burrito" in toppings[2].lower():
        if "," in toppings[3]:
            z = toppings[3].count(",")
            totaltoppings.append(z + 1)
        else:
            totaltoppings.append(1)

totalburritos = []
for burrito in data:
    if "burrito" in burrito[2].lower():
        totalburritos.append(1)

averageburritotoppings = sum(totaltoppings) / sum(totalburritos)
print(averageburritotoppings)
    
## Part 6
    ## separting out the quantity and numbers of chip orders into separate
    ## lists

dictionaryofchiporders = {}
typesofchiporders = []
quantityofchiporders = []
for i in data:     
    if "chips" in i[2].lower():  ##Filterinng out all the chips items from data
        typesofchiporders.append(i[2]) ## Appending the types of chips list
        changetoint = int(i[1]) #making the values into ints
        quantityofchiporders.append(changetoint)  ## appending to the number of
        ## chips ordered list
## Now have two separete lists of equal length with the types of chips and their quantities

## combining the two lists into a diciontionary item and appending to dict
for types in typesofchiporders:  # using nested lists be able to combine both
    for quantity in quantityofchiporders:  #lists at the same time
        if types in dictionaryofchiporders.keys(): #check membership to avoid
        ## a key error when I tried to update the dict the first time around
            amalgam = {types: (dictionaryofchiporders.get(types) + quantity)} ##adding the previous entry            
            dictionaryofchiporders.update(amalgam)
            break  #amalgam varible combines both type of order and quantit
            #into one dict entry.
        else:
            amalgam = {types: quantity}            
            dictionaryofchiporders.update(amalgam)
            break
        
        
        
        
    
    
    


        
    


    


        
        
    
        
            
    





    


        


    



