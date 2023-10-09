class TreasureQuest:
    """
    TreasureQuest class
    """
    def __init__(self):
        self.story = {
            "start": {
                "step_text": "You are in a forest. Do you want to go left or right",
                options: {
                    "left": "left_path",
                    "right": "right_path"
                }
            },

            "left_path": {
                "step_text": "You encounter a bear! Do you run or climb a tree?",
                options: {
                    "run": "end_run",
                    "climb": "end_climb"
                }
            },
            "right_path": {
                "step_text": "You got away safely! The end.",
                options: {}
            },
            "end_climb": {
                "step_text": "You are safe in the tree. The end.",
            }
        }
        

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
        Prompt the user for username.
        Validate username entered by user.
        """
        while True:
            try:
                username = input("Enter your name:")

                # Checks if the username is empty or contains only spaces
                if not username.strip():
                    raise ValueError("Username cannot be empty or contain only spaces.")

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("Username should only contain letters and numbers.")

                # Checks if the username is too short or too long
                if len(username) <= 3 or len(username) > 20:
                    raise ValueError("Username should be between 3 and 20 characters.")
                
                return username

            except ValueError as e:
                print(f"Invalid Input:{e}")
                print("Please try again.")


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








       