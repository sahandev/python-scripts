##enter user inputs and convert to capital
name = input("enter your name: ")
age = input("enter your age: ")

print("Hello " +name+ " \n your age is "+age)
print("WELCOME TO THE SYSTEM "+name.upper())

##replace tuple value from user input
friends= ["sahan", "jazz", "lak"]
print(friends)

new_friend = input("enter another name to replace tupple 2nd name: ")
friends [2] = new_friend
print(friends)