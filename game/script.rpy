# Opening chapter

# name of the character.

define u = Character("Uta")

define un = Character("?")
define ud = Character("Dad")
define p = Character("Priest")
define m = Character("Monsters")

# The game starts here.

label start:



    play music opening
    "Ahh, it's such a peaceful day."
    scene bg field

    un "What does it means to be peaceful?"

    "A place without conflict."
    "Perhaps."
    
    un "Why can't it always be peaceful?"
    
    "I wonder that too sometimes."
    
    un "If everyone was peaceful I could go anywhere right?"
    
    "If only it was, but each day I feel the profecy is comeing true things may change when you grow older."
    
    un "Why is that?"
    
    "Beasts and Monsters even conflicts amongst nations they have grown fiercer lately things will become really dangerous."
    
    un "*shudder*"
    
    "And then heroes will arive from outside this world to save us all when the time is right before the darkest hour."
    "As a Smith you must be ready when they arrive."
    
    un "I will!"

    stop music fadeout 2.0
    scene 
    show black
    
    "UTA!!"
    
    play music panic
    scene bg room1 with hpunch
    
    u "HUH?!"

    un "How long did you stay up last night?!"

    u "AHHHHHH!"

    un "Don't forget to come back before lunch!"
    
    u "Why didn't you remind me?!"
    
    ud "You are the one that told me you become a adult today."
    
    u "This is not fair! I will get scolded!"
    
    ud "If you run now you might reach the church in time for your ceremony."

    scene bg chapel with hpunch
    p "...with this I conclude, may the gods bless us all, for light and for prosperity."
    "Amen."
    
    u "Crap, it's already this late?!"
    
    p "Ah Uta of all the people I didn't think you would be missing today."
    
    u "I am really sorry! I was too exited and then I ..."
    
    p "Heh, when you didn't show up I already expected something like that from you."
    p "Unluckily for you, I have no mana for another proper blessing cerimony today but I can make a ritualistic one."
    
    stop music fadeout 3.0
    u "Umm, I don't know the difference."
    u "Thank god, I still can do it!"
    
    play music normal
    p "Alright, then come stand in this spot."
    "The prist splashes ceremonial water on Uta."
    
    u "Huh?!"
    
    p "May the gods bless this child, Amen."
    p "It's done."
    
    u "Amen!"
    u "Wait that was it?!"
    
    p "Well, it's usually for people futher away that can't travel the water I splashed you with is imbued with the different aspects of the ceremony."
    
    u "Huh ... so how do I?"
    
    p "Oh, well since we used the ritual you should manifest before the fall, your gift I mean."
    p "It might be inconvenient for you but Adults should come on time."
    
    u "I guess this is how it is then."
    u "Really, thank you!"
    
    p "If anything bad happens or nothing at all happens come to me tomorrow and I will take a look."
    
    u "Should be fine I think."
    
    "As I walk outside the other kids already know their gift, some even playing with sticks."
    
    u "Oh neat, that must be some sort of fighting skill."
    
    un "Break! Yes I win, this skill is amazing!"
    un "He's so strong now, he has the potenial to be a adventurer!"
    un "Hehe! I rather be a knight and start my own family line!"
    
    u "(Woah, this is so cool, I wonder what skill I can get...)"
    
    scene bg blacksmith room
    ud "Welcome back, did you know your skill yet?"
    
    u "Uhhhh... That I don't know yet."
    u "The priest told me I should know it later."
    ud "Ha, arrived to late huh?"
    u "Yes, but I am still gonna get something! It Could be the combat skill I always wanted!"
    ud "Don't get your hopes up too much, you will get the flame spirit skill like me and everyone before me."
    ud "Quit the adventurer dream and come to work with me."
    
    u "But dad... I would like to see how the world is like! The ocean, the mountains, the land covered in ice..."
    u "You know, just amazing wonders!"
    
    ud "Your grandfather is lucky to have had an adventure with the skill we inherited, even if it isn't as strong for combat as real combat skills."
    ud "But things have changed, a half hearted skill is not enough to travel the world anymore."
    
    u "*sigh"
    u "I will not give up on this."
    ud "Enough chit chat, I need your help. For at least one more day for being oversleeping!"

    jump chp1
