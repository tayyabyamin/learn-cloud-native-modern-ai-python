motorcycles:list[str] = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

# .remove is used to remove the variable in this case too_expensive from the variable list motorcycles 

motorcycles.remove(too_expensive)
print(motorcycles)

# f is formatted strings. It allows you to embed expressions or variables inside curly braces {} directly within a string, and Python automatically evaluates and inserts the result.
# here using f (formatted strings), python will replace the {too_expensive.title()} with its value
# \n is used for adding a new line. while A is just the first letter of the sentence.

print(f"\nA {too_expensive.title()} is too expensive for me.")
