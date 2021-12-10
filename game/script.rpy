# Opening chapter

# name of the character.

define u = Character("Uta")

define un = Character("?")
define ud = Character("Dad")
define p = Character("Priest")

# The game starts here.

label start:

    play music opening
    "It is a peaceful day."
    scene bg field

    un "What does it means to be peaceful?"

    "A place without conflict."
    "Perhaps."
    
    un "I heard that war is a thing of the past."
    un "There is nothing we should be afraid of!"
    
    "Yes my dear."
    "Yet, the prophecy is true."
    "Things may change when you grow older."
    
    un "Why is that?"
    
    "The gods have decided our fate and prophecy is told to brave men many eons ago."
    "This is we have legends and tales."
    "The heroes will come to save us all when the times come..."
    "You must be ready when the end arrive."
    
    un "I will!"
    "You better be..."

    stop music fadeout 3.0
    scene 
    show black
    
    ""
    "Is this time already?"
    
    play music panic
    scene bg room1
    
    un "Don't forget to come back at 10!"
    
    u "Yikes! I think I'm late, why didn't you remind me?!"
    
    ud "Come on, you don't have much time now."
    
    u "This is not fair! I will get scold!"
    
    scene bg room1 with hpunch
    u "Ahhhh!"
    
    ud "If you run now, maybe you get there in time."
    
    u "This is no time for joke..."
    u "(Should have know better, why did I sleep so late last night?)"
    
    scene bg chapel
    p "...with this I conclude, the mightly lord should bless us all, for light and for prosperity."
    "Amen."
    
    u "Crap, they just finish."
    
    p "Is you, the girl they talked about who went missing today."
    p "Luckily or unluckily for you, the ceremonial will be done privately since I have no mana for today."
    
    stop music fadeout 3.0
    u "Umm, I don't know the difference."
    u "Thank god, I still can do it!"
    
    play music normal
    p "Then let's not waste anytime, Amen."
    p "It's done, you can go home now."
    p "*sigh"
    
    u "Thanks!"
    u "(Is this how ceremonial works? Just like that?)"
    u "..."
    
    p "Oh, before you ask, yes."
    p "You should know before fall, the gift I mean."
    p "If anything, please comeback tomorrow, I'm tired now."
    
    u "Wai- and the door just shut on me... Nice."
    u "I guess this is how it is then."
    u "..."
    u "Should be fine I think."
    
    "The other kids already know their gift, some even playing with sticks."
    
    u "Oh neat, that must be some sort of fighting skill."
    
    un "Break! Yes I win, this skill is amazing!"
    un "He's so strong now, he has the potenial to be a adventurer!"
    un "Hehe! I rather be a knight and start my own family line!"
    
    u "(Woah, this is so cool, I wonder what skill I can get...)"
    
    scene bg blacksmith room
    ud "Welcome back, did you know your skill yet?"
    
    u "Uhhhh... That I don't know yet."
    u "The priest told me I should know it later."
    u "I very excited! Could be something I always wanted!"
    
    ud "Ha, I heard the other kid has the fighting skill."
    ud "You won't get it since every village, there's only one fighter each year."
    ud "Quit the adventurer dream and come to work with me."
    
    u "But dad... I would like to see how the world is like! The ocean, the mountains, the land covered in ice..."
    u "You know, just amazing and unseen wonders!"
    
    ud "Your grandfather is lucky to have an adventure, he doesn't know how to fight."
    ud "The storm doesn't sink his trade ship, thank god for that or else you won't be here."
    
    u "*sigh"
    u "I will not give up on this."
    
    ud "Enough chit chat, I need your help. Come help me with this smithing, the bars aren't going to heat itself!"

    jump chp1
