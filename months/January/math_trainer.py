""" This program is for teaching times tables,creating a quizzes, and printing
facts"""

#Imports
import random
import sys 


#Constants
TEST_QUESTION = (4,6)
QUESTION_TEMPLATE = "What is %sx%s? "
LOWER = 1
UPPER = 12
MAX_QUESTIONS = 3
TIMES_TABLE_ENTRY = "%2s x %2s = %3s "
INSTRUCTIONS = """Welcome to math trainer. This application will train you
               on your times tables. It can either print oneor more of the tables
               for you so that you can revise (training) or it can test
               your times tables. """
CONFIRM_QUIT_MESSAGE = "Are you sure you want to quit (Y/n)? "


#Function
def make_question_list(lower=LOWER, upper=UPPER, random_order=True):
    """ making a list of all possible questions for times table 1-12
    and in random order when random order = true"""
    
    
    spam =[(x+1, y+1) for x in range(lower-1,upper)
                      for y in range(lower-1,upper)]
    if random_order:
        random.shuffle(spam)
        return spam
def do_testing():
    score = 0
    question_list = make_question_list()
    for i, question in enumerate(question_list):
        if i >=MAX_QUESTIONS:
            break
        prompt = QUESTION_TEMPLATE%question
        correct_answer = question[0] * question[1]
        answer = input(prompt)
        if int(answer) == correct_answer:
            print("Correct!")
            score = score+1
        else:
            print("Incorrect,should have been %s"%(correct_answer))

    print("you scored %s"%score)

def display_times_tables(upper=UPPER):
    """display times tables up to UPPER"""
    tables_per_line = 5
    tables_to_print = range(1, upper+1)
    #GET A BATCH OF 5 TO PRINT
    batch = tables_to_print[:tables_per_line]
    #REMOVE THEM FROM THE LIST
    tables_to_print = tables_to_print[tables_per_line:]
    while batch != []:
        for x in range (1, upper+1):
            accumulator = []
            for y in batch:
                #this covers only the tables in the batch
                #it builds the columns
                accumulator.append(TIMES_TABLE_ENTRY%(y, x, x*y))
            print(" ".join(accumulator))
        print("\n") #vertical seperation between blocks of tables
        #now get another line and repeat
        batch = tables_to_print[:tables_per_line]
        tables_to_print = tables_to_print[tables_per_line:]
        break
                                   
            #entry = TIMES_TABLE_ENTRY%(x+1, y+1,(x+1)*(y+1))
            #print(entry)

def do_quit():
    """quit the application"""
    if confirm_quit():
        sys.exit()
    print("In Quit (not quitting, returning!)")

def confirm_quit():
    """Ask user to confirm that they want to quit. default to yes
    Return True (yes,quit) or Flase (no, dont quit)"""
    spam = input(CONFIRM_QUIT_MESSAGE)
    if spam == "n":
        return False
    else:
        return True
    
    
    

#Testing section
#do_testing()
#display_times_tables()

#main section
if __name__ == "__main__" :
    while True:
        print(INSTRUCTIONS)
        input_prompt = "Press: 1 for training,"+\
                       "2 for testing, 3 to quit.\n"
        selection = input(input_prompt)
        selection = selection.strip()
        while selection not in ["1", "2", "3"]:
            selection = input("Please type either 1, 2, or 3: ")
            selection = selection.strip()

        if selection == "1":
            display_times_tables()
        elif selection == "2":
            do_testing()
        else:
            do_quit()
