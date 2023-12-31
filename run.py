import sys
import time

from story import story_description


class TreasureQuest:
    """
    TreasureQuest class for a text-based adventure game.
    """

    def __init__(self):
        """
        Initialize the TreasureQuest game.
        It creates an instance of the TreasureQuest game, using the
        'story_description' dictionary to define the game's storyline and
        choices.
        """
        self.story_description = story_description

    def type_text(self, text, delay=0.03):
        """
        Print text with a typing effect.
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def display_intro(self):
        """
        Display the game's introduction.
        """
        # Credit for ASCII art: https://fsymbols.com/generators/carty/
        print("""

    ████████╗██╗░░██╗███████╗   ░██████╗░██╗░░░██╗███████╗░██████╗████████╗
    ╚══██╔══╝██║░░██║██╔════╝   ██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝
    ░░░██║░░░███████║█████╗░░   ██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░
    ░░░██║░░░██╔══██║██╔══╝░░   ╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░
    ░░░██║░░░██║░░██║███████╗   ░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░
    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝   ░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░
        """)
        self.type_text("""
**----------------------------------------------------------------------------**
         Welcome to "The Quest for the Lost Treasure" - an adventure
         that will take you on a thrilling journey into the heart
                     of mysteries and legends.
**----------------------------------------------------------------------------**
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
                username = input("\nEnter your name: ").strip().lower()

                # Checks if the username is empty or contains only spaces
                if not username.strip():
                    raise ValueError("Username cannot be empty or contain only spaces.")  # noqa

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("Username should only contain letters and numbers.")  # noqa

                # Checks if the username is too short or too long
                if len(username) < 3 or len(username) > 20:
                    raise ValueError("Username should be between 3 and 20 characters.")  # noqa

                return username

            except ValueError as e:
                print(f"Invalid Input: {e}")
                print("Please try again.\n")

    def restart_game(self):
        """
        Function to restart the game.
        Regardless of success or failure user is offered
        an option to restart the game.
        """
        while True:
            restart_choice = input("\nWould you like to play again?(yes/no): "
                                   ).strip().lower()
            if restart_choice == "yes":
                self.start_game()
                break
            elif restart_choice == "no":
                self.type_text("""
    **------------------------------------------------------------**
                       Thank you for playing!!
    **------------------------------------------------------------**
                   """)
                break
            else:
                print("\nInvalid choice. Enter 'yes' to play again or 'no' to exit.")  # noqa

    def play_game(self, current_step="start"):
        """
        Main function to play the game's story.
        """
        while current_step:
            step = self.story_description[current_step]
            step_text = step["step_text"]
            options = step["options"]
            outcome = step.get("outcome")

            # Display the current step's text
            print(step_text)

            # Display the options
            if outcome == "success":
                self.type_text("""
**----------------------------------------------------------------------------**
        Congratulations on your triumphant adventure! You are successful in
        your quest. As you sail back to Port Haven with your treasure-laden
        ship, the tales of your courage and determination will inspire
        generations to come. Thank you for joining us on this epic voyage,
        and may your future adventures be as legendary as this one.
**----------------------------------------------------------------------------**
                    \n""")
                self.restart_game()
                break
            elif outcome == "failure":
                self.type_text("""
**----------------------------------------------------------------------------**
    Despite your best efforts, your quest for the lost treasure has failed.
**----------------------------------------------------------------------------**
                    \n""")
                self.restart_game()
                break
            if options:
                choice = input("Enter your choice (either 1 or 2): "
                               ).strip().lower()
                while choice not in ["1", "2"]:
                    print("\nInvalid choice. Please enter 1 or 2.")
                    choice = input("\nEnter your choice (either 1 or 2): "
                                   ).strip().lower()

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
                self.type_text(f"""
                       Welcome aboard, Captain {user_name}!""")
                print("""
         Our story starts in the heart of the bustling coastal town of
         Port Haven. A whispered legend has captured the imaginations of
         adventurers and dreamers alike. It speaks of a long-lost treasure,
         hidden away centuries ago.

         The treasure is said to be unimaginable, with jewels that glitter
         like stars and riches beyond measure.
                      """)
                self.type_text(f"""
         You, Captain {user_name}, are a seasoned sailor and fearless leader
         known for your daring voyages across treacherous seas.
                """)
                self.play_game()
                break
            elif play_choice == "no":
                print("\nAhoy, brave adventurer! Your treasure awaits.")
                print("It seems you have not type 'yes'. Enter 'yes' to play the game.\n")  # noqa
            else:
                print("Invalid choice. Enter 'yes' or 'no'")


if __name__ == "__main__":
    """
    Creates an instance of the TreasureQuest class and
    initiates the game by calling the start_game method.
    """
    game = TreasureQuest()

    game.start_game()
