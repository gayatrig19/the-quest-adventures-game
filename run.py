from story import story_description


class TreasureQuest:
    """
    TreasureQuest class
    """

    def __init__(self):
        """
        Initialize the TreasureQuest game.
        It creates an instance of the TreasureQuest game, using the
        'story_description' dictionary to define the game's storyline and
        choices.
        """
        self.story_description = story_description

    def display_intro(self):
        """
        Display the game's introduction.
        """
        # Credit for ASCII art: https://fsymbols.com/generators/carty/
        print("""
               
                ████████╗██╗░░██╗███████╗   ░██████╗░██╗░░░██╗███████╗░██████╗████████╗
                ╚══██╔══╝██║░░██║██╔════╝   ██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝
                ░░░██║░░░███████║█████╗░░   ██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░
                ░░░██║░░░██╔══██║██╔══╝░░   ╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░
                ░░░██║░░░██║░░██║███████╗   ░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░
                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝   ░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░
        """)  # noqa
        print("""
           ----------------------------------------------------------------------------------
                    Welcome to "The Quest for the Lost Treasure" - an adventure
                     that will take you on a thrilling journey into the heart
                                   of mysteries and legends.
           ----------------------------------------------------------------------------------
        """)
        print("""
                Your goal is to find the legendary treasure hidden by Captain
                Blackbeard. At each step, you will be presented with options.

                            Choose your path wisely to succeed.

                Explore different paths, meet mystical creatures, and make
                            decisions to shape your destiny.

                Reach the end and discover the treasure to win! Or face a
                different fate based on your choices. Enjoy the journey and
                embrace the excitement of the unknown. Good luck!!
            """)

    def get_username_input(self):
        """
        Prompt the user for username.
        Validate username entered by user.
        """
        while True:
            try:
                username = input("Enter your name: ").strip().lower()

                # Checks if the username is empty or contains only spaces
                if not username.strip():
                    raise ValueError("\nUsername cannot be empty or contain only spaces.")  # noqa

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("\nUsername should only contain letters and numbers.")  # noqa

                # Checks if the username is too short or too long
                if len(username) <= 3 or len(username) > 20:
                    raise ValueError("\nUsername should be between 3 and 20 characters.")  # noqa

                return username

            except ValueError as e:
                print(f"Invalid Input: {e}")
                print("Please try again.")

    def restart_game(self):
        """
        Function to restart the game.
        Regardless of success or failure user is offered
        an option to restart the game.
        """
        while True:
            restart_choice = input("Would you like to play again?(yes/no): "
                                   ).strip().lower()
            if restart_choice == "yes":
                self.start_game()
                break
            elif restart_choice == "no":
                print("Thank you for playing.")
                break
            else:
                print("Invalid choice. Enter 'yes' to play again or 'no' to exit.")

    def play_game(self, current_step="start"):
        """
        Main function to play the game's story.
        """
        # Start the story from the beginning
        while current_step:
            step = self.story_description[current_step]
            step_text = step["step_text"]
            options = step["options"]
            outcome = step.get("outcome")

            # Display the current step's text
            print(step_text)

            # Display the options
            if outcome == "success":
                print("Congratulations! You have succeeded in your quest.\n")
                self.restart_game()
                break
            elif outcome == "failure":
                print("Unfortunately, your quest has ended in failure.\n")
                self.restart_game()
                break
            if options:
                choice = input("Enter your choice (1 or 2): ").strip().lower()
                while choice not in ["1", "2"]:
                    print("Invalid choice. Please enter 1 or 2.")
                    choice = input("Enter your choice (either 1 or 2): ").strip().lower()

                current_step = options[f"option_{choice}"]
            else:
                current_step = None

    def start_game(self):
        """
        Displays introduction and rules of the game.
        Asks user if user wants to start the game.
        Checks if user has entered valid input.
        """
        self.display_intro()
        while True:
            play_choice = input("\nAre you ready to play the Game? (yes/no): "
                                ).strip().lower()

            if play_choice == "yes":
                user_name = self.get_username_input()
                print(f"\nWelcome, Captain {user_name}!")
                self.play_game()
                break
            elif play_choice == "no":
                print("\nAhoy, brave adventurer! Your treasure awaits, but it's your choice.")
                print("It seems you have not type 'yes'. Enter 'yes' to play the game.\n")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'")


if __name__ == "__main__":
    """
    Creates an instance of the TreasureQuest class and
    initiates the game by calling the start_game method.
    """
    game = TreasureQuest()

    game.start_game()
