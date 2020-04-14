#-------------------------------------------------------------------------------
# Name:        IT Networking and Systems Administration
#              Assessment Application
# Version:     v1.0
#
# Purpose:     To brief and test the user's knowledge of basic topics and
#              aspects covered in the IT Networking & Systems Administration
#              Competition
#
# Author:      Alvin. R
#
# Created:     25/05/2014
# Licence:     Educational
#-------------------------------------------------------------------------------

# Imports pygame module.
import pygame
import time
import math

# Initializes pygame.
pygame.init()

# Defining some colors for later. RGB color-coding used.
# Also defining some variables for further usage.
skyblue = (103, 159, 232)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)
clicks = 0
choice = " "
correct_answers = 0

# Initializing some fonts.
solotext = pygame.font.SysFont("Times New Roman", 25)
endquiztext = pygame.font.SysFont("Times New Roman", 40)

# Defining and setting screen size.
# For debug purposes. Please switch back to pygame.FULLSCREEN.
size = (1024, 768)
screen = pygame.display.set_mode((size),pygame.FULLSCREEN)

# For windowed mode, 1024 x 768
#screen = pygame.display.set_mode(size)

# Screen Title/caption.
pygame.display.set_caption("ITN&SA Assessment App")

#Loop count variables.
done = False
done_quiz = False
done_tut = False
calculate = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Dictionary for storing USER Answers.
user_answers = {
1 : '   ',
2 : '   ',
3 : '   ',
4 : '   ',
5 : '   ',
6 : '   ',
7 : '   ',
8 : '   ',
9 : '   ',
10 : '   ',
11 : '   ',
12 : '   ',
13 : '   ',
14 : '   ',
15 : '   ',
16 : '   ',
17 : '   ',
18 : '   ',
19 : '   ',
20 : '   ',
21 : '   ',
22 : '   ',
23 : '   ',
24 : '   ',
25 : '   '
}
# Dictionary for comparing User Answers (ANSWERS).
answers = {
1 : 'c',
2 : 'f',
3 : 'c',
4 : 'b',
5 : 'f',
6 : 'b',
7 : 'f',
8 : 'c',
9 : 'f',
10 : 'b',
11 : 'c',
12 : 'f',
13 : 'd',
14 : 'f',
15 : 'f',
16 : 'a',
17 : 'd',
18 : 't',
19 : 'c',
20 : 't',
21 : 'd',
22 : 'f',
23 : 'c',
24 : 'a',
25 : 'c'
}

# Starts Timer
start_time = time.time()

# MAIN PROGRAM HERE!
while not done:
    # Main events go here.
    for event in pygame.event.get():
        # Closes window when user clicks exit.
        if event.type == pygame.QUIT:
            exitprompt = pygame.image.load("etc/exitprompt.jpg")
            screen.blit(exitprompt, (259, 225))
            pygame.display.flip()
            # Draws prompt, asking if user is SURE they want to quit.
            for event in pygame.event.get():
                if event.type is pygame.KEYDOWN:
                    exit_choice = pygame.key.name(event.key)
                    if exit_choice == "y":
                        done = True
                    elif exit_choice == "n":
                        break
                    else:
                        pass
        # Displays informative text when user mouses over object in Main Menu.
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            pos = pygame.mouse.get_pos()
            if (x in range(90, 474)) and (y in range(220, 308)):
                endscreen = pygame.image.load("menutext/menutext_tutorial.png")
                screen.blit(endscreen, (562, 233))
                pygame.display.flip()
            elif (x in range(90, 394)) and (y in range(373, 461)):
                endscreen = pygame.image.load("menutext/menutext_assessment.png")
                screen.blit(endscreen, (562, 391))
                pygame.display.flip()
            elif (x in range(89, 334)) and (y in range(500, 583)):
                endscreen = pygame.image.load("menutext/menutext_exit.png")
                screen.blit(endscreen, (562, 544))
                pygame.display.flip()
        # IF the user clicks within the "tuturial button" area, begin tutorial.
        if event.type == pygame.MOUSEBUTTONDOWN:
            done_tut = False
            x, y = event.pos
            pos = pygame.mouse.get_pos()
            print pos
            if (x in range(90, 474)) and (y in range(220, 308)):
                slide = 1
                slide_num = str(slide)
                slide_name = "tutorial_slides/" + slide_num + "t.jpg"
                # Here is where the slide-changing happens!
                # Python iterates through a loop, everytime user wants to
                # proceed, 1 is added to count. Likewise if they want to go
                # back - subtract 1. Then, loop back to the beginning, and
                # cocatinate the count(slide) value with the file extension
                # to draw the appropreate question slide.
                while not done_tut:
                    slide_num = str(slide)
                    slide_name = "tutorial_slides/"+slide_num+"t.jpg"
                    slide_screen = pygame.image.load(slide_name)
                    screen.blit(slide_screen, imagerect)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done_tut = True
                            done = True
                        # Mouse over detection, will display a small help-text.
                        if event.type is pygame.MOUSEMOTION:
                            x, y = event.pos
                            pos = pygame.mouse.get_pos()
                            if (x in range(53,221)) and (y in range(47, 84)):
                                help = pygame.image.load("etc/tuthelp.png")
                                screen.blit(help, (64, 91))
                                pygame.display.flip()
                        # Navigation bar segment - control for buttons.
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            pos = pygame.mouse.get_pos()
                            print pos
                            print slide
                            if (x in range(41,244)) and (y in range(675, 737)):
                                done_tut = True
                                break
                            elif (x in range (550,749)) and (y in range (675,737)):
                                if slide < 5 and slide != 1:
                                    slide -= 1
                                    slide_num = str(slide)
                                    print "The new slide number is: ", slide
                            elif (x in range(784,985)) and (y in range(675, 737 )):
                                if slide < 4 and slide >= 1:
                                    slide = slide + 1
                                    slide_num = str(slide)
                                    print "The new slide number is: ", slide
                        break
                # Slide-changing code ends here!
            # Quiz-Segment begns HERE!
            elif (x in range(90, 394)) and (y in range(373, 461)):
                done_quiz = False
                done = False
                user_review = False
                calculate = False
                correct_answers == 0
                slide = 0
                slide_num = str(slide)
                slide_name = "assessment_slides/" + slide_num + ".jpg"
                # Here is where the slide-changing happens!
                # Python iterates through a loop, everytime user wants to
                # proceed, 1 is added to count. Likewise if they want to go
                # back - subtract 1. Then, loop back to the beginning, and
                # cocatinate the count(slide) value with the file extension
                # to draw the appropreate question slide.
                while not done_quiz:
                    choice_output = solotext.render("You Chose: ",1,(grey))
                    choice_key = solotext.render(choice,1,(grey))
                    slide_num = str(slide)
                    slide_name = "assessment_slides/"+slide_num+".jpg"
                    slide_screen = pygame.image.load(slide_name)
                    screen.blit(slide_screen, imagerect)
                    if slide <= 25 and slide != 0:
                        screen.blit(choice_output, (753, 595))
                        screen.blit(choice_key, (875, 595))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        # Mouse over detection, will display a small help-text.
                        if event.type is pygame.MOUSEMOTION:
                            x, y = event.pos
                            pos = pygame.mouse.get_pos()
                            if (x in range(53,221)) and (y in range(47, 84)):
                                help = pygame.image.load("etc/quizhelp.png")
                                screen.blit(help, (64, 91))
                                pygame.display.flip()
                        if event.type is pygame.KEYDOWN:
                            choice = pygame.key.name(event.key)
                            if slide <= 25 and slide != 0:
                                user_answers[slide] = choice
                        if event.type == pygame.QUIT:
                            done_quiz = True
                            done = True
                        # Navigation bar segment - control for buttons.
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            pos = pygame.mouse.get_pos()
                            print pos
                            if (x in range(41,244)) and (y in range(675, 737)):
                                user_wants_to_exit = False
                                exitprompt = pygame.image.load("etc/exitprompt.jpg")
                                screen.blit(exitprompt, (259, 225))
                                pygame.display.flip()
                                # Draws prompt, asking if user is SURE they want to quit.
                                while not user_wants_to_exit:
                                    for event in pygame.event.get():
                                        if event.type is pygame.KEYDOWN:
                                            exit_choice = pygame.key.name(event.key)
                                            if exit_choice == "y":
                                                user_wants_to_exit = True
                                                done_quiz = True
                                            elif exit_choice == "n":
                                                user_wants_to_exit = True
                                                break
                                            else:
                                                pass
                                        break
                            # If user initiates previous, decrease slide count.
                            elif (x in range (550,749)) and (y in range (675,737)):
                                if slide < 25 and slide != 0:
                                    slide -= 1
                                    slide_num = str(slide)
                                    print "The new slide number is: ", slide
                            # If this is the FINAL SLIDE, do the following:
                            # - Calculate score out of 25.
                            # - Calculate percentage.
                            # - Calculate letter-grade.
                            # - Calculate time elapsed.
                            # - Write information to a text-file in the local
                            #   code directory.
                            elif (x in range(784,985)) and (y in range(675, 737 )):
                                if slide == 26:
                                    print user_answers
                                    if not calculate:
                                        for key in set(user_answers) & set(answers):
                                            if user_answers[key] == answers[key]:
                                                correct_answers += 1
                                        correct_answersDisplay = str(correct_answers)
                                        percent4 = float(correct_answers) / (25)
                                        percent3 = percent4 * 100
                                        percent2 = math.floor(percent3)
                                        percent = int(percent2)
                                        print percent
                                        percent_Display = str(percent)
                                        if percent >= 85 and percent < 101:
                                            score_level = "A"
                                        elif percent >= 75 and percent < 85:
                                            score_level = "B"
                                        elif percent >= 65 and percent < 75:
                                            score_level = "C"
                                        elif percent >= 55 and percent < 65:
                                            score_level = "D"
                                        elif percent >= 0 and percent < 55:
                                            score_level = "F"
                                        else:
                                            score_level = "?"
                                        grade = score_level
                                        timeStore = str(round(time.time() - start_time))
                                        time_output = timeStore + " Seconds"
                                        score_write = "You scored: " + correct_answersDisplay + "/25"
                                        percent_write = "You scored a percentage of: " + percent_Display + "%"
                                        grade_write = "You scored a letter-grade of: " + grade
                                        time_write = "You took: " + str(round(time.time() - start_time, 2)) + " seconds to complete the Assessment."
                                        calculate = True
                                    # File-writing happens here!
                                    with open("results.txt", "w") as f:
                                        f.write ('The results for your Assessment are as follows:\n')
                                        f.write (' \n')
                                        f.write (score_write)
                                        f.write (' \n')
                                        f.write (percent_write)
                                        f.write (' \n')
                                        f.write (grade_write)
                                        f.write (' \n')
                                        f.write (time_write)
                                        f.write (' \n')
                                        f.write ('-     -     -     -     - \n')
                                        for key, value in dict.items(user_answers):
                                            f.write ('For Question %s , your answer was: %s .\n' % (key, value))
                                        f.write (' \n')
                                        for key, value in dict.items(answers):
                                            f.write ('For Question %s , the correct answer was: %s .\n' % (key, value))
                                    # Draws score, percent, letter-grade, and time to screen.
                                    while not user_review:
                                        score = endquiztext.render(correct_answersDisplay, 1, (grey))
                                        score_percent = endquiztext.render(percent_Display, 1, (grey))
                                        score_time = endquiztext.render(time_output, 1, (grey))
                                        score_grade = endquiztext.render(grade, 1, (grey))
                                        screen.blit(score, (490, 213))
                                        screen.blit(score_percent, (500, 263))
                                        screen.blit(score_time, (251, 359))
                                        screen.blit(score_grade, (514, 311))
                                        pygame.display.flip()
                                        # Give user only choice of exitting back to menuscreen.
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                x, y = event.pos
                                                pos = pygame.mouse.get_pos()
                                                print pos
                                                if (x in range(41,244)) and (y in range(675, 737)):
                                                    user_review = True
                                                    done_quiz = True
                                                    break
                                # If user initiates next, increase slide count.
                                elif slide <= 25 and slide >= 0:
                                    slide = slide + 1
                                    slide_num = str(slide)
                                    print "The new slide number is: ", slide
                        break
                # End of Slide-Changing Code, AND the Quiz-Segment.
            # Begin end-application with a confirmation prompt.
            elif (x in range(89, 334)) and (y in range(500, 583)):
                user_wants_to_exit = False
                exitprompt = pygame.image.load("etc/exitprompt.jpg")
                screen.blit(exitprompt, (259, 225))
                pygame.display.flip()
                user_wants_to_exit = False
                while not user_wants_to_exit:
                    for event in pygame.event.get():
                        user_wants_to_exit = False
                        exitprompt = pygame.image.load("etc/exitprompt.jpg")
                        screen.blit(exitprompt, (259, 225))
                        pygame.display.flip()
                        if event.type is pygame.KEYDOWN:
                            exit_choice = pygame.key.name(event.key)
                            if exit_choice == "y":
                                user_wants_to_exit = True
                                done = True
                            elif exit_choice == "n":
                                user_wants_to_exit = True
                                break
                            else:
                                pass
                        break
    # Draws menu screen
    screen.fill(skyblue)
    menu = pygame.image.load("menu.jpg")
    imagerect = menu.get_rect()
    screen.blit(menu, imagerect)

    # Updates screen & limits FPS to 60.
    pygame.display.flip()
    clock.tick(60)
# Draws end-screen.
endscreen = pygame.image.load("etc/end.jpg")
screen.blit(endscreen, imagerect)
pygame.display.flip()
time.sleep(2)
# Terminates program.
pygame.quit()
