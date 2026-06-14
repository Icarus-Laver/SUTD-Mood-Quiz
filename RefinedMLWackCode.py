def question_1():
    answer = input("1. Are you an SUTDent? \nA.Yes, I am from NUS \nB.What is SUTDent \nC.NO \nD.YES I LOVE SUTD \n\nYour Answer: ")
    #print(type(answer))

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_1()
    
    elif answer.upper() == 'A':
        mood[3] += 1 
    elif answer.upper() == 'B':
        mood[2] += 1
        mood[8] += 1
    elif answer.upper() == 'C':
        mood[4] += 1 
    elif answer.upper() == 'D':
        mood[1] += 1
        mood[5] += 1 
        mood[7] += 1 
        mood[10] += 1 
        mood[11] += 1 

def question_2():
    answer = input("2. Which term are you in? \nA.Term 1 \nB.Term 3 \nC.I lost count \nD.Who cares? I’m dropping out soon \n\nYour Answer: ")
    #print(type(answer))

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_2()
    
    elif answer.upper() == 'A':
        mood[1] += 1 
        mood[5] += 1
        mood[7] += 1 
        mood[10] += 1
        mood[11] += 1 
    elif answer.upper() == 'B':
        mood[2] += 1
        mood[6] += 1 
        mood[8] += 1
    elif answer.upper() == 'C':
        mood[4] += 1
        mood[8] += 1
    elif answer.upper() == 'D':
        mood[3] += 1

def question_3():
    answer = input("3. Which pillar are you in/interested in? \nA.ASD \nB.ISTD/CSD \nC.EPD \nD.ESD \nE.DAI \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_3()
    
    elif answer.upper() == 'A':
        mood[4] += 1 
        mood[6] += 1
        mood[8] += 1 
        mood[9] += 1
    elif answer.upper() == 'B':
        mood[2] += 1
        mood[3] += 1 
        mood[7] += 1
        mood[11] += 1
    elif answer.upper() == 'C':
        mood[5] += 1
        mood[7] += 1
    elif answer.upper() == 'D':
        mood[1] += 1
        mood[10] += 1
    elif answer.upper() == 'E':
        mood[8] += 1
        mood[10] += 1

def question_4():
    answer = input("4. How would you deal with academic pressure? \nA.What academic pressure =D \nB.Optimistic reaction to any pressure \nC.*ignore* Going to my fifth row right now >:( \nD.Negative attitude towards stress \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_4()
    
    elif answer.upper() == 'A':
        mood[7] += 1 
        mood[10] += 1
        mood[11] += 1 
    elif answer.upper() == 'B':
        mood[1] += 1
        mood[5] += 1 
        mood[11] += 1
    elif answer.upper() == 'C':
        mood[3] += 1
    elif answer.upper() == 'D':
        mood[2] += 1
        mood[4] += 1
        mood[6] += 1
        mood[8] += 1
        mood[9] += 1

def question_5():
    answer = input("5. Do you arrive for your lectures on time? \nA.Always on time \nB.Always late \nC.Never attend \nD.Only attend before exams \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_5()
    
    elif answer.upper() == 'A':
        mood[5] += 1 
        mood[11] += 1 
    elif answer.upper() == 'B':
        mood[4] += 1
        mood[8] += 1 
    elif answer.upper() == 'C':
        mood[7] += 1
    elif answer.upper() == 'D':
        mood[3] += 1
        mood[6] += 1
        mood[9] += 1
        mood[10] += 1

def question_6():
    answer = input("6. What stationery do you use for taking notes? \nA.iPad \nB.My blood and tears \nC.I don’t even go to class \nD.Who takes notes? \nE.Pen and paper (like the old times) \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_6()
    
    elif answer.upper() == 'A':
        mood[1] += 1
        mood[2] += 1 
        mood[5] += 1 
        mood[11] += 1 
    elif answer.upper() == 'B':
        mood[4] += 1
 
    elif answer.upper() == 'C':
        mood[7] += 1
        mood[8] += 1
    elif answer.upper() == 'D':
        mood[2] += 1
        mood[5] += 1
        mood[11] += 1

def question_7():
    answer = input("7. Do you often feel lonely？ \nA.I have too many friends \nB.No, I got group project \nC.Of course not, I have my imaginary friend \nD.I can’t live without my alone time \nE.Loneliness is my only friend \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_7()
    
    elif answer.upper() == 'A':
        mood[5] += 1
        mood[8] += 1 

    elif answer.upper() == 'B':
        mood[2] += 1
        mood[6] += 1 
        mood[9] += 1 
        mood[11] += 1 
 
    elif answer.upper() == 'C':
        mood[3] += 1
        mood[9] += 1
    elif answer.upper() == 'D':
        mood[9] += 1
    elif answer.upper() == 'E':
        mood[4] += 1
        mood[9] += 1

def question_8():
    answer = input("8. What do you think are the primary psychological issues that students face? \nA.Exams \nB.Relationship problems \nC.Having an urge to murder a group mate \nD.Family issues \nE.Students don’t face issues. Wdym \nF.Stressed about finding food options on campus \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_8()
    
    elif answer.upper() == 'A':
        mood[2] += 1
        mood[4] += 1
        mood[6] += 1
        mood[8] += 1 
        mood[9] += 1 
        mood[11] += 1 

    elif answer.upper() == 'B':
        mood[4] += 1
        mood[8] += 1 
 
    elif answer.upper() == 'C':
        mood[3] += 1

    elif answer.upper() == 'D':
        mood[4] += 1
        mood[8] += 1
    elif answer.upper() == 'E':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1
    elif answer.upper() == 'F':
        mood[6] += 1
        mood[10] += 1

def question_9():
    answer = input("9. How do you feel about your mental state? \nA.What mental state? \nB.I love life \nC.#@*&%#& \nD.I am kalm *meditates* \nE.Don’t know, don’t care \nF.Every dog that passes by me gets scolded by me \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_9()
    
    elif answer.upper() == 'A':
        mood[6] += 1

    elif answer.upper() == 'B':
        mood[1] += 1
        mood[5] += 1
        mood[11] += 1 
 
    elif answer.upper() == 'C':
        mood[2] += 1
        mood[8] += 1

    elif answer.upper() == 'D':
        mood[7] += 1
        mood[10] += 1
        mood[11] += 1
        
    elif answer.upper() == 'E':
        mood[4] += 1
        mood[9] += 1

    elif answer.upper() == 'F':
        mood[3] += 1

def question_10():
    answer = input("10. Which type of group member are you? \nA.The tanker \nB.The entertainer \nC.The lost \nD.The bossy one \nE.The one who forgets about their work \nF.The anxious one \nG.The serious one \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_10()
    
    elif answer.upper() == 'A':
        mood[5] += 1
        mood[7] += 1

    elif answer.upper() == 'B':
        mood[1] += 1
        mood[11] += 1 
 
    elif answer.upper() == 'C':
        mood[4] += 1
        mood[8] += 1
        mood[9] += 1

    elif answer.upper() == 'D':
        mood[3] += 1
        mood[7] += 1
        
    elif answer.upper() == 'E':
        mood[7] += 1
        mood[8] += 1
        mood[9] += 1

    elif answer.upper() == 'F':
        mood[2] += 1
        mood[6] += 1
    elif answer.upper() == 'G':
        mood[5] += 1
        mood[10] += 1
        mood[11] += 1

def question_11():
    answer = input("11. How do you study for your exams?\n A.I don’t need to study, i will ace my exams anyway \nB.Study a bit, just need to pass somehow \nC.Study till the last minute \nD.Just use cheat sheet, no need to study \nE.I teach others \nF.I don’t need to study, my goals in life are much bigger than studying for one exam \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_11()
    
    elif answer.upper() == 'A':
        mood[7] += 1
        mood[10] += 1

    elif answer.upper() == 'B':
        mood[4] += 1
        mood[8] += 1
        mood[9] += 1 
 
    elif answer.upper() == 'C':
        mood[2] += 1
        mood[5] += 1
        mood[6] += 1
        mood[8] += 1
        mood[11] += 1

    elif answer.upper() == 'D':
        mood[7] += 1
        mood[10] += 1
        
    elif answer.upper() == 'E':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1

    elif answer.upper() == 'F':
        mood[3] += 1
        mood[7] += 1
        mood[10] += 1

def question_12():
    answer = input("12. What do you do when you have too much homework/assignment/project? \nA.Eat it \nB.Organise the time and finish them on time \nC.Give prof the puppy dog eyes for time extension \nD.Go club and drink \nE.De-stress by going to find my friends to share tea \nF.Sleep \nG.Stress about it until I can’t fall asleep \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_12()
    
    elif answer.upper() == 'A':
        mood[3] += 1
        mood[8] += 1

    elif answer.upper() == 'B':
        mood[1] += 1
        mood[5] += 1
        mood[10] += 1
 
    elif answer.upper() == 'C':
        mood[8] += 1
        mood[11] += 1

    elif answer.upper() == 'D':
        mood[4] += 1
        
    elif answer.upper() == 'E':
        mood[8] += 1

    elif answer.upper() == 'F':
        mood[7] += 1
        mood[9] += 1
        mood[10] += 1

    elif answer.upper() == 'G':
        mood[2] += 1
        mood[6] += 1
        mood[8] += 1
        mood[9] += 1

def question_13():
    answer = input("13. How many hours of sleep do you get?\n A.7 to 8 hours \nB.What is sleep? \nC.Stay Up Till Dawn \nD.>8 hours \nE.<7 hours \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_13()
    
    elif answer.upper() == 'A':
        mood[1] += 1
        mood[10] += 1
        mood[11] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
        mood[4] += 1
        mood[6] += 1
        mood[8] += 1 
 
    elif answer.upper() == 'C':
        mood[2] += 1
        mood[5] += 1
        mood[8] += 1

    elif answer.upper() == 'D':
        mood[7] += 1
        mood[9] += 1
        
    elif answer.upper() == 'E':
        mood[4] += 1
        mood[6] += 1
        mood[8] += 1

def question_14():
    answer = input("14. Picture this: A prof suddenly sends an email, telling you to re-submit your work. The prof gives you 2.5 hours to submit it and accuses you of abusing your class rep. What would you do?\n A.I do it properly and submit it on time \nB.I email the prof, telling him/her to re-submit their lecture video to me \nC.I don’t give a #@*&%#& \nD.I don’t read my emails \nE.I sleep and think about it tomorrow \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_14()
    
    elif answer.upper() == 'A':
        mood[2] += 1
        mood[5] += 1
        mood[6] += 1
        mood[10] += 1
        mood[11] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
 
    elif answer.upper() == 'C':
        mood[3] += 1

    elif answer.upper() == 'D':
        mood[4] += 1
        mood[8] += 1
        mood[9] += 1
        
    elif answer.upper() == 'E':
        mood[1] += 1

def question_15():
    answer = input("15. What would you do if you haven’t started an assignment that is due tomorrow?\n A.Due tomorrow, Do tomorrow \nB.Don’t do the assignment at all \nC.Somehow finish \nD.Somehow finish \nE.Email the prof for a time extension \n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_15()
    
    elif answer.upper() == 'A':
        mood[7] += 1
        mood[9] += 1
        mood[10] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
 
    elif answer.upper() == 'C':
        mood[4] += 1
        mood[5] += 1
        mood[9] += 1
        mood[10] += 1
        mood[11] += 1

    elif answer.upper() == 'D':
        mood[1] += 1
        mood[2] += 1
        mood[5] += 1
        mood[11] += 1
        
    elif answer.upper() == 'E':
        mood[6] += 1
        mood[8] += 1
        mood[11] += 1

def question_16():
    answer = input("16. Are you satisfied with your dormitory life?\n A.I LOVE DORM\nB.Ready to move out. Anytime now…\nC.I don’t even stay in dorm\nD.Facilities here are trash, my home ftw\nE.It’s been alright\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_16()
    
    elif answer.upper() == 'A':
        mood[1] += 1
        mood[5] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
        mood[9] += 1
 
    elif answer.upper() == 'C':
        mood[4] += 1

    elif answer.upper() == 'D':
        mood[8] += 1
        mood[9] += 1
        
    elif answer.upper() == 'E':
        mood[2] += 1
        mood[6] += 1
        mood[10] += 1
        mood[11] += 1

def question_17():
    answer = input("17. How would you deal with a friend/group mate who irritates you?\n A.Talk shit about them behind their backs\nB.Punch them\nC.Be nice to them anyway\nD.Ignore them, not worth my time\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_17()
    
    elif answer.upper() == 'A':
        mood[3] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
 
    elif answer.upper() == 'C':
        mood[1] += 1
        mood[9] += 1
        mood[11] += 1
        
    elif answer.upper() == 'D':
        mood[4] += 1
        mood[6] += 1
        mood[10] += 1

def question_18():
    answer = input("18. 15 minutes before an exam ……………\n A.All prepared\nB.Trying to find out the subject which I have to write the exam for\nC.Still studying\nD.Explaining a concept to my friends\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_18()
    
    elif answer.upper() == 'A':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
        mood[8] += 1
 
    elif answer.upper() == 'C':
        mood[2] += 1
        mood[6] += 1
        mood[9] += 1
        mood[11] += 1
        
    elif answer.upper() == 'D':
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1

def question_19():
    answer = input("19. Are you okay?\nA.No \nB.Of course\nC.Of course (but delulu)\nD.I need help\nE.Life has been great to me\nF.Meh\nG.Life is life *shrugs* but I’m managing\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_19()
    
    elif answer.upper() == 'A':
        mood[3] += 1
        mood[6] += 1
        mood[9] += 1

    elif answer.upper() == 'B':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1
 
    elif answer.upper() == 'C':
        mood[4] += 1
        mood[8] += 1
        mood[9] += 1

    elif answer.upper() == 'D':
        mood[2] += 1
        mood[6] += 1
        mood[8] += 1
        
    elif answer.upper() == 'E':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1
        mood[11] += 1

    elif answer.upper() == 'F':
        mood[4] += 1
        mood[9] += 1

    elif answer.upper() == 'G':
        mood[10] += 1
        mood[11] += 1

def question_20():
    answer = input("1 + 1 =\n A.2\nB.3\nC.My wallet balance\nD.My hair\nE.The number of friends I have\nF.Existential crisis\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_20()
    
    elif answer.upper() == 'A':
        mood[1] += 1
        mood[5] += 1
        mood[7] += 1
        mood[10] += 1

    elif answer.upper() == 'B':
        mood[3] += 1
        mood[8] += 1
 
    elif answer.upper() == 'C':
        mood[6] += 1

    elif answer.upper() == 'D':
        mood[2] += 1
        
    elif answer.upper() == 'E':
        mood[4] += 1
        mood[9] += 1

    elif answer.upper() == 'F':
        mood[2] += 1
        mood[6] += 1

def question_21():
    answer = input("21. Do you eat supper?\nA.No, I have no friends :’(\nB.Of course, can’t go without supper\nC.No, I never get hungry at night\nD.I sleep early\nE.Maggi\nF.I go to supper to stir shit\nG.I go to supper to listen to tea\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_21()
    
    elif answer.upper() == 'A':
        mood[4] += 1
        mood[9] += 1
        
    elif answer.upper() == 'B':
        mood[5] += 1
        mood[7] += 1
        mood[11] += 1
 
    elif answer.upper() == 'C':
        mood[4] += 1

    elif answer.upper() == 'D':
        mood[7] += 1
        mood[10] += 1
        
    elif answer.upper() == 'E':
        mood[1] += 1
        mood[6] += 1

    elif answer.upper() == 'F':
        mood[2] += 1
        mood[3] += 1
        mood[7] += 1

    elif answer.upper() == 'G':
        mood[3] += 1
        mood[7] += 1

def question_22():
    answer = input("22. What do you think of this game?\n A.DUMB\nB.Funny\nC.I need help\nD.Love it, you guys should make more\nE.I never want to do this again\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_22()
    
    elif answer.upper() == 'A':
        mood[3] += 1
        
    elif answer.upper() == 'B':
        mood[1] += 1
        mood[7] += 1
        mood[10] += 1
 
    elif answer.upper() == 'C':
        mood[2] += 1
        mood[4] += 1
        mood[6] += 1
        mood[9] += 1

    elif answer.upper() == 'D':
        mood[1] += 1
        mood[5] += 1
        mood[10] += 1
        mood[11] += 1
        
    elif answer.upper() == 'E':
        mood[3] += 1
        mood[4] += 1
        mood[8] += 1

def question_23():
    answer = input("23. What do you do if the queue at the canteen is too long , but you are hungry?\nA.Give up, just don’t eat\nB.I wait\nC.Cut queue\nD.Go back and eat instant noodle\nE.I steal my friend’s food\nF..*sigh and walk to GOMGOM*\nG.I eat my friend *YUM*!\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_23()
    
    elif answer.upper() == 'A':
        mood[2] += 1
        mood[4] += 1
        mood[6] += 1
        mood[8] += 1
        mood[9] += 1
        
    elif answer.upper() == 'B':
        mood[1] += 1
        mood[5] += 1
        mood[10] += 1
        mood[11] += 1
 
    elif answer.upper() == 'C':
        mood[3] += 1

    elif answer.upper() == 'D':
        mood[4] += 1
        mood[6] += 1
        mood[9] += 1
        
    elif answer.upper() == 'E':
        mood[3] += 1

    elif answer.upper() == 'F':
        mood[10] += 1

    elif answer.upper() == 'G':
        mood[3] += 1

def question_24():
    answer = input("24. What do you do when you don’t understand a topic taught in class?\n A.*ignore* and hope that it is never tested in the exam\nB.Reread the notes and figure it out myself-\nC.Complain about it to the prof\nD.Ask around\nE.Ask TA for help\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_24()
    
    elif answer.upper() == 'A':
        mood[4] += 1
        mood[8] += 1

    elif answer.upper() == 'B':
        mood[5] += 1
        mood[7] += 1
        mood[9] += 1
        mood[10] += 1
 
    elif answer.upper() == 'C':
        mood[3] += 1

    elif answer.upper() == 'D':
        mood[1] += 1
        mood[2] += 1
        mood[5] += 1
        mood[6] += 1
        mood[11] += 1
        
    elif answer.upper() == 'E':
        mood[1] += 1
        mood[2] += 1
        mood[5] += 1
        mood[6] += 1
        mood[11] += 1

def question_25():
    answer = input("25. What do you do in your free time?\nA.Study with friends\nB.Play mobile legend, BANG BANG!\nC.Sleepzzz\nD.Stay in the classroom to mug\nE.Find people to disturb\nF.Go out with friends\nG.Go clubbing\n\nYour Answer: ")

    if answer.upper() != 'A' and answer != 'B' and answer != 'C' and answer != 'D' and answer != 'E' and answer != 'F' and answer != 'G':
        print("You RETARD! CORRECT LETTERS ONLY")
        question_25()
    
    elif answer.upper() == 'A':
        mood[5] += 1
        mood[11] += 1
        
    elif answer.upper() == 'B':
        mood[1] += 1
        mood[7] += 1
        mood[10] += 1
 
    elif answer.upper() == 'C':
        mood[1] += 1
        mood[4] += 1
        mood[6] += 1
        mood[7] += 1
        mood[8] += 1
        mood[9] += 1
        mood[10] += 1

    elif answer.upper() == 'D':
        mood[2] += 1
        
    elif answer.upper() == 'E':
        mood[3] += 1
        mood[7] += 1

    elif answer.upper() == 'F':
        mood[1] += 1
        mood[7] += 1
        mood[8] += 1

    elif answer.upper() == 'G':
        mood[6] += 1
        mood[7] += 1

def quit_game():
    would_like_to_exit_game = input("Would you like to touch grass outside? \n 1) Yes \n 2) No \n Your Answer: ")
    if would_like_to_exit_game != '1' and would_like_to_exit_game != '2':
        print("You RETARD! 1 or 2 ONLY")
        quit_game()
    else: 
        return would_like_to_exit_game

mood ={ 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0 }

def get_highest_mood():
    highest_mood = max(mood, key=mood.get)
    print(highest_mood)
    if highest_mood == 1:
        print("Your mood is Joyful")
    elif highest_mood == 2:
        print("Your mood is Anxious")
    elif highest_mood == 3:
        print("Your mood is Irritable")
    elif highest_mood == 4:
        print("Your mood is Depressed")
    elif highest_mood == 5:
        print("Your mood is Motivated")
    elif highest_mood == 6:
        print("Your mood is Stressed")
    elif highest_mood == 7:
        print("Your mood is Confident")
    elif highest_mood == 8:
        print("Your mood is Overwhelmed")
    elif highest_mood == 9:
        print("Your mood is Lonely")
    elif highest_mood == 10:
        print("Your mood is Calm")
    elif highest_mood == 11:
        print("Your mood is Hopeful")
    else:
        print("You are having Mood Swings")



would_like_to_exit_game = '2'
while would_like_to_exit_game == '2' :
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()
    question_21()
    question_22()
    question_23()
    question_24()
    question_25()
    print(mood)
    get_highest_mood()
    would_like_to_exit_game = quit_game()
    