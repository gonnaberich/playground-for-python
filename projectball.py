# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("ask the magic eight ball a question, WARNING ANSWER MAY BE EXTREMELY SASSY: (press enter to quit) ")
    
    answers = random.randint(1,19)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "Outlook not good"
      
    elif answers == 2:
        print "You may rely on it"
    
    elif answers == 3:
        print "its a secret to everybody"
    
    elif answers == 4:
        print "My sources say no"
    
    elif answers == 5: 
        print "yes"
        
    elif answers == 6:
        print "yowzah"
        
    elif answers == 7:
        print "please hold while I contact the all knowing coding master for the answer to your question"
        
    elif answers == 8:
        print "change your tone of voice and maybe i'll answer"
        
    elif answers == 9:
        print "it is certain"
        
    elif answers == 10:
        print "empty your mind and ask again"
        
    elif answers == 11:
        print "the answer lies within a carbonated drink of your choice"
        
    elif answers == 12:
        print "give me one good reason why I should answer your question"
        
    elif answers == 13:
        print "ha ha thats a joke right?"
        
    elif answers == 14:
        print "Im a computer not a fortuneteller"
        
    elif answers == 15:
        print "dont you already know the answer?"
    
    elif answers == 16:
        print "Why are you asking me this when you already know the answer to this?"
        
    elif answers == 17:
        print "The answer may lies closer than you think"
        
    elif answers == 18:
        print ("The answer will appear soon")
        
    elif answers == 19:
        print ("Loading I will have an answer shortly")