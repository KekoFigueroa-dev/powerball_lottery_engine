# Import random for lottery number generation
import random
import math

# Print welcome and game description
print("---------------------Welcome to my Powerball Lottery Simulator!--------------------")
print("The powerball lottery is a game where you pick 5 'white' and 1 'red' ball")
print("The white balls are numbered 1-69 and the red ball is numbered 1-26")
print("The white balls are sorted numerically and the red ball is listed last")
print("for example, a winning number could be 12, 23, 34, 45, 56, 7 where 7 is the red ball")

in_running = True  # Main loop flag

while in_running:
    # Generate winning ticket (5 unique white balls + 1 red ball)
    WHITE_NUMBER = 69
    RED_NUMBER = 26

    winning_ticket = []
    while len(winning_ticket) < 5:
        white_ball = random.randint(1, WHITE_NUMBER)
        if white_ball not in winning_ticket:
            winning_ticket.append(white_ball)
    winning_ticket.sort()
    red_ball = random.randint(1, RED_NUMBER)
    winning_ticket.append(red_ball)

    # Calculate and display odds of winning
    total_tickets = WHITE_NUMBER * (WHITE_NUMBER - 1) * (WHITE_NUMBER - 2) * (WHITE_NUMBER - 3) * (WHITE_NUMBER - 4) * RED_NUMBER // 120
    print(f"For this powerball of {WHITE_NUMBER} white balls and {RED_NUMBER} red balls, your odds of winning are 1 in {total_tickets}, with a single ticket purchased")
    
    # Get user input for number of tickets to purchase
    ticket_amount = input("\nHow many tickets would you like to purchase? ")
    while not ticket_amount.isdigit():
        print("Sorry that is not an integer, Try again")
        ticket_amount = input("\nHow many tickets would you like to purchase? ")
    ticket_amount = int(ticket_amount)
    if ticket_amount > total_tickets:
        ticket_amount = total_tickets

    # Generate and display purchased tickets, ensuring no duplicates
    purchased_tickets = []
    tickets_bought = 0
    while tickets_bought < ticket_amount:
        current_ticket = []
        while len(current_ticket) < 5:
            white_ball = random.randint(1, WHITE_NUMBER)
            if white_ball not in current_ticket:
                current_ticket.append(white_ball)
        current_ticket.sort()
        red_ball = random.randint(1, RED_NUMBER)
        current_ticket.append(red_ball)
        if current_ticket not in purchased_tickets:
            purchased_tickets.append(current_ticket)
            print(f"Ticket purchased: {current_ticket}")
            tickets_bought += 1
        else:
            print("Ticket already purchased, ignoring duplicate")

    # Reveal winning numbers and check for a win
    print("\n----------Welcome to the POWERBALL DRAWING!----------")
    print(f"\nTonight's winning numbers are: {winning_ticket}")
    input("Press Enter to see if you have a winning ticket!")

    # Display result: win or loss
    if winning_ticket in purchased_tickets:
        print(f"Congratulations! You have a winning ticket!")
        print(f"Winning numbers: {winning_ticket}")
    else:
        print(f"You purchased {ticket_amount} tickets, but none were winners.")

    # Prompt user to run simulation again or exit
    choice = input("\nWould you like to run the simulation again? (y/n): ").lower()
    if choice != 'y':
        in_running = False

print("Thank you for playing my Powerball Lottery Simulator! Goodbye!")
