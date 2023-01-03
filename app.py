# fruit = ["banana", "apple", "cherry"]
# print(fruit)
#############################################
# fruit[0] = "pear"
# fruit[-1] = "orange"
# print(fruit)
################################################
#einfügen
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = ['x', 'y']
# print(alist)
##############################################
#löschen an einer position
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = []
# print(alist)

############################################
### eine position einfügen
# alist = ['a', 'd', 'f']
# alist[1:1] = ['b', 'c']
# print(alist)
# alist[4:4] = ['e']
# print(alist)
############################################
##String'Buchstaben ersetzen
# greeting = "Hello, world!"
# newGreeting = 'J' + greeting[1:]
# print(newGreeting)
# print(greeting)          # same as it was
#############################################
#immer etwas hinzufügen
# phrase = "many moons"
# phrase_expanded = phrase + " and many stars"
# phrase_larger = phrase_expanded + " litter"
# phrase_complete = "M" + phrase_larger[1:] + " the night sky."
# excited_phrase_complete = phrase_complete[:-1] + "!"
#################################################
#mit /del/ löschen
# a = ['one', 'two', 'three']
# del a[1]
# print(a)

# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5]
# print(alist)
#################################################
## a is b = true
# a = "banana"
# b = "banana"

# print(a is b)
# #############################################
# a = "banana"
# b = "banana"

# print(id(a))
# print(id(b))
################################################
#a is b = false , a == b true
# a = [81,82,83]
# b = [81,82,83]

# print(a is b)

# print(a == b)

# print(id(a))
# print(id(b))
###################################################
##true
# a = [81, 82, 83]
# b = a
# print(a is b)
###################################################
###false,true,true, [5,82,83]
# a = [81,82,83]
# b = [81,82,83]
# print(a is b)

# b = a
# print(a == b)
# print(a is b)

# b[0] = 5
# print(a)
###################################################
## clonen der liste
# a = [81,82,83]

# b = a[:]       # make a clone using slice
# print(a == b)
# print(a is b)

# b[0] = 5

# print(a)
# print(b)

# b = ['q', 'u', 'i']
# z = b
# b[1] = 'i'
# z.remove('i')
# print(z)

# sent = "Holidays can be a fun time when you have good company!"
# phrase = sent
# phrase = phrase + " Holidays can also be fun on your own!"
# print(phrase)

# lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
# lst.remove('pluto')
# first_three = lst[:3]
# print(first_three)
# print(lst)

# x = ["dogs", "cats", "birds", "reptiles"]
# y = x
# x += ['fish', 'horses']
# y = y + ['sheep']
# print(x)
# print (y)

# sent = "The mall has excellent sales right now."
# wrds = sent.split()

# wrds[1] = 'store'
# new_sent = " ".join(wrds)


# print(new_sent)
##############################################################
##Manipulation der Liste
# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
# print(mylist)

# mylist.insert(1, 14)
# print(mylist)
# print(mylist.count(12))

# print(mylist.index(3))
# print(mylist.count(5))

# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# mylist.remove(5)
# print(mylist)

# lastitem = mylist.pop()
# print(lastitem)
# print(mylist)

####################################################################
##liste ergänzen
# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
# print(mylist)

# mylist = mylist.sort()   #probably an error
# print(mylist)
###################################################################
# origlist = [45,32,88]
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list before changes
# newlist = origlist + ['cat']
# print("newlist:", newlist)
# print("the identifier:", id(newlist))              #id of the list after concatentation
# origlist.append('cat')
# print("origlist:", origlist)
# print("the identifier:", id(origlist))             #id of the list after append is used
############################################################################
##['W', 'a', 'r', 'm', 't', 'h']
# st = "Warmth"

# a = []
# b = a + [st[0]]
# c = b + [st[1]]
# d = c + [st[2]]
# e = d + [st[3]]
# f = e + [st[4]]
# g = f + [st[5]]
# print(g)
###########################################################################
# st = "Warmth"
# a = []
# a.append(st[0])
# a.append(st[1])
# a.append(st[2])
# a.append(st[3])
# a.append(st[4])
# a.append(st[5])
# print(a)
########################################################################
###upper+lower
# ss = "Hello, World"
# print(ss.upper())

# tt = ss.lower()
# print(tt)
# print(ss)
#######################################################################
##ersetzen
# ss = "    Hello, World    "

# els = ss.count("l")
# print(els)

# print("***"+ss.strip()+"***")

# news = ss.replace("o", "***")
# print(news)
########################################################################
# name = "Rodney Dangerfield"
# score = -1  # No respect!
# print("Hello " + name + ". Your score is " + str(score))
#######################################################################
# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello " + name + ". Your score is " + str(score))
#######################################################################
# scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
# for person in scores:
#     name = person[0]
#     score = person[1]
#     print("Hello {}. Your score is {}.".format(name, score))

####################################################################
##ausgabe
# person = input('Your name: ')
# greeting = 'Hello {}!'.format(person)
# print(greeting)
###################################################################
# person = input('Enter your name: ')
# print('Hello {}!'.format(person))

#################################################################
# origPrice = float(input('Enter the original price: $'))
# discount = float(input('Enter discount percentage: '))
# newPrice = (1 - discount/100)*origPrice
# calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
# print(calculation)

# origPrice = float(input('Enter the original price: $'))
# discount = float(input('Enter discount percentage: '))
# newPrice = (1 - discount/100)*origPrice
# calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
# print(calculation)
# name = "Sally"
# greeting = "Nice to meet you"
# s = "Hello, {}. {}."

# print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

# print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

# print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.

# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# sports.remove(3)
# trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
# trav_dest.remove('London')
# print(trav_dest)

# nums = [3,5,8]
# accum = []
# for w in nums:
#     x= w**2
#     accum.append(x)
#     print(accum)

# lst= [3,0,9,4,1,7]
# new_list=[]
# for i in range(len(lst)):
#    new_list.append(lst[i]+5)
# print(new_list)


# verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

# newlist = []

# for i in verbs:
    
#     newlist.append(i + "ing")
    
# print (newlist)

# lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]


# list=[]
# for i in lst_nums:
    
#     list.append(i**2)
#     print(list)a = ["holiday", "celebrate!"]


# s = input("Enter some text")
# ac = ""
# for c in s:
#     ac = ac + c + "-" + c + "-"

# print(ac)


# byzo = 'hello world!'
# c = 0
# for x in byzo:
#     z = x + "!"
#     print(z)
#     c = c + 1

# cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
# t = 0
# for elem in cawdra:
#     t = t + len(elem)
    
# print(t)

# Derzeit gibt es eine Zeichenfolge namens str1. 
# Schreiben Sie Code, um eine Liste mit dem Namen zu erstellen, chars die die Zeichen von enthalten sollte str1.
# Jedes Zeichen in str1 sollte ein eigenes Element in der Liste sein chars.

# str1 = "I love python"
# # HINT: what's the accumulator? That should go here.
# chars = []
# for x in str1:
    
#     chars += x

# print(chars)

# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

# for color in colors:
#     print(color)
#####['R', 'O', 'Y', 'G', 'B', 'I', 'V']
# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
# initials = []

# for color in colors:
#     initials.append(color[0])

# print(initials)
# lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
# lst.remove('pluto')
# first_three = lst[:3]

# print(first_three)

# nums = [4, 5, 2, 93, 3, 5]
# s = 0
# for n in nums:
#     s = s + n
# print(s)    

# lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
# s = 0
# for item in lst:
#     if type(item) == type("string"):
#         s = s + 1
# print(s)
#############################['p', 'y', 't', 'h', 'o', 'n', '!']
# ael = "python!"
# app = []
# for i in ael:
#     app.append(i)
    
# print(app)

# a = ["holiday", "celebrate!"]
# quiet = a
# quiet.append("company")
# print(quiet)

# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# scores_split = scores.split(" ")
# a_scores = 0
# for x in scores_split:
#     x = float(x)
#     if x >= 90:
#         a_scores += 1

# print(a_scores)

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"

# stopwords = set(w.upper() for w in stopwords)
# acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)

# print(acro)
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"

# acro=""

# orglist=org.split()

# for firstw in orglist:
#     if firstw not in stopwords:
#         acro=acro+firstw[0].upper()
# print(acro)

# p_phrase = "was it a car or a cat I saw"


# phrase= p_phrase[::-1]
   
# print(phrase)print(i)
# for item in inventory:
#     item_desc, number, cost = item.split(", ")
#     print("The store has {} {}, each for {} USD.".format(number, item_desc, cost))


#stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
#org = "The water earth and air are vital"
#acro=""
#orgli=org.split()
#for i in orgli:
#    if i not in stopwords:
        #
        #acro+=' .'.join(i[:2].upper())
        #print(acro)


