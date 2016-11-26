#!/usr/bin/python
#JcharisTech tools by Jcharis
# Cryptscripts.py version 1.0
import codecs
import base64
import random
import string

print("====================================")
print("Cryptscripts.py")
print("Version 1.0 by JcharisTech")
print ("Cryptscripts uses python3") 
print("====================================")
print("Cryptology Scripts")
print("""
      MAIN MENU
      1 BASE64 ENCODE
      2 BASE64 DECODE
      3 ROT -13
      4 CAESAR SHIFT
      5 REVERSE
      6 MESSAGE REVERSE
      7 MISC
      8 UPPER CASE
      9 Lower Case
      10 LEET CONVERTER
      11 Caesar char and ord
      12 PHRASE COUNTER
      13 RANDOM SHUFFLER
      14 RANDOM PASSWORD GENERATOR(pw-gen like)
      
""")

menu = int(input("Enter Your Choice from Menu: "))


if menu == 1:
    print ("BASE 64 ENCODE")
    print("string conversion is utf-8")
    
    toEncodedText = input("What is your plaintext? ")
    #sTringencodetype = input("Choose type of string encoding eg utf-8 ,ascii")
    clearText = base64.b64encode(bytes('toEncodedText','utf-8'))
    print (clearText)
    
elif menu == 2:
    print("BASE 64 DECODE")

    toDecodedText = input("What is your encodedtext? ")
    clearText = base64.b64decode(toDecodedText)
    print (clearText)
    
elif menu == 3:
    print ("ROT-13")
    #ROTATION 
    plainText2= input("What is your rotation text?: ")
    #python 3.5
    cipherText2=codecs.getencoder("rot-13")(plainText2)
    print (cipherText2)

    #python 2.7
    #cipherText= plainText2.encode('rot13') python2.7
    #print (cipherText)
elif menu == 4:
    print ("CAESAR SHIFT")
    #CaesarBruteForce
    ctext = input("What text do you want to shift?: ")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    plaintext = ""
    shift = 1
 
    while shift <= 26:
     for c in ctext:
      if c in alphabet:
       plaintext += alphabet[(alphabet.index(c)+shift)%(len(alphabet))]
     print("Shift used: " + str(shift))
     print("Ciphertext: " + ctext)
     print("Plaintext: " + plaintext)
     shift = shift + 1
     plaintext = ""

#Reverse Script
elif menu == 5:
    print ("REVERSE SCRIPT")
    toReverseText = input("Enter Text to Reverse: ")
    reverSEd = toReverseText[::-1]
    print (reverSEd)

#Reverse Message
elif menu == 6:
    print ("MESSAGE REVERSE")
    message = input("Enter Message to Reverse: ")
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    print(translated)

#MISCELLANOUS
elif menu == 7:
    print ("MISC In progress ;Check out our youtube channel @ J-sec;")
    print ("MISC In progress ;Jesus saves")  
    print ("MISC In progress ;Check our blog @ www.jcharistech.wordpress.com ") 


#UPPER CASE CONVERTING
elif menu == 8:
    print ("UPPER CASE CONVERTER")
    wordcase = input("Enter your text here: ")
    convUpper = wordcase.upper()
    print(convUpper)
    
#LOWER CASE CONVERTING
elif menu == 9:
    print ("LOWER CASE CONVERTER")
    wordcase = input("Enter your text here: ")
    convLower = wordcase.lower()
    print(convLower)
#LEET CONVERTER 
elif menu == 10:
    print ("LEET CONVERTER")
    replacements = ( ('hacker','haxor'), ('elite','eleet'), ('a','4'),('b','l3'),('c','('),('d','[)'), ('e','3'),
                 ('l','1'),('s','5'),('t','7'), ('w','\/\/'),('o','0'), ('t','+') )
    my_string = input("Enter Text here: ")
    new_string = my_string
    for old, new in replacements:
        new_string = new_string.replace(old, new)

    print ( new_string )

 #Caesaer Script
elif menu == 11:
    print("CHAR AND ORD SCRIPT")
    plainText = input("What is your plaintext? ")

    for i in plainText:
        caesarit=ord('i')
        print (caesarit)
elif menu == 12:
    print ("Phrase Count")
    phrase = input("Enter Full Text: ")
    tfinder = len(phrase)
    print ("Length is :" ,tfinder)

#RANDOM PASSWORD GENERATOR
elif menu == 13:
    print ("RANDOM SHUFFLER")
    unshuff = input("Enter Text to shuffle: ")
    shuff = list(unshuff)
    print (shuff)
    print (random.shuffle(shuff))
    
#PASSWORD GENERATOR LIKE PWGEN    
elif menu == 14:
	print ("RANDOM PASSWORD GENERATOR")
	def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
		return ''.join(random.choice(chars) for _ in range(size))

	print(pw_gen(int(input('Number of characters in your password?: '))))    



else:
    print ('Wrong Number...Retry')
    print ('Thanks for Using Cryptscript')
    














