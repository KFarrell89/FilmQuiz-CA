class Player:
    score = 0
    current_question = 0
    quit = False #used for identifying if a player still wants to play

    def __init__(self, name = "Player One", home_location = ""):
        self.name = name
        self.home_location = home_location
    

    def next_question(self):

        concluded = False #used for checking entry into loops

        print("\nType your answers. Enter 'C' for a clue, enter 'S' for your current score, or enter 'Q' to quit the game.\n")
        if self.current_question < 10:
            self.current_question += 1

        if self.current_question == 1:

            print("Here is your first question:\n ")

        elif self.current_question == 10:

            print("Here is your final question:\n ")

        else:
            print("Here is your next question:\n ")
        
        #used to create questions out of a questions dictionary
        question = Question(list(questions.keys())[0],questions[self.current_question][0],questions[self.current_question][1],questions[self.current_question][2], questions[self.current_question][3], questions[self.current_question][4], questions[self.current_question][5])

        while concluded == False and self.quit == False: #while the player has not entered a right or wrong answer or tried to quit.
            print(question.text)
            print()
            answer = input("Answer: ")

            if answer.upper() == question.answer:#compares the answer given to the appropriate answer attribute of the question
                concluded = True
                player.score += question.points # add points to the players score
                print("\nThat is correct!\n")
        
            elif answer.upper() == "C":

                question.clue_count += 1 #keeps track of how many clues are used
                
                if question.clue_count == 1:
                    question.points -=2
                    print()
                    print(question.clue_1)
                    print()

                if question.clue_count == 2:
                    question.points -=2
                    print()
                    print(question.clue_2)
                    print()

                if question.clue_count == 3:
                    question.points -=2
                    print()
                    print(question.clue_3)
                    print()

                if question.clue_count == 4:
                    question.points -=2
                    print()
                    print(question.clue_4)
                    print()

                if question.clue_count > 4:
                    print("\nNo more clues available.\n")
    
            elif answer.upper() == "S":
                print("\nYour current score is: " + str(player.score) + "\n")

            elif answer.upper() == "Q":
                print("\nGoodbye!\n")
                self.quit = True
            
            else:
                concluded = True
                print("\nThat is incorrect.\n")


    def score_check(self):

        return "{name} from {location}, you have {score} points so far!".format(name = self.name, location = self.home_location, score = self.score)
        
    # questions are numbered by the dictionary key and follow this pattern:
    # question number { question text - answer - clue - clue - clue - clue }

questions = {1: ["Complete the film title starring John Candy: ‘Uncle…’?","BUCK","Rhymes with truck", "Another name for a male deer.", "Begins with the second letter of the alphabet.", "Another name for a dollar."],
             2: ["Jim Carrey portrayed which Batman villain?","RIDDLER","His calling card is a question mark (?).", "He wears all green and has a cane.", "Shares his name with a common word puzzle.", "'Riddle me this...'"],
             3: ["Where were The Lord of the Rings movies filmed?","NEW ZEALAND","Country in Oceania.", "Has a higher population of sheep than it does people.", "The national symbol is a Kiwi bird.", "Famous for the All Blacks Rugby team."],
             4: ["What movie about a great white shark was considered the first-ever summer blockbuster?","JAWS","Directed by Steven Spielberg.", "Directed in 1975.", "'We're gonna need a bigger boat'.", "Part of the your body which is used when eating."],
             5: ["Which movie from 1995 asks 'What's in the box?'","SEVEN","Features the deadly sins throughout.", "Stars Kevin spacey as the bad guy.", "Stars Brad Pitt and Morgan Freeman.", "A one word title that is a spelled out number."],
             6: ["Which film originally featured Ben Stiller as a fashion model?","ZOOLANDER","Also starring Owen Wilson and Will Ferrell", "Ben Stiller could not turn left.", "Ben Stiller's character 'Derek' has this movie title surname.", "Animals are kept in part of the title."],
             7: ["Which Marvel film stars Chris Hemsworth as the titular character?","THOR","He comes from Asgard.", "He has a hammer named 'Mjölnir'.", "He is one of the Avengers.", "He is the God of Thunder"],
             8: ["In which film do a medical engineer and an astronaut work together to survive after an accident leaves them adrift?","GRAVITY","Stars Sandra Bullock", "Stars George Clooney, that's the full cast (other than some voice acting)", "Discovered by Isaac Newton.", "Keeps us from floating into space."],
             9: ["Which animated toy cowboy has adventures with other toys?","WOODY","His life is turned upside down by a space ranger.", "Voiced by Tom Hanks.", "Owned by Andy", "'There's a snake in my boot'."],
             10: ["Who is the titular anti-hero that is a 'Merc with a mouth'?","DEADPOOL","Has a red and black suit.", "Essentially become immortal.", "Danced to an N-Sync song.", "Played by Ryan Reynolds"]}


class Question:
    points = 10
    clue_count = 0

    def __init__(self, question_number, text, answer, clue_1, clue_2, clue_3, clue_4):

        self.question_number = question_number
        self.text = text
        self.answer = answer
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3
        self.clue_4 = clue_4

#contains a welcome and borders for formatting
welcome_message = """-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\nWelcome to FilmQuiz :-: The game where you answer 10 questions, each of which has 4 clues, for the chance to win the ultimate prize...Bragging rights!\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"""
    
game_rules = """\nThe rules of FilmQuiz are as follows:\n\nEach question is worth 10 points.\n\nEach clue you use reduces the points avalable for a question by 2.\n\nQuestions cannot be skipped and only one answer will be accepted, so use your clues and answer wisely."""
                       
start_message = welcome_message + "\n \n" + game_rules  + "\n\nNow that we know the game, let's get to know the player.\n"

print(start_message)
player_name = input("What's your name?\n\n") #grabs player name from player input
player_location = input("\n\nAnd where do you come from?\n\n")#grabs player location from player input

player = Player(player_name, player_location)

print("\n\nWelcome {name} from {location} and best of luck to you. Let the game begin\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-".format(name = player_name, location = player_location))


while player.current_question < 10 and player.quit == False:
    player.next_question()

final_message = "You have reached the end of the game. Your final score was {score} out of 100. Thanks for playing FilmQuiz.\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-".format(score = player.score)

print(final_message)