#day0
print("HELLO WORLD!")

print("hello" + " "  + "Machine") #string concatenation using adding two strings

print("Hello World\nHello New Line\tHello tab")   #\n for new line, \t for tab

print("When need to print \\n instead of new line and single back slash \\") #not assume \n as new line

# test input method to take inputs and print results

#input takes all data as string, need to convert to other data type if needed i.e int
#print("Nice to meet you:", input("Howdy, What's your name? ") + "!")

#variables

name = input("What's your name? ")
length_name = len(name) #len function return number of characters in string
print("Nice to meet you", name, ". " + "YOUR NAME HAS NO. OF CHAR: ", length_name )

