class TreasureQuest:
    """
    TreasureQuest class
    """
    def __init__(self):
        self.story_description = {
            "start": {
                "step_text": """
                    
                In the heart of the bustling coastal town of Port Haven, 
                a whispered legend has captured the imaginations of adventurers 
                and dreamers alike. It speaks of a long-lost
                treasure, hidden away by a legendary pirate captain, 
                Captain Blackbeard, centuries ago.The treasure is said 
                to be unimaginable, with jewels that glitter like stars and 
                riches beyond measure.
                You are Captain Alex Sterling, a seasoned sailor and fearless 
                leader known for your daring voyages across treacherous seas. 
                The lure of the lost treasure beckons to you, as it does to so 
                many others. Assemble your crew, for you have resolved to 
                embark on 'The Quest for the Lost Treasure.'
                As you set sail aboard the 'Black Serpent', your trusty ship, 
                two paths stretch before you, each with its own challenges and 
                mysteries. 
                -----------------------------------------------------------------          
                Option 1: Do you navigate the Enchanted Forest, where magic 
                          fills the air and mythical creatures roam?                                          
                Option 2: Or do you brave the treacherous Mountains of Shadows, 
                          where the secrets of the Scepter may be concealed 
                          among the rugged peaks?        
                -----------------------------------------------------------------
                         """,
                options: {
                    "Option 1": "enchanted_forest",
                    "Option 2": "mountains_of_shadow"
                }
            },

            "enchanted_forest": {
                "step_text": """
                You choose to navigate the Enchanted Forest, a place where 
                magic fills the air and mythical creatures roam. As you journey 
                deeper into the forest, you encounter a wise old owl perched on 
                a moss-covered branch in the woods who offers you guidance. 
                The owl speaks to you: 'The path to the treasure lies through 
                these woods, but it is treacherous and not for the faint of 
                heart. You must choose your way wisely'. 
                But the mystical trees with glowing leaves whispers secrets 
                about the treasure, urging you to trust your own instincts.
                --------------------------------------------------------------
                Option 1: Do you accept the owl's guidance?                               
                Option 2: Or do you decide to follow your own instincts and 
                          continue the journey through the uncharted depths 
                          of the Enchanted Forest?
                --------------------------------------------------------------
                """,
                options: {
                    "Option 1": "owl's_guidance",
                    "option 2": "forest_depths"
                }
            },
            "mountains_of_shadow": {
                "step_text": """
                You choose to brave the treacherous Mountains of Shadows,  
                a place known for it's unforgiving terrain, where the secrets 
                of the Scepter may be concealed among the rugged peaks. 
                As you ascend higher into the formidable mountains, you come 
                across a fork in the path. One path leads further into the 
                mountains, while the other path descends towards the 
                valley.                 
               ----------------------------------------------------------------
               Option 1: Do you continue ascending higher into the mountains?                 
               Option 2: Do you choose to descend towards the valley?         
               ---------------------------------------------------------------- 
                """,
                options: {
                    "Option 1": "mountain_ascend",
                    "option 2": "valley_descend"
                }
            },
            "owl's_guidance": {
                "step_text": """
                You accept the owl's guidance and follow its directions deeper 
                into the Enchanted Forest. The air becomes thick with 
                enchantment as you venture through the ancient woods. The wise 
                old owl leads you to a clearing, where an ancient tree with 
                mystical inscriptions stands tall, it's bark adorned with 
                glowing symbols. The owl hoots softly and the inscriptions 
                come to life, revealing a hidden path to the Treasure Cove 
                bathed in ethereal light.                            
               ----------------------------------------------------------------
               Option 1: Do you follow the illuminated hidden path to the 
                         Treasure Cove?             
               Option 2: Or do you trust your instincts and explore your own 
                         way through the forest?  
               -----------------------------------------------------------------
                """,
                options: {
                    "Option 1": "treasure_cove",
                    "option 2": "trust_instincts"
                }
            },
        }
        
    def display_intro(self):
        """
        Display the game's introduction.
        """
        print("""
            --------------------------------------------------------------------------
             Welcome to "The Quest for the Lost Treasure" - an adventure that will
             take you on a thrilling journey into the heart of mysteries and legends.
            --------------------------------------------------------------------------
        """)
        print("""
                 Your goal is to find the legendary treasure hidden by Captain Blackbeard.
                 At each step, you will be presented with options - Option 1 and Option 2.
                 Choose your path wisely to succeed. 
                 Explore different paths, meet mystical creatures, and make decisions to shape 
                 your destiny.
                 Reach the end and discover the treasure to win! Or face a different fate based on 
                 your choices. Enjoy the journey and embrace the excitement of the unknown. \n
                                  Good luck, Captain!
        """)

    def get_username_input(self):
        """
        Prompt the user for username.
        Validate username entered by user.
        """
        while True:
            try:
                username = input("Enter your name:\n")

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
   