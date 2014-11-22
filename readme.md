###Hello Project Tech Teens!

For today's exercise these may be some helpful hints on how we can build a guessing game. [You can follow along with the slides as well](https://docs.google.com/presentation/d/1_USVM2isK9PPsC0c-Reo3NJGEcbApwO-6GOb10YTvAo/edit?usp=sharing).

Oh and if you wanted to make your own ASCII art try [here](http://www.network-science.de/ascii/).

###Object Types

Objects give us the **WHO** and **WHAT** in a program. Python's builtin objects that we will want to use:

* Strings
* Integers
* Booleans

```
i_am_a_string = "Hello World!"
i_am_an_integer = 4
i_am_a_boolean = False
```

###Functions

Functions allow us to *DO THINGS* in our programs. Some of Python's built in functions we will want to use:

```
    print "Hello World" 
    ## Prints a String "Hello World" to the screen 
    
    name = raw_input("Please type in your name: ") 
    ## Prints a message to the screen asking the user for input,
    records the input in the variable name
    
    int("5")
    ## Turns String "5" into an Integer 5
    
    str(5)
    ## Turns Integer 5 into String "5"
    
    random.randrange(0,10)
    ## Creates a random number between 0 and 10
    
    sys.exit()
    ## Closes a program
    
    "HELLO WORLD".lower()
    ## Turns String "HELLO WORLD" into "hello world"
    
    "  hello world  ".strip()
    ## Removes extra spaces at start and end.
    
```

We can write our own! This method needs additional information, it needs a number.

```
   def add_two(number):
       return number + 2
   
   print add_two(4) 
   ## prints 6
```
###Logical Operators

Let's us compare two things by returning a boolean of True or False. 

Example - Equality Test

```
   name = "Lorena"
   name == "Lorena"
```


[More logical operators](http://www.tutorialspoint.com/python/python_basic_operators.htm)

###If / else if / else statements

```
    name = "Lorena"
    if name == "Lorena":
       print "Hello Lorena"
    else if name == "Rahul":
       print "Hello Rahul"
    else:
       print "Hello"
    
```

####Error Messages!!

Errors can happen. But Python will tell you what you did wrong! As coders we often make mistakes, but that's OK! You can always fix it :-)

###Python and Whitespace
Whitespace, or the number of spaces (spacebar), is important in Python. Each time you write a statement that spans more than one line, indent the second line by four spaces.

```
greeting = "hello"
if greeting == "hello":
 print greeting
  File "<stdin>", line 2
    print greeting
        ^
IndentationError: expected an indented block
```




