class TreasureQuest:
    """
    TreasureQuest class
    """
    def __init__(self):
        # Constructor logic here
        pass  # Placeholder for constructor logic

    def display_intro(self):
        """
        Display the game's introduction.
        """
        print ("""
               --------------------------------------------------------------------------
                  Welcome to "The Quest for the Lost Treasure" - an adventure that will
                  take you on a thrilling journey into the heart of mystery and legend.
               --------------------------------------------------------------------------
        """)
        print("""
                 Your goal is to find the legendary treasure hidden by Captain Blackbeard.
                 Choose your path wisely to succeed. At each step, you will be presented 
                 with options - Option 1 and Option 2. Enter the number of your choice.
                 
                 Explore different paths, meet mystical creatures, and make decisions to shape 
                 your destiny.
                 
                 Your adventure will lead to various outcomes, including success and disappointment.
                 
                 Reach the end and discover the treasure to win! Or face a different fate based on 
                 your choices. Enjoy the journey and embrace the excitement of the unknown. 
                                  
                                  Good luck, Captain!
        """)

    def get_username_input(self):
        """
        Get username input from user.
        Validate username entered by user.
        """
    
    def start_game(self):
        """
        Displays introduction and rules of the game.
        Asks user if user wants to start the game.
        Checks if user has entered valid input.
        """
        self.display_intro()
        while True:
            play_choice = input("Are you ready to play the Game? (yes/no):").lower()

            if play_choice == "yes":
                user_name = self.get_username_input()
                print(f"Welcome, {user_name} !")
                break
            elif play_choice == "no":
                print("Ahoy, brave adventurer! Your treasure awaits, but it's your choice.")
                print("Feel free to return whenever you're ready to embark on this epic quest!")
                retry_choice = input("Are you ready to play the Game? (yes/no):").lower()
                if retry_choice != "yes":
                    print("You should enter 'yes' to play the game.")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'")





# Create an instance of the TreasureQuest class
game = TreasureQuest()

# Call the start_game method to begin the game
game.start_game()

# Call the display_intro method
# game.display_intro()








       