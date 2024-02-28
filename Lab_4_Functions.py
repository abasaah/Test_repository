#!/usr/bin/env python
# coding: utf-8

# # What you will learn in this lesson
# 
# 1. Defining functions
# 
# 2. Variable scope
# 
# 3. Documentation
# 
# 4. Lamda expressions
# 
# 5. high level functions
# 
# 6. List comprehentions

# In[66]:


x='Selorm'


# In[2]:


print(len(x))


# In[67]:


def count_function(name):
    count = 0
    for i in range(len(name)):
        count+=1
    return count    
    


# In[63]:


def count_function(name):
    count = 0
    for i in name:
        count+=1
    return count  


# In[68]:


count_function(x)


# In[6]:


count = 0
for i in range(len(x)):
    count+=1
print(count)   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


len()


# In[4]:


count


# # Funtions
# 
# A function is a block of codes that performs an action.

# ### Parts(components) of a function in python
# * Function Header
# 
# The function header always starts with the def keyword, which indicates that this is a function definition.
# 
# Then comes the function name (cylinder_volume)
# 
# Immediately after the name are parentheses that may include arguments separated by commas which in our case are height and radius
# 
# Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. 
# 
# NB: If a function doesn't take arguments, these parentheses are left empty.
# 
# The header always end with a colon :.
# 
# 
# * Funtion Body
# 
# The body of a function is the rest of the code after the header line.
# 
# Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
# 
# The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function.
# 
# NB: The body of a function may not contain a return stamentment but a print statement.
# 
# A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. 
# 
# If there is no return statement, the function simply returns None.
# 
# 
# 

# In[7]:


x =[12,45,2,3,4,5,6]


# In[8]:


min(x)


# In[9]:


max(x)


# In[11]:


# Empty function
def empty_function(): 
    
    
    
    pass


# In[12]:


empty_function()


# In[13]:


# Example 1
def cylinder_volume(height,radius):#<----- function header
   
    pi = 3.14186
    return height*pi*radius**2     #<------ function body


# In[14]:


pi


# In[15]:


cylinder_volume(3,1.2)


# In[16]:


# height = 13
# radius = 7

cylinder_volume(13,7)


# In[ ]:





# ### Variable scope
# This refers to which part of a program that a variable can be referenced or used from.

# **Local variables**: they are variables that can only be accessed inside the funtion
# 
# **Global variables**: they are variables that can be accessed ouside a function.    
# 
# The **pi** in the cylinder volume function is a local variable.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[ ]:


#pi # this variable has a local scope hence, cannot accessed outside the function


# In[17]:


pi_ = 22/7


# In[18]:


pi_ # Global scope


# In[19]:


# Example 2

def area_circle(radius):
    

    
    return pi_*radius**2
   


# In[20]:


area_circle(8)


# In[24]:


#Example 3
def bmi(height,weight):
     return weight/height**2


# In[25]:


bmi(1.6,56)


# In[23]:


bmi(1.9,69.78)


# In[ ]:





# ### Difference between print and return in a function

# In[26]:


def print_new_age(current_age,year):
    age = current_age +(year-2021)
    print(age)
    
    
def return_new_age(current_age,year):
    age = current_age +(year-2021)
    return age


# In[27]:


print_new_age(20,2087)


# In[28]:


return_new_age(20,2087)


# In[29]:


x = print_new_age(20,2087)


# In[30]:


print(x)


# In[32]:


x


# In[33]:


x/2 # This will produce an error


# In[34]:


y = return_new_age(20,2087)


# In[35]:


print(y)


# In[36]:


y/2


# In[ ]:





# In[37]:


def average_score(x):
    ave = sum(x)/len(x)
    return ave

def average_score_print(x):
    ave = sum(x)/len(x)
    print(ave)


# In[38]:


marks = [477,15,4597,45698,41,2.558,7849]

average_marks = average_score(marks)


# In[39]:


print(average_marks)


# In[40]:


marks = [477,15,4597,45698,41,2.558,7849]

average_marks_2 = average_score_print(marks)


# In[41]:


print(average_marks_2)


# ### arguments of a function
# 
# They are values passed as inputs to a function

# In[55]:


# default arguments

def cylinder_volume(height,radius,pi = 3.14186):
   
    return height*pi*radius**2


# In[43]:


cylinder_volume(5,1.4)


# In[44]:


# default arguments

def cylinder_volume(height,radius,pi= 3.14186): # This is wrong,non-default argument shouldn't follow default argument 
   
    return height*pi*radius**2


# In[47]:


cylinder_volume(23,4,22/7)


# In[48]:


cylinder_volume(23,4)


# In[49]:


cylinder_volume(4,23,22/7)


# ### passing arguments
# 1. By position
# 2. By name

# In[50]:


def bmi(height,weight):
    return weight/height**2


# ### By position
# To call a function by position, the arrangement of the arguments matters

# In[51]:


bmi(1.76,65) # Calling a function by position


# In[52]:


bmi(65,1.76) # This is wrong


# ### By name
# To call a function by name, the arrangement of the arguments does not matters

# In[53]:


bmi(height=1.76, weight=65) # calling a function by name


# In[54]:


bmi(weight=65,height=1.76 )


# ## Documentation Strings (Docstrings)

# In[ ]:


def return_new_age(current_age,year):
    """
    Calculates the age of a person at a given year from 2021.
    
    INPUT:
    current_age: int, current age of the person.
    year: int, prefered year
    
    OUTPUT: 
    return_new_age: current_age +(year-2021), returns age of the person at the given year from 2021
    
    """
    age = current_age +(year-2021)
    return age


# In[ ]:


return_new_age(20,2087)


# In[ ]:


help(return_new_age)


# In[ ]:


def bmi(height,weight):
    """
    This function calculates the bmi of a person
    
    INPUT:
    height:float or int,height of a person in meters
    weight: float or int,weight of a person in kilograms
    """
    return weight/height**2


# In[ ]:


bmi(1.7,59)


# In[ ]:


help(bmi)


# In[ ]:


return_new_age() # put the curser inside the bracket and press shift+tab to view the docstring 


# In[ ]:


get_ipython().run_line_magic('pinfo', 'return_new_age')


# In[ ]:


help(print)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'print')


# ## Lamda expressions (Anonymous functions)
# 
# #### Components of a Lambda Function
# 
# The lambda keyword is used to indicate that this is a lambda expression.
# 
# Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
# 
# Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
# 
# With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.
# 
# Lamda expressions are used to create anonimous functions(functions that do not have names)

# In[ ]:


def square(x):
    return x**2

square(6)


# In[ ]:


lambda x: x**2


# In[ ]:


lambda price,quantity,cost:(price*quantity)-cost


# In[ ]:


n = [12,4,5,6,3,4,67,8,9]


# In[ ]:


square_lambda = lambda x: x**2
    


# In[ ]:


square_lambda(6)


# In[ ]:


lambda_bmi=lambda height,weight : weight/height**2


# In[ ]:


lambda_bmi(1.7,64)


# In[ ]:


lambda_bmi(weight=64,height=1.7) # you call lambda expressions explicitly (thus names)


# In[ ]:


square=lambda argument: argument**2


# In[ ]:


square(6)


# In[ ]:


BMI=lambda w,h: w/h**2


# In[ ]:


BMI(62,1.5)


# ### some important higher-order built-in functions
# 
# 1. map()
# 
# **map()** is a higher-order built-in function that takes a 
# 
# function and iterable as inputs, and returns an iterator that 
# 
# applies the function to each element of the iterable.
# 
# 
# 
# 2.**filter()** is a higher-order built-in function that takes a 
# 
# function and iterable as inputs and returns an iterator with 
# 
# the elements from the iterable for which the function returns 
# 
# True.

# ### map()

# In[ ]:





# In[2]:


numbers = [ [34, 63, 88, 71, 29],[90, 78, 51, 27, 45], [63, 37, 85, 46, 22], [51, 22, 34, 11, 18]]
        


# In[ ]:





# In[ ]:





# In[13]:


# using the for loop
# solution 1
for i in range(len(numbers)):
    
    print(sum(numbers[i])/len(numbers[i]))


# In[ ]:





# In[11]:


for i in numbers:
    print(i)


# In[14]:


# using the for loop
# solution 2
for i in numbers:
    print(sum(i)/len(i))


# In[ ]:





# In[76]:


# Solution 3

for i,marks in enumerate(numbers):
    print(sum(numbers[i])/len(numbers[i]))


# In[ ]:





# In[15]:


def average_score(x):
    return sum(x) / len(x)


# In[16]:


numbers[0]


# In[17]:


average_score(numbers[0])


# In[21]:


map(average_score,numbers)


# In[22]:


list(map(average_score,numbers))


# In[23]:


map(min,numbers)


# In[24]:


list(map(min,numbers))


# In[25]:


list(map(max,numbers))


# In[26]:


tuple(map(max,numbers))


# In[27]:


set(map(max,numbers))


# ### Using lambda functions with map()

# In[28]:


n = [12,4,5,6,3,4,67,8,9]


# In[29]:


list(map(lambda x:x**2,n))


# In[30]:


y = list(map(lambda x:x**2,n))


# In[31]:


y


# In[ ]:





# In[ ]:





# In[32]:


team_points=[87,45,67,90,100,12,35,89,55,55]


# In[33]:


def add_8(value_list):
    return value_list+8


# In[34]:



team_points_8 = list(map(add_8,team_points))
team_points_8


# In[ ]:





# In[36]:


mean_l = lambda nums:sum(nums)/len(nums)

ave = list(map(mean_l,numbers))
print(ave)


# In[37]:


ave = list(map(lambda nums:sum(nums)/len(nums),numbers))
print(ave)


# ### filter()

# In[47]:


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) <10


# In[48]:


is_short(cities[0])


# In[49]:


is_short(cities[2])


# In[50]:


short_cities = list(filter(is_short, cities))
print(short_cities)


# In[51]:


is_less = lambda name: len(name) < 10
less_cities = list(filter(is_less,cities))
print(less_cities)


# ## Zip and Enumerate

# ## zip()

# **zip** and **enumerate** are useful built-in functions that can come in handy when dealing with loops.
# They help to simplify tasks.
# 
# **zip** returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.

# ### zip()

# In[59]:


country = ['Ghana','Togo','Nigeria','Ivory Coast','South Africa']

capital = ['Accra', 'Lome', 'Abuja','Abidjan','Johannesburg']

currency = ['Cedis','CFA','Naira','CFA','Rand']


# In[ ]:


#(1,'a'),(2,'b') (3,'c')


# In[60]:


zip(country,capital,currency)


# In[61]:


list(zip(country,capital,currency))


# In[62]:


#example
list(zip(['a', 'b', 'c'], [1, 2, 3])) 


# In[63]:


l = ('a','e','r','t')
n =(3,4,5,6,)


# In[64]:


list(zip(l,n))


# In[ ]:





# ### Using the for loop with zip

# In[67]:


countries = ['Ghana','Togo','Nigeria','Ivory Coast','South Africa']

capitals = ['Accra', 'Lome', 'Abuja','Abidjan','Johannesburg']

currencies = ['Cedis','CFA','Naira','CFA','Rand']


# In[69]:


for country,capital,currency in zip(countries,capitals,currencies):
    print("{} : {} : {} ".format(country,capital,currency))


# In[ ]:





# ### Unzipping

# In[71]:


my_list = [('a', 1), ('b', 2), ('c', 3)]

letters, nums = zip(*my_list)              # To unzip a data structure bring a * before the input.


# In[72]:


letters


# In[73]:


nums


# ### Enumerate()

# **enumerate** is a built in function that returns an iterator 
# 
# of tuples containing indices and values of a list.
# 
# You'll often use enumerate when you want the index along with each 
# 
# element of an iterable in a loop.
# 

# In[74]:


letters = ['a', 'b', 'c', 'd', 'e']
list(enumerate(letters))


# In[78]:


tuple_1 = (67,65,90,87) # tuple unpacking
x,y,z,s = tuple_1


# In[80]:


print(x)
print(y)
print(z)
print(s)


# In[75]:


letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)


# ### List Comprehentions
# 
# List comprehensions allow us to create a list using a for loop in one step.
# 
# You create a list comprehension with brackets [ ], including an expression to evaluate for each element in an iterable.
# 

# In[81]:


# List comprehension format: 
# [expression followed by iterable or iteration]
#Eg:


squares = [x**2 for x in range(1,10)]
print(squares)


# In[82]:


squares = []
for i in range(1,10):
    squares.append(i**2)
print(squares)


# ### Conditionals in List Comprehensions
# 
# You can also add conditionals to list comprehensions (listcomps).
# 
# After the iterable, you can use the if keyword to check a condition in each iteration.
# 

# In[83]:


# Conditional list comprehension without 'else' format: 
# [exprssion followed by iterable followed by condition]
# Eg:
squares = [x**2 for x in range(1,10) if x % 2 == 0]
print(squares)


# Conditional List Comprehensions that includes 'else' in the
# 
# condition have a different format.
# 
# In cases like this you have to move the conditionals to the beginning of
# 
# the listcomp, right after the expression.
# 

# In[84]:


# Conditional list comprehension without 'else' format: 
# [exprssion followed by condition followed by else condition followed by iterable]
# Eg:
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(1,10)]
print(squares)


# In[ ]:





# In[ ]:





# In[ ]:





# ## Exercise

# ### Question 1
# 
# Use a list comprehension to create a new  list called first_names containing just the first names in the list names in lowercase.
# 

# In[85]:


names = ['Ama Frimpong','Agyemang Duah','Kwesi Amstrong','Patrick Mensah', 'Emmanuel Doe', 'Nelson Tettey']


# In[90]:


names[0].split()[0].lower()


# In[ ]:





# In[98]:


#Solution

first_names = [name.split()[0].lower() for name in names]
print(first_names)


# In[99]:


names = ['Ama Frimpong','Agyemang Duah','Kwesi Amstrong','Patrick Mensah', 'Emmanuel Doe', 'Nelson Tettey']


# In[100]:


names


# In[101]:


for name in names:
    print(name.split()[0].lower())


# In[ ]:





# ### Question 2
# Use a list comprehension to create a list called multiples_3, containing the first 20 multiples of 3.

# In[102]:


# solution
multiples_3 =[i*3 for i in range(1,21)]
print(multiples_3)


# ### Question 3
# 
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
# 

# In[104]:


scores = {
             "Rick Ampofo": 70,
             "Morty Smith": 35,
             "Samuel Sarpong": 82,
             "Jerry Rawlings": 23,
             "Bethilda Great": 98
          }


# In[ ]:





# In[105]:


passed =[name for name,score in scores.items() if score >= 65] 
print(passed)


# In[106]:


# solution
passed =[(name,score) for name,score in scores.items() if score >= 65] 
print(passed)


# In[ ]:


z = scores.items()


# In[ ]:




