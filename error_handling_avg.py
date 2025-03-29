count = 0 
total = 0


while True:
    user_input = input("Enter a number (or done to end the program) : ")
    
    
    if user_input.lower() == "done":
        break
    try:
        
        value_enetered = float(user_input)
        count += 1
        total += value_enetered
        
    except:
        print("You have eneterd an invalid input, please try again")
        
print(f"count = {count}, total = {total}, average = {round(total/count,2) if count > 0 else "N/A"}")
print("You have successfully finished your calculation")
    
    
    
    