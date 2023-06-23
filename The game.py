from time import sleep
import random
global i
score=100
def scor():
    global score
    score-=1
    return score






def mstrip(x):
    d = []
    for i in x:
        if i.upper() in ['6','5','4','3','1','2','7','8','9','0',"A","B","C","D",'E','F',"G","H","I","J",
                         "K","L","M","N","O",'P','Q','R','S','T','U','V','W','X','Y','Z']:
            d.append(i.upper())

    return ''.join(d)
def print_pause(x):
    print(x)
    sleep(3)
def choice():
    x = input("what is your choice 1 or 2: ")
    while mstrip(x)!="1" and mstrip(x)!="2":
        x= input("what is your choice 1 or 2: ")

    #n is the score

    return mstrip(x)
def the_truth():
    global score
    print_pause("Upon closer examination, an initial observation stands out")
    print_pause("regarding Cristena's long artificial nails. It becomes")
    print_pause("evident that her nails would make it challenging for her")
    print_pause("to effectively handle a firearm. Assuming she had put on")
    print_pause("the artificial nails aboard the train, there should have")
    print_pause("been discernible marks left behind on the trigger.")
    print_pause("Alternatively, if she had changed all her fingernails, it")
    print_pause("would have raised suspicions due to noticeable marks or")
    print_pause("inconsistencies. Moreover, anyone familiar with artificial")
    print_pause("nails would be aware of her attempt to alter her appearance.")

    print_pause("Shifting focus to the other suspect, Wahid, no")
    print_pause("significant evidence has been uncovered thus far.")
    print_pause("However, upon revisiting the victim's body, a")
    print_pause("compelling detail surface. victim's index finger remains")
    print_pause("the only digit that stands upright, resembling a dying")
    print_pause("message often associated with the killer. Additionally,")
    print_pause("the Arabic word for 'one' is pronounced as 'Wahid,' which")
    print_pause("coincidentally shares the same spelling as the suspect's")
    print_pause("name. And I assume this because the victim was an Arabic")
    print_pause("to English translator.")

    print_pause("Furthermore, an examination of Wahid's belongings reveals")
    print_pause("a white chemical powder resembling that found in medical")
    print_pause("gloves suggesting an attempt that he wear them to")
    print_pause("suggesting an attempt. The redness on his hand can be")
    print_pause("attributed to wearing these gloves, suggesting an attempt.")

    print_pause("Based on these compelling pieces of evidence, it becomes")
    print_pause("clear that Wahid is the prime suspect in the murder case.")
    print_pause("A search of his bag would likely yield the gloves as")
    print_pause("further proof. Thus, Wahid, the conclusion is")
    print_pause("unequivocal—you are the perpetrator of this crime.")

    print_pause("(1)play another game ?")
    print_pause("(2)stop playing")
    scor()
    ch=choice()
    if ch=="1":
        random.choice([sit3,situ2])()
    else:

        print("thank you for playing")




def sit1():
    global score
    score=100

    print_pause("Amidst the dramatic backdrop of a moving train, "
          "a journey that commenced at 6 am ")
    print_pause("and was due to conclude at 10 am took an ominous turn at approximately 8:45 am. ")
    print_pause("Startled by the train conductor's frantic scream.")
    print_pause(" you and the other two individuals gathered beside a lifeless body. ")
    print_pause( "you as a detective who collaborating ")
    print_pause("with the police have only 85 minutes to uncover the circumstances of this person's death. ")
    print_pause("what is the first thing you will do?")
    print_pause("(1)	Inspect the crime scene.")
    print_pause("(2)	Examine the corpse.")
    scor()
    ch=choice()
    if ch=="1":
        inspect_the_scene()
    else:examine_the_corpse()

def inspect_the_scene():
    global score
    print_pause("after inspecting the crime scene")
    print_pause(" you found that the corpse is in the same Corridor ")
    print_pause("where the two other passengers' rooms are in  ")
    print_pause("what you will do now ?")
    print_pause("(1) searching for the murder weapon")
    print_pause("(2) Examine the corpse")
    ch=choice()
    if ch=="1":
        searching_for_gun()
    else:examine_the_corpse()

def searching_for_gun():
    global score
    print_pause("you found nothing. may be the murder throw it from the "
                "window of the train while the train moves")
    print_pause("what you will do now "
                "(1) Examine the corpse")
    print_pause("(2)inspect the scene ")
    ch=choice()
    scor()
    if ch=="1":
        examine_the_corpse()
    else:inspect_the_scene()
def examine_the_corpse():
    global score
    print_pause("After a thorough examination of the deceased individual,")
    print_pause(" several significant findings emerged.")
    print_pause(" Firstly, upon inspecting the victim's wallet,")
    print_pause(" it was uncovered that he was employed as a translator specializing in ")
    print_pause("Arabic-to-English translation. ")
    print_pause("This detail shed light on his professional background.")
    print_pause("Secondly, a meticulous examination of the body revealed a")
    print_pause(" bullet hole at the person's back, effectively ruling out the possibility of suicide and")
    print_pause(" indicating that the cause of death was indeed a gunshot wound.")
    print_pause(" This deduction strongly suggests the involvement of a firearm as the murder weapon.")
    print_pause("Lastly,")
    print_pause("an intriguing detail caught attention—the only finger that remained upright on the deceased's hand was the index finger.")
    print_pause("This peculiar observation raises suspicions that the victim ")
    print_pause("may have attempted to conceal or signal something to the murderer. ")
    print_pause("what you will do now ?"
          "(1) Talking with the suspects "
          "(2) searching for the gun inside the train" )
    scor()
    ch=choice()
    if ch=="1":
        talking_with_the_sus()
    else:searching_for_gun()
def talking_with_the_sus():

    print_pause(
        "The initial suspect in question is Wahid, a French doctor. When questioned about his connection to the victim, Wahid claimed that he had never encountered the deceased individual before and that this was their first meeting. You observe that his right hand is more red than his other hand and has a white chemical.")

    print_pause(
        "Another individual present at the scene is identified as Cristena. She was not only a math teacher but also hails from France. When questioned about her knowledge of the deceased, she claims to have seen him for the first time. However, a noteworthy observation catches your eye—a tail colored artificial nail adorning all Cristena's fingers.")


    print_pause("After a thorough examination of the deceased individual, several significant findings emerged.")
    print_pause(
        "Firstly, upon inspecting the victim's wallet, it was uncovered that he was employed as a translator specializing in Arabic-to-English translation. This detail shed light on his professional background.")
    print_pause(
        "Secondly, a meticulous examination of the body revealed a bullet hole at the person's back, effectively ruling out the possibility of suicide and indicating that the cause of death was indeed a gunshot wound. This deduction strongly suggests the involvement of a firearm as the murder weapon.")
    print_pause(
        "Lastly, an intriguing detail caught attention—the only finger that remained upright on the deceased's hand was the index finger. This peculiar observation raises suspicions that the victim may have attempted to conceal or signal something to the murderer.")
    print_pause("What will you do now?"
    "(1) tell who is the the Killer"
    "(2) Start again")
    scor()
    ch=choice()
    if ch=="1":
        finding_the_killer()
    else: sit1()
def finding_the_killer():
    print_pause("who is the killer? ")
    print_pause("(1) wahid ")
    print_pause("(2) cristena ")
    scor()
    ch=choice()
    if ch=="1":
        print_pause("you are right you are a great detective")

        print("your total score is :",scor()+4," out of 100")
    else:
        print_pause("sorry, you losed, do you want to play again to detect the right?")
        print_pause("(1) if you want ot repeat the game ")
        print_pause("(2) if you want to know the right inference")
        ch=choice()
        if ch=="1":
            sit1()
        else:
            the_truth()
def situ2():
    score=100
    print_pause("You are a detective investigating the theft of a precious ring from a "
                " famous business woman in a hotel")
    print_pause("what is the first thing you will do ?")
    print_pause("1- searchimg for the ring")
    print_pause("2- ask the woman about its descriptions")
    ch=choice()
    scor()
    if ch=="1":
        searching_for_the_ring()
    else:
        descriptions()
def descriptions():
    print_pause("it is a red ring has a wight Minor scratch on bottom")

    print_pause("what will you do now ")
    print_pause("1-asking her about the suspects ")
    print_pause("2-search for the people with a red ring")
    ch=choice()
    scor()
    if ch == "1":
        ask_for_sus()
    else:
        searching_for_the_ring()
def searching_for_the_ring():
    print_pause("you found a lot of people wear a ring  ")
    print_pause("what will you do now?")
    print_pause("1-ask the woman about its descriptions")
    print_pause("2-ask for the suspects")
    scor()
    ch=choice()
    if ch == "1":
        descriptions()
    else:
        ask_for_sus()
def ask_for_sus():
    print_pause("there are only three people can stool the ring, ms.Sara, ms.Dyana, and ms.Lana ")
    print_pause("what will you do now ?")
    print_pause("1-investigate with the suspects ")
    print_pause("2-ask for descriptions again")
    scor()
    ch=choice()
    if ch == "1":
        inves_sus()
    else:descriptions()
def inves_sus():
    print_pause("you ask a questions do you know any thing about a lost ring? "
                "and the answer be like")
    print_pause("ms.Sara:'i am busy now and i have no time for this children games,"
                " a ring i don't know any thing about a red ring'")
    print_pause("ms.Dyana:'sorry,i have no idea about any ring, i can not help you.'")
    print_pause("ms.Lana, are you kidding me a lost ring, if your ring get lost just buy another one ")
    print_pause("what will you do now ?")
    print_pause("1-shed light on the truth")
    print_pause("2-play again to remember some information ")
    scor()
    ch=choice()
    if ch == "1":
        the_truth2()
    else:descriptions()
def the_truth2():
    print_pause("The ring thief is: ")
    print_pause("1-Sara")
    print_pause("2- another one")
    ch=choice()
    if ch=="1":
        print_pause("congratulation you win, Sara is the thief because when")
        print_pause(" you ask her about the she says i do not no any thing about a 'red ring',")

        print_pause("yor score is: ")
        print(scor()+5)

        print_pause( "even you do not ask about a red you  just say a ring")
        print_pause("(1) playing anther game. ")
        print_pause("(2) stop playing .")
        scor()
        ch=choice()
        if ch=="1":
            random.choice([sit1,sit3])()
        else:print("thank you for playing" )
    else:
        print_pause("1- Dyana")
        print_pause("2- Lana")
        scor()
        ch=choice()
        if ch=="1":
            print("Sara is the thief because when" )
            print_pause(" you ask her about the she says i do not no any thing about a 'red ring',")
            print_pause("even you do not ask about a red you  just say 'a ring'")
        else:
            print("Sara is the thief because when" )
            print_pause(" you ask her about the she says i do not no any thing about a 'red ring',")
            print_pause("even you do not ask about a red you  just say 'a ring'")

def sit3():
    global score
    score=100
    print_pause("When you were staying in your office, someone knocked on the door and said, "
                "'Please help me find my son. "
                "I heard that you are a great detective.'  You paused for a moment, ")
    print_pause("considering the situation, and asked her for more details. "
                "She then mentioned that her son had left only one message and requested that "
                "you come to her house to investigate the clues there.")
    print_pause("what you will do now:")
    print_pause("(1) Ask her to show you the message.")
    print_pause("(2) visit her house and investigate.")
    scor()
    ch=choice()
    if ch=="1":
        show_massage()
    else:visit_home()
def show_massage():
    print_pause("the massage is 'sorry I left because I think you did not care about me, so I will "
                "leave for you a puzzle to test your knowledge about you son the puzzle is "
                "'the other message in my biggest A '.")
    print_pause("what will you do now:")
    print_pause("(1)ask her about his son and his interests.")
    print_pause("(2)visit her house and investigate their.")
    scor()
    ch=choice()
    if ch=="1":
        about_son()
    else:visit_home()
def visit_home():
    print_pause("you enter his room, and found a big poster contains 5 flags "
                "of a different countries and among those flags there was a "
                "flag bigger than the others and has this number 1998, and except this nothing"
                " is especial.")
    print_pause("what you will do now")

    print_pause("(1)	 ask her about his son and his interests."
                "(2)	say, your inference.")
    scor()
    ch=choice()
    if ch=="1" :
        about_son()
    else:inference()
def about_son():
    print_pause("I believe my son has a passion for football, and "
                "I believe he also enjoys watching anime. His favorite anime is 'Detective Conan.")
    print_pause("his bond with his father used to be incredibly strong, "
                "but unfortunately, his father passed away in 1998 while they were together in France.")
    print_pause("what you will do now ")
    print_pause("(1)say you inference."
                "(2)visit his room.")
    scor()
    ch=choice()
    if ch=="1":
        inference()
    else:visit_home()
def inference():
    print_pause("After assimilating all this information, it strikes you"
                " that his room's poster prominently displayed the flag of France, which was the largest. ")
    print_pause("You also recall that he has a love for football, and in the year his father passed away, 1998")
    print_pause("France emerged as the victorious team in the World Cup, which took place in France. ")
    print_pause("By piecing together these details, you come to the conclusion that both the son and"
                " his father were ardent supporters of the French national team. ")
    print_pause("Suddenly, the significance of the phrase 'my biggest A' becomes clear to you.")
    print_pause("do you now know what meant by my biggest A")
    print_pause("(1)Eiffel tower"
                "(2)the letter in 'France' word.")
    scor()
    ch=choice()
    if ch=="1":
        eiffel()
    else:
        letter()
def eiffel():
    print_pause("congratulation, your scorer is : " )
    print(scor()+5)
    print_pause( " Eiffel tower is  true and my mean that he has a Miniature ")
    print_pause("model of the Eiffel Tower. and the other massage inside it .")
    print_pause("Now, as you search his room once more, you come across "
                "a Miniature model of the Eiffel Tower hidden in his wardrobe. ")
    print_pause("To your surprise, inside the tower, you find a message that reads, 'Thank you, Mom, for always caring about me.'")
    print_pause("I'm currently on a visit to Russia to watch the final of the World Cup between France and Croatia on July 15, 2018. ")
    print_pause("I will return after the event. This reminds me of the wonderful days I spent with my father.'")
    print_pause("(1) play again another game")
    print_pause("(2)  top playing ")
    scor()
    ch=choice()
    if ch=="1":
        random.choice([sit1,situ2])()
    else:
        print("thank you for playing ")
def letter():
    print_pause("not true because it does not make "
                "sense that the other massage in France and you ignore the word 'my biggest'")
    print_pause("Eiffel tower is  true and  means that he has a Miniature model of the Eiffel Tower."
                " and the other massage inside it .")
    print_pause("Now, as you search his room once more, you come across "
                "a Miniature model of the Eiffel Tower hidden in his wardrobe. ")
    print_pause("To your surprise, inside the tower, you find a message that reads, "
                "'Thank you, Mom, for always caring about me.'")
    print_pause("I'm currently on a visit to Russia to watch the final of the World Cup between France and Croatia on July 15, 2018. ")
    print_pause("I will return after the event. This reminds me of the wonderful days I spent with my father.'")
    print_pause("(1) play another game")
    print_pause("(2)  stop playing  ")
    ch=choice()
    scor()
    if ch=="1":
        random.choice([sit1,situ2])()
    else:
        print("thank you for playing this game")











while True:


    print_pause("this a website to make all things clear i have created it")
    print_pause("https://a7h7m7e7d.github.io/DECI/web.html")
    sleep(2)

    random.choice([sit1,situ2,sit3])()

    break










