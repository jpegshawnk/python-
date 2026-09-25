num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
print("1 for +,2 for -, 3 for *, 4 for /") 
op = input()
if op =="1" :
    answer1 = num1 + num2 
elif op ==  "2" :
answer2 = num1 - num2 
elif op ==  "3" :
answer3 = num1 * num2
elif op ==  "4" :
answer4 = num1 / num2
else:
answer = "Invalid chioce"
print(answer) 
