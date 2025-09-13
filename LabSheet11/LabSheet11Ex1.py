sentence = "I love programming in Python"
is_present = "Python" in sentence 
if is_present == True:
    print("This word is present")
    newsentence=sentence.replace("Python","Java")
    print(newsentence)
else:
    print("This word is not present")