import random
def guess_the_number_game_danish():
    
    # Vælger tilfældigt et tal mellem 1 og 100
    number_to_guess = random.randint(1, 100)
    
    print("Velkommen til 'Gæt tallet' spillet!")
    print("Jeg har valgt et tal mellem 1 og 100.")
    
    forsøg = 0
    while True:
        # Spillerens gæt
        try:
            player_guess = int(input("Indtast dit gæt: "))
            
            # Input validering
            if player_guess < 1 or player_guess > 100:
                print("Indtast venligst et tal mellem 1 og 100.")
                continue

            forsøg += 1
            
            # Tjekker gættet
            if player_guess == number_to_guess:
                print(f"Tillykke! Du gættede tallet i {forsøg} forsøg.")
                break
            elif player_guess < number_to_guess:
                print("Tallet er højere.")
            else:
                print("Tallet er lavere.")
        except ValueError:
            print("Indtast venligst et gyldigt tal.")

# For at spille spillet kan du fjerne '#' ('#' betyder 'kommentar')fra den næste linje
guess_the_number_game_danish()
