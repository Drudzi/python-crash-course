
#if x: -----> If x is True, do something. If x is False, ignore the intended part and continue.
    #do something

age = 20
if age >= 18:
    print("You're old enough to drink alcohol")
    print("What would you like?")
else: #Catchall statement!
    print("You are not old enough!") #Else statements are executed when all conditional tests fail.
    print("Sorry, you might want a coke instead?")

print()

age = 12
if age < 4:
    print("Admmision cost: $0.")
elif age < 18: 
    print("Admission cost: $25.")
else:
    print("Admission cost: $40.")

#A more concise and practical way to do the above:
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: #Added extra elif block.
    price = 40
elif age >= 65: #You don't need to finish with else, sometimes its more specific with elif.
    price = 20 
#else:
    #price = 20 #If above 65, price is 50% off.
print(f"Admission cost: ${price}.")
print()
#IF-ELIF-ELSE let's only one test to pass.
#Sometimes you want to test all conditions of interest, then you can use only if-statements without any elifs or elses.
#Runs regardless of whether the previous test passed or not. Makes sense when more than one condition could be True.

#Checking multiple conditions:
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings: #if after if runs regardless of what happened previously.
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings: #If it would have been if-elif-elif, the elifs wouldn't have been passed because first if cancels chain if True.
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print()
#Use if-elif-else if you only want one block to run.
#Use if-series if you want more blocks to run.

#5-6. Stages of Life:
age = 69
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")