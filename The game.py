from time import sleep
import datetime
import random

score = 0
current_time = 0
x = input("Your name: ")


def sit1():
    global current_time
    current_time = datetime.datetime.now()
    global score
    score = 0
    global x
    x = input("Your name: ")
    print_pause(
        "Hi " + x + ", check this scenario and try to find a solution for this case."
    )
    print_pause(
        "Amidst the dramatic backdrop of a moving "
        "train, a journey that commenced at 6 am and was due to conclude at "
        "10 am took an ominous turn at approximately 8:45 am."
    )
    print_pause(
        "Startled by the train conductor's frantic "
        "scream, you and the other two individuals gathered beside a lifeless body."
    )
    print_pause(
        "As a detective collaborating with the police, "
        "you have only 85 minutes to uncover the circumstances of this person's death."
    )
    print_pause("What is the first thing you will do?")
    print_pause("(1) Inspect the crime scene.")
    print_pause("(2) Examine the corpse.")
    ch = choice()
    score += 30
    if ch == "1":
        print("Good choice, " + x + "! Your score is", score)
        inspect_the_scene()
    else:
        print("Good choice, " + x + "! Your score is", score)
        examine_the_corpse()


def inspect_the_scene():
    global score
    print_pause(
        "After inspecting the crime scene, you found that the"
        " corpse is in the same corridor where the two other passengers' rooms are."
    )
    print_pause("What will you do now?")
    print_pause("(1) Search for the murder weapon.")
    print_pause("(2) Examine the corpse.")
    ch = choice()
    if ch == "1":
        score += 5
        print("Good choice, " + x + "! Your score is", score)
        searching_for_gun()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is", score)
        examine_the_corpse()


def searching_for_gun():
    global score
    print_pause(
        "You found nothing. Maybe the murderer threw the weapon "
        "from the window of the moving train."
    )
    print_pause("What will you do now?")
    print_pause("(1) Examine the corpse.")
    print_pause("(2) Inspect the crime scene.")
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is", score)
        examine_the_corpse()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is", score)
        inspect_the_scene()


def examine_the_corpse():
    global score
    print_pause(
        "After a thorough examination of the deceased individual, several"
        " significant findings emerged."
    )
    print_pause(
        "Firstly, upon inspecting the victim's wallet, it was uncovered"
        " that he was employed as a translator specializing in Arabic-to"
        "-English translation."
    )
    print_pause("This detail shed light on his professional background.")
    print_pause(
        "Secondly, a meticulous examination of the body revealed a bullet"
        " hole at the person's back, effectively ruling out the possibility of "
        "suicide and indicating that the cause of death was indeed a"
        " gunshot wound."
    )
    print_pause(
        "This deduction strongly suggests the involvement of a firearm"
        " as the murder weapon."
    )
    print_pause(
        "Lastly, an intriguing detail caught attention—the only "
        "finger that remained upright on the deceased's hand was the index finger."
    )
    print_pause(
        "This peculiar observation raises suspicions that the victim "
        "may have attempted to conceal or signal something to the murderer."
    )
    print_pause("What will you do now?")
    print_pause("(1) Talk with the suspects.")
    print_pause("(2) Search for the gun inside the train.")
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        talking_with_the_sus()
    else:
        score += 5
        print("Good choice, " + x + "! Your score is " + str(score))
        searching_for_gun()


def talking_with_the_sus():
    global score
    print_pause(
        "The initial suspect in question is Wahid, "
        "a French doctor. When questioned about his connection to the victim,"
        " Wahid claimed that he had never encountered the deceased individual before"
        " and that this was their first meeting."
    )
    print_pause(
        "Another individual present at the scene is identified as"
        " Cristena. She was not only a math teacher but also hails from"
        " France. When questioned about her knowledge of the deceased, "
        "she claims to "
        "have seen him for the first time."
    )
    print_pause(
        "After a thorough examination of the deceased individual,"
        " several significant findings emerged."
    )
    print_pause(
        "Firstly, upon inspecting the victim's wallet, it was uncovered that he"
        " was employed as a translator specializing in Arabic-to-English translation."
        " This detail shed light on his professional background."
    )
    print_pause(
        "Secondly, a meticulous examination of the body revealed a bullet hole at the"
        " person's back, effectively ruling out the possibility of suicide and indicating "
        "that the cause of death was indeed a gunshot wound. This deduction strongly "
        "suggests the involvement of a firearm as the murder weapon."
    )
    print_pause(
        "Lastly, an intriguing detail caught "
        "attention—the only finger that remained upright on the "
        "deceased's hand was the index finger. This peculiar observation "
        "raises suspicions that the victim may have attempted to conceal or signal "
        "something to the murderer."
    )
    print_pause("What will you do now?")
    print_pause("(1) Tell who the killer is.")
    print_pause("(2) Start again.")
    ch = choice()
    if ch == "1":
        print("Good choice, " + x + "! Your score is " + str(score))
        finding_the_killer()
    else:
        print("Good choice, " + x + "! Your score is " + str(score))
        sit1()


def finding_the_killer():
    global score
    print_pause("Who is the killer?")
    print_pause("(1) Wahid.")
    print_pause("(2) Cristena.")
    ch = choice()
    if ch == "1":
        global current_time
        current_time1 = datetime.datetime.now()
        print(
            "Your total score is: "
            + str(score + 50)
            + " out of 100 and you took "
            + str(current_time1 - current_time)
            + " to find the solution."
        )
        print("(1) Play another game?")
        print("(2) Stop playing.")
        ch = choice()
        if ch == "1":
            random.choice([sit1, situ2])()
        else:
            print("Thank you for playing!")
    else:
        current_time1 = datetime.datetime.now()
        print(
            "Sorry, "
            + x
            + ", you lost. Your score is "
            + str(score)
            + " out of 100 and you took "
            + str(current_time1 - current_time)
            + " to find the solution."
        )
        print("Do you want to play again to detect the right?")
        print("(1) Play again.")
        print("(2) Know the right inference.")

        ch = choice()
        if ch == "1":
            sit1()
        else:
            the_truth()


def choice():
    x = input("What is your choice, 1 or 2: ")
    while x.strip() != "1" and x.strip() != "2":
        x = input("What is your choice, 1 or 2: ")
    return x.strip()


def the_truth():
    print_pause(
        "Upon closer examination, an initial "
        "observation stands out regarding Cristena's long artificial nails."
    )
    print_pause(
        "It becomes evident that her nails would "
        "make it challenging for her to effectively handle a firearm."
    )
    print_pause(
        "Assuming she had put on the artificial nails"
        " aboard the train, there should have been discernible marks left"
        " behind on the trigger."
    )
    print_pause(
        "Alternatively, if she had changed all her "
        "fingernails, it would have raised suspicions due to noticeable marks "
        "or inconsistencies."
    )
    print_pause(
        "Moreover, anyone familiar with artificial "
        "nails would be aware of her attempt to alter her appearance."
    )
    print_pause(
        "Shifting focus to the other suspect, Wahid, "
        "no significant evidence has been uncovered thus far."
    )
    print_pause(
        "However, upon revisiting the victim's body, a compelling " "detail surfaces."
    )
    print_pause(
        "The victim's index finger remains the only digit that "
        "stands upright, resembling a dying message often associated with the killer."
    )
    print_pause(
        "Additionally, the Arabic word for 'one' is pronounced as "
        "'Wahid,' which coincidentally shares the same spelling as the suspect's name."
    )
    print_pause(
        "Furthermore, an examination of Wahid's belongings reveals a"
        " white chemical powder resembling that found in medical gloves,"
        " suggesting an attempt to wear them."
    )
    print_pause(
        "The redness on his hand can be attributed to wearing these "
        "gloves, suggesting an attempt."
    )
    print_pause(
        "Based on these compelling pieces of evidence, it becomes "
        "clear that Wahid is the prime suspect in the murder case."
    )
    print_pause("A search of his bag would likely yield the gloves as further proof.")
    print_pause(
        "Thus, Wahid, the conclusion is unequivocal—you are the "
        "perpetrator of this crime."
    )
    print_pause("(1) Play another game?")
    print_pause("(2) Stop playing.")
    ch = choice()
    if ch == "1":
        random.choice([sit3(), situ2])()
    else:
        print("Thank you for playing!")


def print_pause(x):
    print(x)
    sleep(3)


def situ2():
    global score
    score = 0
    global current_time
    current_time = datetime.datetime.now()
    print_pause(
        "You are a detective investigating the theft of a"
        " precious ring from a famous businesswoman in a hotel"
    )
    print_pause("What is the first thing you will do?")
    print_pause("1- Search for the ring")
    print_pause("2- Ask the woman about its descriptions")
    ch = choice()
    global x
    if ch == "1":
        score += 5
        print("Good choice, " + x + "! Your score is " + str(score))
        searching_for_the_ring()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        descriptions()


def descriptions():
    print_pause("The ring is red and has a white minor scratch on the bottom.")
    print_pause("What will you do now?")
    print_pause("1- Ask her about the suspects")
    print_pause("2- Search for people with a red ring")
    ch = choice()
    if ch == "1":
        global score
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        ask_for_sus()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        searching_for_the_ring()


def searching_for_the_ring():
    print_pause("You found a lot of people wearing a ring.")
    print_pause("What will you do now?")
    print_pause("1- Ask the woman about its descriptions")
    print_pause("2- Ask for the suspects")
    ch = choice()
    global score
    score += 10
    if ch == "1":
        print("Good choice, " + x + "! Your score is " + str(score))
        descriptions()
    else:
        score += 1
        print("Good choice, " + x + "! Your score is " + str(score))
        ask_for_sus()


def ask_for_sus():
    print_pause(
        "There are only three people who could "
        "have stolen the ring: Ms. Sara, Ms. Dyana, and Ms. Lana."
    )
    print_pause("What will you do now?")
    print_pause("1- Investigate with the suspects")
    print_pause("2- Ask for descriptions again")
    ch = choice()
    global score
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        inves_sus()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        descriptions()


def inves_sus():
    print_pause("You ask a question: 'Do you know anything about a lost ring?'")
    print_pause(
        "Ms. Sara: 'I am busy now and I have no "
        "time for these children's games. I don't know anything about a red ring.'"
    )
    print_pause("Ms. Dyana: 'Sorry, I have no idea about any ring. I cannot help you.'")
    print_pause(
        "Ms. Lana: 'Are you kidding me? A lost ring? "
        "If your ring gets lost, just buy another one.'"
    )
    print_pause("What will you do now?")
    print_pause("1- Shed light on the truth")
    print_pause("2- Play again to remember some information")
    ch = choice()
    global score
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        the_truth2()
    else:
        print("Good choice, " + x + "! Your score is " + str(score))
        situ2()


def the_truth2():
    print_pause("The ring thief is:")
    print_pause("1- Ms. Sara")
    print_pause("2- Another one")
    global score
    ch = choice()
    if ch == "1":
        print(
            "Congratulations, " + x + "! You win. Sara is the thief because when "
            "you asked her about the ring, she said she didn't"
            " know anything about a red ring."
        )
        global current_time
        current_time1 = datetime.datetime.now()
        print(
            "Your score is: "
            + str(score + 50)
            + " out of 100 and you took "
            + str(current_time1 - current_time)
            + " to find the solution."
        )
        print("(1) Play another game?")
        print("(2) Stop playing.")
        ch = choice()
        if ch == "1":
            random.choice([sit1, sit3])()
        else:
            print("Thank you for playing!")
    else:
        print_pause("1- Ms. Dyana")
        print_pause("2- Ms. Lana")

        ch = choice()
        if ch == "1":
            current_time1 = datetime.datetime.now()
            print(
                "Sorry, "
                + x
                + ", you lose. Your score is "
                + str(score)
                + " out of 100 and you took "
                + str(current_time1 - current_time)
                + " to find the solution."
            )
            print(
                "Sara is the thief because when you asked her"
                " about the ring, she said she didn't know anything about a red ring."
            )
            print(
                "Even though you didn't ask about a red ring, you just said 'a ring'."
            )
        else:
            current_time1 = datetime.datetime.now()
            print(
                "Sorry, "
                + x
                + ", you lose. Your score is "
                + str(score)
                + " out of 100 and you took "
                + str(current_time1 - current_time)
                + " to find the solution."
            )
            print(
                "Sara is the thief because when you "
                "asked her about the ring, she said she didn't know anything about a red ring."
            )
            print(
                "Even though you didn't ask about a red ring, you just said 'a ring'."
            )


def sit3():
    global current_time
    global score
    score = 0
    current_time = datetime.datetime.now()
    print("Hi ", x)
    print_pause(
        "When you were staying in your office, someone knocked on the door and said, "
        "'Please help me find my son. "
        "I heard that you are a great detective.'  You paused for a moment, "
    )
    print_pause(
        "considering the situation, and asked her for more details. "
        "She then mentioned that her son had left only one message and requested that "
        "you come to her house to investigate the clues there."
    )
    print_pause("What will you do now:")
    print_pause("(1) Ask her to show you the message.")
    print_pause("(2) Visit her house and investigate.")
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        show_message()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        visit_home()


def show_message():
    global score
    print_pause(
        "The message is 'Sorry I left because I think "
        "you did not care about me, so I will "
        "leave for you a puzzle to test your knowledge about your son. The puzzle is "
        "'the other message in my biggest A'."
    )
    print_pause("What will you do now:")
    print_pause("(1) Ask her about her son and his interests.")
    print_pause("(2) Visit her house and investigate further.")
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        about_son()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        visit_home()


# Rest of the code...
def visit_home():
    print_pause(
        "You enter his room and find a big poster "
        "containing 5 flags of different countries. "
        "Among those flags, there is a flag that is "
        "bigger than the others and has the number 1998. "
        "Other than this, there is nothing special."
    )
    print_pause("What will you do now?")
    print_pause("(1) Ask her about her son and his interests.")
    print_pause("(2) Share your inference.")
    global score
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        about_son()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        inference()


def about_son():
    print_pause(
        "She says, 'I believe my son has a passion for football, and "
        "I believe he also enjoys watching anime. His favorite anime is 'Detective Conan'."
    )
    print_pause(
        "His bond with his father used to be incredibly strong, "
        "but unfortunately, his father passed away in 1998 "
        "while they were together in France."
    )
    print_pause("What will you do now?")
    print_pause("(1) Share your inference.")
    print_pause("(2) Visit his room.")
    global score
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        inference()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        visit_home()


def inference():
    print_pause(
        "After assimilating all this information,"
        " it strikes you that his room's poster"
        " prominently displayed the flag of France,"
        " which was the largest."
    )
    print_pause(
        "You also recall that he has a love for football, "
        "and in the year his father passed away, 1998, France emerged as"
        " the victorious team in the World Cup, which took place in France."
    )
    print_pause(
        "By piecing together these details, you come to the "
        "conclusion that both the son and his father were ardent "
        "supporters of the French national team."
    )
    print_pause(
        "Suddenly, the significance of the phrase 'my biggest A' becomes clear to you."
    )
    print_pause("Do you now know what is meant by 'my biggest A'?")
    print_pause("(1) Eiffel Tower")
    print_pause("(2) The letter 'A' in the word 'France'.")
    global score
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        eiffel()
    else:
        print("Good choice, " + x + "! Your score is " + str(score))
        letter()


def eiffel():
    global score
    global current_time
    current_time1 = datetime.datetime.now()
    print(
        "Congratulations, "
        + x
        + "! Your score is: "
        + str(score + 50)
        + " and you took "
        + str(current_time1 - current_time)
        + " to find the solution."
    )
    print()
    print_pause(
        "Eiffel Tower is true and it means that he has"
        " a miniature model of the Eiffel Tower and the other message is inside it."
    )
    print_pause(
        "Now, as you search his room once more, you"
        " come across a miniature model of the Eiffel Tower hidden in his wardrobe."
    )
    print_pause(
        "To your surprise, inside the tower, you find "
        "a message that reads, 'Thank you, Mom, for always caring about me.'"
    )
    print_pause(
        "I'm currently on a visit to Russia to watch the"
        " final of the World Cup between France and Croatia on July 15, 2018."
    )
    print_pause(
        "I will return after the event. This reminds me "
        "of the wonderful days I spent with my father.'"
    )
    print_pause("(1) Play another game.")
    print_pause("(2) Stop playing.")
    ch = choice()
    if ch == "1":
        random.choice([sit1, situ2()])()
    else:
        print("Thank you for playing!")


def letter():
    global score
    global current_time
    current_time1 = datetime.datetime.now()
    print(
        "Sorry, "
        + x
        + ", you lost. Your score is "
        + str(score)
        + " and you took "
        + str(current_time1 - current_time)
        + " to find the solution."
    )
    print_pause(
        "It is not true because it does not make "
        "sense that the other message is in 'France' and you i"
        "gnore the word 'my biggest'."
    )
    print_pause(
        "Eiffel Tower is true and it means that he has a "
        "miniature model of the Eiffel Tower and the other message is inside it."
    )
    print_pause(
        "Now, as you search his room once more, you come"
        " across a miniature model of the Eiffel Tower hidden in his wardrobe."
    )
    print_pause(
        "To your surprise, inside the tower, you find a "
        "message that reads, 'Thank you, Mom, for always caring about me.'"
    )
    print_pause(
        "I'm currently on a visit to Russia to watch "
        "the final of the World Cup between France and Croatia on July 15, 2018."
    )
    print_pause(
        "I will return after the event. This reminds me of"
        " the wonderful days I spent with my father.'"
    )
    print_pause("(1) Play another game.")
    print_pause("(2) Stop playing.")
    ch = choice()
    if ch == "1":
        random.choice([sit1, sit3])()
    else:
        print("Thank you for playing this game.")


def sit3():
    global current_time
    global score
    score = 0
    current_time = datetime.datetime.now()
    global x
    print("Hi ", x)

    print_pause(
        "When you were staying in your office, someone knocked on the door and said, "
        "'Please help me find my son. "
        "I heard that you are a great detective.'  You paused for a moment, "
    )
    print_pause(
        "considering the situation, and asked her for more details. "
        "She then mentioned that her son had left only one message and requested that "
        "you come to her house to investigate the clues there."
    )
    print_pause("What will you do now:")
    print_pause("(1) Ask her to show you the message.")
    print_pause("(2) Visit her house and investigate.")
    ch = choice()
    if ch == "1":
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        show_message()
    else:
        score += 10
        print("Good choice, " + x + "! Your score is " + str(score))
        visit_home()


# Main game loop
while True:
    print_pause("This is a website to make all things clear. I have created it.")
    print_pause("https://a7h7m7e7d.github.io/DECI/web.html")
    sleep(2)
    random.choice([sit1, situ2, sit3])()
    break
