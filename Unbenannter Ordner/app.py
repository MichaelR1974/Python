# import turtle
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.forward(150)
# alex.left(55)
# alex.forward(150)
# alex.left(55)
# alex.forward(150)
# alex.left(55)
# alex.forward(150)
# alex.left(55)
# alex.forward(150)
# # zwei
# import turtle
# wn = turtle.Screen()             # Set up the window and its attributes
# wn.bgcolor("lightgreen")


# tess = turtle.Turtle()           # create tess and set his pen width
# tess.pensize(5)

# alex = turtle.Turtle()           # create alex
# alex.color("hotpink")            # set his color

# tess.forward(80)                 # Let tess draw an equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                   # complete the triangle

# tess.right(180)                  # turn tess around
# tess.forward(80)                 # move her away from the origin so we can see alex

# alex.forward(50)                 # make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# wn.exitonclick()
# # Loop
# import turtle
# wn = turtle.Screen()

# elan = turtle.Turtle()

# distance = 50
# for _ in range(10):
#     elan.forward(distance)
#     elan.right(90)
#     distance = distance + 10
    
    # Turtles
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.color("blue")
# tess.shape("turtle")

# dist = 5
# tess.up()                     # this is new
# for _ in range(30):    # start with size = 5 and grow by 2
#     tess.stamp()                # leave an impression on the canvas
#     tess.forward(dist)          # move tess along
#     tess.right(24)              # and turn her
#     dist = dist + 2
# wn.exitonclick()
# school = "Luther College"
# print(school[-3])

# lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]

# output=(len(lst))
# print(output)
# s ="python rocks"
# print(s[:])
# new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
# sub_lst = new_lst[8:12]
# print(sub_lst)
# song = "The rain in Spain"
# wds = song.split("i")
# print(wds)

# lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
# output = lst[5:13]
# print(output)
# let = "z"
# let_two = "p"
# c = let_two + let
# m = c*5
# print(m)


# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# last = sports[ 6:]
# print(last)
# ls = ['run','world','travel','lights','moon', 'baseball', 'sea']

# new = ls[2:7]
# print(new)
# b = "My, what a lovely day"
# x = type(b.split(','))
# print(x)

# b = "My, what a lovely day"
# x = b.split(',')
# z = "".join(x)
# y = z.split()
# a = "".join(y)
# print(type(a))
# 
# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']


# last = (sports[-3:])
# print(last)

# for name in["Michael","Claudi"]:
#     print("Hi",name,"Please come")

# print("This will execute first")

# for __ in range(3):
#     print("This line will execute three times")
#     print("This line will also execute three times")

# print("Now we are outside of the for loop!")

# nums = [1,2,3,4,5,6,7,8,9,10]
# accum = 0
# for w in nums:
#     print(nums)
#     print(w)
#     print(accum)
#     accum += w
# print(accum)
# 


# str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
# numbs = str1.count('')-1
# print(numbs)
# sum1 = 0
# numbers=(list(range(0,41)))
# for w in numbers:
#     sum1 += w



# several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

# for i in several_things: 
#     print(i)
    
#     print(type(i))
   
# str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
# for i in str_list:
#     print(len(i))

# from collections import Counter


# original_str = "The quick brown rhino jumped over the extremely lazy fox."
# tot = 0
# for num in original_str:
#     print (num)
#     tot= len(original_str)
# print(tot)
# sum_val = 0
# sum = 0
# addition_str = "2+5+10+20"

# sum_vale = addition_str.split("+")
# sum = list(map(int,sum_vale))


# for number in sum:
#     sum_val += number

# print(f"{sum_val}")




# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
# avg_temp=  [float(value) for value in week_temps_f.split(',')]







# print(str(len(avg_temp)))
# nums = range(0,67)
# print(type(list(nums)))count"

# num_words_list= original_str.split()

# print(num_words_list)

# lett = ''
# for i in range(7):
#     lett += 'b'
    
#     print(lett)

# count = 0
# original_str = "The quick brown rhino jumped over the extremely lazy fox."
# for num_chars in original_str:
#     count += 1
    
# print(count)
# import turtle
# turtle.bgcolor('black') 
# turtle.color('yellow')
# turtle.width(10)
# turtle.begin_fill()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.color('orange')
# turtle.end_fill()
# ws= turtle.Screen()
# ws.title("Python guides")
# turtle.speed(6)
# turtle.color('green', 'pink')

# while True:
#     turtle.forward(200)
#     turtle.left(150)
#     if abs(turtle.pos()) < 1:
#         break

# ws.exitonclick()

# import turtle
# wn = turtle.Screen()

# amy = turtle.Turtle()
# amy.pencolor("Pink")
# amy.forward(50)
# if amy.pencolor() == "Pink":
#     amy.right(60)
#     amy.forward(100)
# else:
#     amy.left(60)
#     amy.forward(100)

# kenji = turtle.Turtle()
# kenji.forward(60)
# if kenji.pencolor() == "Pink":
#     kenji.right(60)
#     kenji.forward(100)
# else:
#     kenji.left(60)
#     kenji.forward(100)

# import turtle
# wn = turtle.Screen()

# amy = turtle.Turtle()
# amy.pencolor("Pink")
# amy.right(170)

# colors = ["Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Orange", "Pink", "Pink", "Orange", "Yellow", "Purple", "Orange", "Purple", "Yellow", "Orange", "Pink", "Orange", "Purple", "Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Yellow"]


# for color in colors:
#     if amy.pencolor() == "Purple":
#         amy.forward(50)
#         amy.right(59)
#     elif amy.pencolor() == "Yellow":
#         amy.forward(65)
#         amy.left(98)
#     elif amy.pencolor() == "Orange":
#         amy.forward(30)
#         amy.left(60)
#     elif amy.pencolor() == "Pink":
#         amy.forward(50)
#         amy.right(57)

#     amy.pencolor(color)

# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
# avg =  [float(value) for value in week_temps_f.split(',')]
# print (type(avg[0]))


# avg_temp = sum(avg)/len(avg)
# print(avg_temp)

# print('i' in 'in')
# print('l' not in 'in')

# print(18 / 4)

# courses = ["ENGR 101", "SI 106"]

# if "SI 106" in courses:
#    print("You can SI")
# else:
#     print ("Take SI 106!")
    
# Erstellen Sie eine Variable, b  und weisen Sie ihr den Wert zu 15.
# Schreiben Sie dann Code, um zu sehen, ob der Wert bgrößer als der von ist a.
# Ist dies der aFall, sollte der Wert von mit 2 multipliziert werden. 
# Wenn der Wert von bkleiner oder gleich ist a, sollte nichts passieren.
# Erstellen Sie schließlich eine Variable cund weisen Sie ihr den Wert der Summe von aund zu b.


# a = 20
# b = 15


# if a < b :
#     a *2
    
# c = a + b
# print(c)

# if "false" in str1:
#     output("False You aren")
# elif "true" in str1:
#     output("True")
# else:
#     output = "Neither"

# percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
# for element in percent_rain:
#     if  element >= 90  :
#         resps = "Bring an umbrella"
#         print(resps)
#     elif  element >= 80 :
#         resps = "Good for the flowers?"
#         print(resps)
#     elif element > 50 :
#         resps = "Watch out for clouds!’"
#         print(resps)
#     else:
#         resps = "Nice day!"    
#         print(resps)

# nums = [9, 3, 8, 11, 5, 29, 2]
# best_num = nums[0]
# for n in nums:
#     if n > best_num:
#         best_num = n
# print(best_num)

# phrase = "What a wonderful day to program"
# tot = 0
# for char in phrase:
#     if char != " ":
#         tot = tot + 1
# print(tot)

# s = "what if we went to the zoo"
# x = 0
# for i in s:
#     if i in ['w']:
#         x += 1
# # 
# print(x)

# Ermitteln Sie für jede Zeichenfolge in der Liste words
# die Anzahl der Zeichen in der Zeichenfolge.
# Wenn die Anzahl der Zeichen in der Zeichenfolge größer als 3 ist, 
# addieren Sie 1 zur Variablen num_words, 
# sodass num_wordsdie Gesamtzahl der Wörter mit mehr als 3 Zeichen erhalten werden sollte.

# words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# items1= ''.join(items)
# same_letter_count = 0
# for char in items1:
#   if char == 'w':
#     same_letter_count = same_letter_count + 1
  
# print (same_letter_count)

# words = ["water", "chair", "pen", "basket", "hi", "car"]
# num_words = 0
# for i in words:
#     if len(i) > 3:
#         num_words += 1


# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

# for items in "w":
#     print (items)
# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

# for i in rainfall_mi:
#      if len(i) > 3.0:
#         num_rainy_months = i
        
# print(i) 

# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# items1= ''.join(sentence)
# same_letter_count = 2
# for char in items1:
#     if char == 'w':
#         same_letter_count = same_letter_count + 1
#         print(items1)