# this is a numerical variable
types_of_people = 10

# another string variable with a numerical variable in it
x = f"There are {types_of_people} type of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}.")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side off.."
e = "a string with a right side."

print (w+e)
