#Exception is error encountered during program running

try: # is for testing
    print(number)

except:
    print("An Error Occured")

num1 = 39
num2 = 0
try:
    print(num1 / num2)

except: #printing or caching the error
    print("ZeroDivisionError has Occured")

finally: # is used to execute
    print("success")