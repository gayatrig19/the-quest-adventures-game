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

# Create an instance of the TreasureQuest class
game = TreasureQuest()

# Call the display_intro method
game.display_intro()








       