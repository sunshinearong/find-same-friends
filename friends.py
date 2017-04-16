from linked_list import *#import class 

filename = raw_input('Input file: ')#input filename
name1 = raw_input('Name 1: ')
name2 = raw_input('Name 2: ')
try:
    f= open(filename,'r')
except Exception,e:
    print("ERROR: Could not open file " + filename)#catch exception
link = LinkedList(None)#init a node
for line in f.readlines():
    names = line.split()#split line
    first = names[0] #first name
    second = names[1]#second name
    link_temp = link#copy first node
    while(link):
        if link._name == first:#first already exists
            link.add_friend(LinkedList(second))#second is a friend of first
            break
        if link._next == None:# not found first name
            link._next = LinkedList(first)#append first name to list
            link._next.add_friend(LinkedList(second))#second is a friend of first
            break
        link = link._next
    link=link_temp#change link to beginning
    link_temp = link
    while(link):
        if link._name == second:#second name already exists
            link.add_friend(LinkedList(first))#first is a friend of second
            break
        if link._next == None:#append second name to list
            link._next = LinkedList(second)
            link._next.add_friend(LinkedList(first))
            break
        link = link._next
    link=link_temp
link = link._next
link_temp = link
name1_friends = -1#flag to know whether name1 exists
name2_friends = -1#flag to know whether name2 exists
while link:
    if link._name == name1:#find name1
        name1_friends = link._friends#find name1 friends
    if link._name == name2:#find name2
        name2_friends = link._friends#find name2 friends
    link = link._next
assert name1_friends != -1 and name2_friends != -1#assert name1 and name2 exist
while name1_friends:
    name2_friends_temp = name2_friends
    while name2_friends:
        if name1_friends._name == name2_friends._name:#share one friend
            print(name1_friends._name)
            break
        name2_friends = name2_friends._next
    
    name2_friends = name2_friends_temp
    name1_friends = name1_friends._next
