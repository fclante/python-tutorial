import random

def get_user_choice():
    """Bed brugeren om deres valg og returner det.""" # Prompt the user for their choice and return it.
    print("Indtast dit valg: sten, papir eller saks")
    while True:
        choice = input().lower()
        if choice in ['sten', 'papir', 'saks']:
            return choice
        print("Ugyldigt valg. Vælg venligst sten, papir eller saks.")

def get_computer_choice():
    """Returner et tilfældigt valg lavet af computeren.""" # Return a random choice made by the computer.
    return random.choice(['sten', 'papir', 'saks'])

def determine_winner(user, computer):
    """Bestem og udskriv vinderen baseret på brugerens og computerens valg.""" # Determine and print the winner based on user and computer choices.
    if user == computer:
        return "Det er uafgjort!" # It's a tie!
    if (user == 'sten' and computer == 'saks') or \
       (user == 'saks' and computer == 'papir') or \
       (user == 'papir' and computer == 'sten'):
        return f"Du vinder! {user} slår {computer}." # You win! {user} beats {computer}.
    else:
        return f"Du taber! {computer} slår {user}." # You lose! {computer} beats {user}.

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computeren valgte: {computer_choice}") # Computer chose: {computer_choice}
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Indgangspunkt for applikationen 
if __name__ == "__main__": # Hvis main findes
    main() # Så kør main