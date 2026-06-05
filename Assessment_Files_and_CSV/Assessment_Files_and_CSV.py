# 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
# Output: 316
file_obj = open("travel_plans.txt", 'r')
num = 0

data = file_obj.read()
num = len(data)
    
print(num)
file_obj.close()

# 2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
# Find the total number of words in the file and assign this value to the variable num_words.
# Output: 48
file_obj = open("emotion_words.txt", 'r')
num_words = 0

for word in file_obj.readlines():
    values = word.split()
    for i in values:
        num_words += 1
    
print(num_words)
file_obj.close()

# 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.
# Output: 10
file_obj = open("school_prompt.txt", 'r')
num_lines = 0

for lines in file_obj.readlines():
    num_lines += 1
    
print(num_lines )
file_obj.close()


# 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
# Output: Writing essays for school can 
file_obj = open("school_prompt.txt", 'r')
beginning_chars = ""

beginning_chars = file_obj.read()[:30]
print(beginning_chars)

file_obj.close()


# 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
# Output: ['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,']
file_obj = open("school_prompt.txt", 'r')
three = []

for word in file_obj.readlines():
    values = word.split()
    three.append(values[2])
                 
print(three)
file_obj.close()


# 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
# Output: ['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous']
file_obj = open("emotion_words.txt", 'r')
emotions = []

for first in file_obj.readlines():
    values = first.split()
    emotions.append(values[0])
    
print(emotions)
file_obj.close()



# 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
# Output: This summer I will be travelling.
file_obj = open("travel_plans.txt", 'r')

first_chars = file_obj.read(33)
print(first_chars)

file_obj.close()



# 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
# Oupput: ['topic', 'point', 'papers,', 'ups,', 'scripts.']
file_obj = open("school_prompt.txt", 'r')
words = file_obj.read().split()

p_words = []
for w in words:
    if 'p' in w:
        p_words.append(w)

print(p_words)
file_obj.close()

