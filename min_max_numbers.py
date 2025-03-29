#Write a program that repeatedly prompts a user for integer numbers until the user enters
#'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except.


            
largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num.lower() == "done":
        break 

    try:
        rnum = int(num)
    except ValueError:
        print("Invalid input")
        continue  

    if largest is None or rnum > largest:
        largest = rnum
    if smallest is None or rnum < smallest:
        smallest = rnum

print("Maximum", largest)
print("Minimum", smallest)
        
