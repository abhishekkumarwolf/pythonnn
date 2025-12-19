'''
create a new file "Practice.txt" using python. Add the following data in it:
Hi Every one
we are learning File I/o
using java
i like progamming in java

Write a function that replace occurance of java with python in above file
search if word learning exist in the file or not
'''

import os


with open("practice.txt", "w") as f:
    f.write(" Hi Everyone\nwe are learning File I/O\nusing java\ni like programming in java")

def word_replace():
    with open("practice.txt", "r") as f:
        content = f.read()

    content = content.replace("java", "Python")

    with open("practice.txt", "w") as f:
        f.write(content)

word_replace()

def word_search():
    with open("practice.txt", "r") as f:
        content = f.read()

        if  "learning" in content:
            return "Yes exist"
        else :
            return "Dont exist"
print(word_search())