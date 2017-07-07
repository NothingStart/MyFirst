#print('Hello World')
#s = 5
#print(s)
#s = s + 1
#print(s)
#ss = '''My Name is\
#
#Zhang Xing'''
#if 2 != 2:
    #print('2')
#elif 2==3:
    #print('3')
#else :
    #print('123')


#listTest = [1,1,3,4,5,6,'a','bb',4,[1.2,3]]
#print(listTest)

#元祖 --不可变的数组
print('1\ %s is name %d'% ('name',2))

#字典
ab = { 'Swaroop' : 'swaroopch@byteofpython.info',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}

for name, address in ab.items():
    print ('Contact %s at %s' % (name, address))
if 'Larry' in ab: # OR ab.has_key('Larry')
    print ("\nLarry's address is %s" % ab['Larry'])

#序列
shoplist = ['apple', 'mango', 'carrot', 'banana']
# Indexing or 'Subscription' operation
print ('Item 0 is', shoplist[0])
print ('Item 1 is', shoplist[1])
print ('Item 2 is', shoplist[2])
print ('Item 3 is', shoplist[3])
print ('Item -1 is', shoplist[-1])
print ('Item -2 is', shoplist[-2])
# Slicing on a list
print ('Item 1 to 3 is', shoplist[1:3]      )
print ('Item 2 to end is', shoplist[2:]     )
print ('Item 1 to -1 is', shoplist[1:-1]    )
print ('Item start to end is', shoplist[:]  )
# Slicing on a string
name = 'swaroop'
print ('characters 1 to 3 is', name[1:3]     )
print ('characters 2 to end is', name[2:]    )
print ('characters 1 to -1 is', name[1:-1]   )
print ('characters start to end is', name[:] )

# 深拷贝 浅拷贝 深复制 浅复制
print ('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!
del shoplist[0]
print ('shoplist is', shoplist)
print ('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object
print ('Copy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item
print ('shoplist is', shoplist)
print ('mylist is', mylist)
# notice that now the two lists are different

#字符串对象
name = 'swaroop'
if name.startswith('Swa'):
    print ('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print ('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print (delimiter.join(mylist))


import os
import time
# 1. The files and directories to be backed up are specified in a list.
source = ['/home/swaroop/byte', '/home/swaroop/bin']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory
target_dir = 'C:/' # Remember to change this to what you will be using
# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print ('Successfully created directory', today)
# The name of the zip file
target = today + os.sep + now + '.zip'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')



class Person:
    '''Represents a person.'''
    population = 0
    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print ('(Initializing %s)' % self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
    def __del__(self):
        '''I am dying.'''
        print ('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print ('I am the last one.')
        else:
            print ('There are still %d people left.' % Person.population)
    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print ('Hi, my name is %s.' % self.name)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print ('I am the only person here.')
        else:
            print ('We have %d persons here.' % Person.population)
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()
swaroop.sayHi()
swaroop.howMany()

#继承
#!/usr/bin/python
# Filename: inherit.py
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('(Initialized SchoolMember: %s)' % self.name)
    def tell(self):
        '''Tell my details.'''
        print ('Name:"%s" Age:"%s"' % (self.name, self.age),)
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ('(Initialized Teacher: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print ('Salary: "%d"' % self.salary)
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print ('Marks: "%d"' % self.marks)
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)
print # prints a blank line
members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students

#文件 I/O读写
#!/usr/bin/python
# Filename: using_file.py

f = file('d:/MyName.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file
f = file('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print (line),
    # Notice comma to avoid automatic newline added by Python
f.close() # close the file



#文件中的持久化存储
import cPickle as p
#import pickle as p
shoplistfile = 'shoplist.data'
# the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist # remove the shoplist
# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print (storedlist)