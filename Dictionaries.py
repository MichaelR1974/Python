# Dictionaries anlegen
#eng2sp = {}
#eng2sp['one']= 'uno'
#eng2sp['two']= 'dos'
#eng2sp['three'] = 'tres'


###################################################################################################################
## Zusammen gefügte Dic
#eng2sp = {'three':'tres', 'two':'dos', 'one':'uno'}
#value = eng2sp['two']
#print(value)


#print(eng2sp['one'])
###################################################################################################################

#mydic = {'cat':12, 'dog':6, 'elephant':23}
#print(mydic['dog'])

###################################################################################################################
###Alle Möglichkeiten Werte zuzuweisen
#olympics = {'gold': 7}
#olympics["silver"] = 8
#olympics['bronze'] = 6
###################################################################################################################
#places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
#places1 = {'Brazil':2016}
#places.update(places1)
###################################################################################################################
## löschen eines Elements

#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#del inventory['pears']
#print(inventory)
###################################################################################################################
##Update eines Elements
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#inventory['pears'] = 0
#print(inventory)
###################################################################################################################
##Zusammen Rechnen von Werten eines Objects
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#inventory['bananas'] = inventory['bananas'] + 200
	
#numItems = len(inventory)
#print(inventory)
###################################################################################################################
#Zeigt alle Werte und Elemente

#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#for key in inventory.keys():
#    print(key, 'has the value', inventory[key])
    
#keys = list(inventory.keys())
#print(keys)
##################################################################################################################
#Zeigt nur die Elemente
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#for key in inventory:
#    print('Got key', key)
##################################################################################################################

## values und items Ausgabe 
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#print(list(inventory.values()))
#print(list(inventory.items()))

#for k in inventory:
#    print('Got',k,'that maps to', inventory[k])
##################################################################################################################
## True,False,312
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#print('apples' in inventory)
#print('cherrys' in inventory)

#if 'bananas' in inventory:
#    print(inventory['bananas'])
#else:
#    print('We have no bananas')
###################################################################################################################
#430,Done,0
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#print(inventory.get('apples'))
#print(inventory.get('cherry'))
#print(inventory.get('cherry',0)) // Cherry vorhanden dann den Inhalt da von ansonsten den zweiten Wert

###################################################################################################################
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#for akey in inventory.keys():     # the order in which we get the keys is not defined
#    print("Got key", akey, "which maps to value", inventory[akey])

#ks = list(inventory.keys())       # liste aller Objekte
#print(ks)
#print(ks[0])                      # Display the first key
###################################################################################################################
##
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#for k in inventory:
#    print("Got key", k)
###################################################################################################################
##Zeigt alle Werte
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#print(list(inventory.values()))

#for v in inventory.values():
#    print("Got", v)
####################################################################################################################
#Zeigt alle Daten seperat
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#print(list(inventory.items()))

#for k, v in inventory.items():
#    print("Got", k, "that maps to", v)
####################################################################################################################
#Ortnet nach Aphabet
#medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
#events = list(medal_events.keys())
####################################################################################################################
#update Element
#opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
#alias = opposites

#print(alias is opposites)

#alias['right'] = 'left'
#print(opposites['right'])
####################################################################################################################


###########################Dictionary Accumulation##################################################################
### Text wird nach dem Buchstaben 't' durchsucht
#f = open('scarlet.txt','r')
#txt = f.read()

#t_count = 0
#for c in txt:
#    if c == 't':
#        t_count = t_count + 1
#print('t:' + str(t_count))
# == t: 17584 occurrences
####################################################################################################################
#
#f = open('scarlet.txt','r')
#txt = f.read

#t_count = 0
#s_count = 0

#for c in txt:
#    if c == 't':
#        t_count = t_count + 1
#    elif c == 's':
#        s_count = s_count + 1
#print('t: ' + str(t_count))
#print('s: ' + str(s_count))

## == t: 17584 occurrences
## == s: 11830 occurrences
############alternativ###############################################################################################
#Zählen von t und s gleichzeitig

#f = open('scarlet.txt','r')
#txt = f.read

#x = {}
#x['t']
#x['s']

#for c in txt:
#    if c == 't':
#        x['t'] = x['t'] +1
#    elif c == 's':
#        x['s'] = x['s'] +1
#print('s: ' + str(x['t']))
#print('s: ' + str(x['s']))

####################################################################################################################
#f = open('scarlet.txt','r')
#txt = f.read

#x = {}
#for c in txt:
#    if c not in x:
#        x[c] = 0
#    x[c]= x[c] +1
#print('s: ' + str(x['t']))
#print('s: ' + str(x['s']))

#####################################################################################################################
## Gibt alle Buchstaben in Anzahl aus
#f = open('scarlet.txt', 'r')
#txt = f.read()
#letter_counts = {}
#for c in txt:
#    if c not in letter_counts:
#        letter_counts[c] = 0

#    letter_counts[c] = letter_counts[c] + 1

## Write a loop that prints the letters and their counts
#for c in letter_counts.keys():
#    print(c + ": " + str(letter_counts[c]) + " occurrences")
#####################################################################################################################

##teilen Sie die Zeichenfolge sentencein eine Liste von Wörtern auf und erstellen Sie dann ein Wörterbuch mit dem Namen word_counts, 
#das jedes Wort und die Häufigkeit, mit der es vorkommt, enthält.

#sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

#words=[]
#word_counts={}

#for i in sentence.split():
#     words.append(i)
#for c in words:
#      if c not in word_counts:
#             word_counts[c] = 0
#      word_counts[c] = word_counts[c] + 1   
#####################################################################################################################
##Erstellen Sie ein Wörterbuch namens char_d. Die Schlüssel des Wörterbuchs sollten jedes Zeichen in sein stri, 
#und der Wert für jeden Schlüssel sollte sein, wie oft das Zeichen in der Zeichenfolge vorkommt.

#char_d={}
#for c in stri:
#      if c not in char_d:
#             char_d[c] = 0
#      char_d[c] = char_d[c] + 1
#####################################################################################################################

#f = open('scarlet.txt','r')
#txt= f.read()

#letter_counts = {}
#for c in txt:
    
#        if c not in letter_counts:
            
#            letter_counts[c] = 0

#        letter_counts[c] = letter_counts[c] + 1
#print(letter_counts['t'])
#####################################################################################################################
#zeigt alle einträge

#f = open('scarlet.txt','r')
#txt= f.read()

#letter_counts = {}
#for c in txt:
    
#     if c not in letter_counts:
            
#        letter_counts[c] = 0

#     letter_counts[c] = letter_counts[c] + 1

#for y in letter_counts:
#    print("There are",letter_counts['y'],"'","'s")
#####################################################################################################################
##Standard Accumulator #### Wichtig!!!!
#f = open('scarlet.txt','r')
#txt= f.read()

#letter_counts = {}
#for c in txt:
    
#     if c not in letter_counts:
            
#        letter_counts[c] = 0

#     letter_counts[c] = letter_counts[c] + 1

#######################################################################################################################
#f = open('scarlet.txt','r')
#txt= f.read()

#x = {}
#for c in txt:
    
#     if c not in x:
            
#        x[c] = 0

#     x[c] = x[c] + 1

###### Ausgabe mit Loop
#letter_value ={} #irgengwelche Werte z.b: {'a': 1,.......}
#scrabble_score = 0
#for y in x:
#    if y in letter_value:
#        scrabble_score = scrabble_score + letter_value[y] * x[y]

#################################################################################################################
# alle Werte in Travel der Continente zusammengerechnet
#travel = {'NA':2, 'E':8,'SA':3,'A':6}
#total = 0
#for continent in travel:
#    total = total + travel[continent]

#print(total)

#################################################################################################################
### erste Teil wird die Zeichenfrequenz erstellt und dann nach dem kleinsten Wert gesucht
#placement = ""

#d = {}

#for c in placement:
#    if c not in d:
#        d[c] = 0
#    d[c] = d[c] + 1

#keys = list(d.keys())
#min_value = keys[0]

#for key in keys:
#    if d [key] < d[min_value]:
#        min_value = key
#################################################################################################################


#str1 = "I wish I wish with all my heart to fly with dragons in a land apart"




#freq_words = {}
#for c in str1:
#    if c not in freq_words:
#        freq_words[c] = 0
#    freq_words[c] = freq_words[c] + 1

#for y in str1:
#    if y in str1:
#      freq_words =  freq_words + str1[y] 


#sally = "sally sells sea shells by the sea shore"

#characters={}

#for c in sally:
    
#    if c not in characters:
            
#        characters[c] = 0

#    characters[c] = characters[c] + 1

#keys = list(characters.keys())
#best_char = keys[0]

#for key in keys:
#    if d [key] > characters[best_char]:
#        best_char = key
#print()

#p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
#p = p.lower()

#low_d = {}
#for c in p:
#    if c not in low_d:
#        low_d[c] = 0
#        low_d[c] = low_d[c] + 1
#print(low_d)