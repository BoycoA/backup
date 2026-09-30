drinks = ["tea", "coffee", "water"]
chosen_drink = drinks[1]
print(chosen_drink)
print(len(drinks))

# 1. What does each print statement display? Explain why drinks[1] selects that drink.
# Your answer:
## print (chosen_drink) will print "coffee", because:
### chosen_drink is the elemento [1] in the list "drinks"
### and python is 0 based index, thus the element [1] is the second element
## print (len(drinks)) will print "3", because:
### there are three elements in the list, and the length shows this

# 2. What are the Python types of drinks and chosen_drink?
# Your answer:
## drinks is a list
## chosen_drinks would be a string