#Import necessary modules
import random
import math
#Powerball engine

#Print welcome message and short game description
print("---------------------Welcome to my Powerball Lottery Simulator!--------------------")
print("The powerball lottery is a game where you pick 5 'white' and 1 'red' ball")
print("The white balls are numbered 1-69 and the red ball is numbered 1-26")
print("The white balls are sorted numerically and the red ball is listed last")
print("for example, a winning number could be 12, 23, 34, 45, 56, 7 where 7 is the red ball")

#iNITIALIZE VARIABLES AND FLAG
WHITE_NUMBER = 69
RED_NUMBER = 26
in_running = True

while in_running:
    #generate winning ticket
    winning_ticket = []
    while len(winning_ticket) < 5:
        white_ball = random.randint(1, WHITE_NUMBER)
        if white_ball not in winning_ticket:
            winning_ticket.append(white_ball)
    winning_ticket.sort()
    red_ball = random.randint(1, RED_NUMBER)
    winning_ticket.append(red_ball)
    #debug
    #print(winning_ticket)
    #input("Press Enter to continue")

    #Generate total number of tickets and get the odds of winning

    total_tickets = WHITE_NUMBER * (WHITE_NUMBER - 1) * (WHITE_NUMBER - 2) * (WHITE_NUMBER - 3) * (WHITE_NUMBER - 4) * RED_NUMBER // 120
    print(f"For this powerball of {WHITE_NUMBER} white balls and {RED_NUMBER} red balls, your odds of winning are 1 in {total_tickets}, with a single ticket purchased")
    break
