class TreasureQuest:
    """
    TreasureQuest class
    """
    def __init__(self):
        self.story_description = {
            "start": {
                "step_text": """
            -------------------------------------------------------------------
                In the heart of the bustling coastal town of Port Haven,
                a whispered legend has captured the imaginations of
                adventurers and dreamers alike. It speaks of a long-lost
                treasure, hidden away by a legendary pirate captain,
                Captain Blackbeard, centuries ago.

                The treasure is said to be unimaginable, with jewels that
                glitter like stars and riches beyond measure.

                You, Captain {username}, are a seasoned sailor and fearless
                leader known for your daring voyages across treacherous seas.

                The lure of the lost treasure beckons to you, as it does to so
                many others. Assemble your crew, for you have resolved to
                embark on 'The Quest for the Lost Treasure.'

                As you set sail aboard the 'Black Serpent', your trusty ship,
                you and your crew have arrived at a mysterious island where
                two paths stretch before you, each with its own challenges and
                mysteries.

            -----------------------------------------------------------------------
                Option 1: Do you navigate the Enchanted Forest, where magic
                          fills the air and mythical creatures roam?
                Option 2: Or do you brave the treacherous Mountains of Shadows,
                          where the secrets of the Scepter may be concealed
                          among the rugged peaks?
            ------------------------------------------------------------------------
                     """,
                "options": {
                    "option_1": "enchanted_forest",
                    "option_2": "mountains_of_shadows"
                }
            },

            "enchanted_forest": {
                "step_text": """
            ------------------------------------------------------------------------
                You choose to navigate the Enchanted Forest, a place where
                magic fills the air and mythical creatures roam. As you journey
                deeper into the forest, you encounter a wise old owl perched on
                a moss-covered branch in the woods who offers you guidance.

                The owl speaks to you: 'The path to the treasure lies through
                these woods, but it is treacherous and not for the faint of
                heart. You must choose your way wisely'.

                But the mystical trees with glowing leaves whispers secrets
                about the treasure, urging you to trust your own instincts.

            ------------------------------------------------------------------------
                Option 1: Do you accept the owl's guidance?
                Option 2: Or do you decide to follow your own instincts and
                          continue the journey through the uncharted depths
                          of the forest?
            ------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "owl's_guidance",
                    "option_2": "forest_depths"
                }
            },

            "mountains_of_shadows": {
                "step_text": """
            -------------------------------------------------------------------------
                You choose to brave the treacherous Mountains of Shadows,
                a place known for it's unforgiving terrain, where the secrets
                of the Scepter may be concealed among the rugged peaks.

                As you ascend higher into the formidable mountains, you come
                across a fork in the path. One path leads further into the
                mountains, while the other path descends towards the
                valley.

            -------------------------------------------------------------------------
                Option 1: Do you continue ascending higher into the mountains?
                Option 2: Do you choose to descend towards the valley?
            -------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "mountain_ascend",
                    "option_2": "valley_descend"
                }
            },

            "owl's_guidance": {
                "step_text": """
            ------------------------------------------------------------------------
                You accept the owl's guidance and follow it's directions deeper
                into the Enchanted Forest. The air becomes thick with
                enchantment as you venture through the ancient woods.

                The wise old owl leads you to a clearing, where an ancient tree
                with mystical inscriptions stands tall, it's bark adorned with
                glowing symbols. The owl hoots softly and the inscriptions
                come to life, revealing a hidden path to the Treasure Cove
                bathed in ethereal light.

            ------------------------------------------------------------------------
                Option 1: Do you follow the illuminated hidden path to the
                         Treasure Cove?
                Option 2: Or do you trust your instincts and explore your own
                         way through the forest?
            ------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "treasure_cove",
                    "option_2": "trust_instincts"
                }
            },

            "forest_depths": {
                "step_text": """
            -------------------------------------------------------------------------
                You decide to continue your journey without the owl's help,
                trusting your own instincts. As you venture deeper into the
                forest, the air becomes charged with an otherworldly energy,
                and the whispers of ancient spirits seem to echo through the
                enchanted glade.

                Suddenly, the mystical pond appears before you, it's shimmering
                waters reflecting the image of a hidden path. The allure is
                almost hypnotic. As you contemplate your choice, a mischievous
                fairy materializes beside the pond. She giggles and speaks,

                "Ah, another brave soul! If you accept the path, I shall grant
                you my magical amulet to aid your quest. But beware, for it
                comes with a price!"

            --------------------------------------------------------------------------
                Option 1: Do you follow the path reflected in the pond's
                          waters, and decline the fairy's offer?
                Option 2: Or do you choose to accept the fairy's offer and
                          take her magical amulet?
            --------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "mystic_pond",
                    "option_2": "mischief_fairy"
                }
            },

            "mountain_ascend": {
                "step_text": """
            -------------------------------------------------------------------------
                You decide to continue ascending higher into the mountains.
                The path is treacherous, and your crew faces many challenges,
                but you persevere. You eventually reach the summit, where you
                spot an ancient temple known as the Temple of Shadows. This
                temple is rumored to hold clues to the treasure's location.

            -------------------------------------------------------------------------
                Option 1: Do you enter the Temple of Shadows?
                Option 2: Do you explore the mountain summit without entering
                          the temple?
              ------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "temple_of_shadows",
                    "option_2": "mountain_summit"
                }
            },

            "valley_descend": {
                "step_text": """
            -------------------------------------------------------------------------
                 You choose to descend towards the valley. The path takes you
                 to a mysterious cave entrance hidden among the rocks. Inside
                 the cave, you discover a series of tunnels and chambers that
                 seem to lead deeper into the mountains.

            -------------------------------------------------------------------------
                Option 1: Do you venture further into the cave's depths?
                Option 2: Or do you decide to leave the cave and explore the
                          valley?
            -------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "cave_depths",
                    "option_2": "explore_valley"
                }
            },

            "treasure_cove": {
                "step_text": """
            -------------------------------------------------------------------------
                Following the hidden path revealed by the owl takes you
                through a labyrinth of ancient trees and sparkling ferns.
                The anticipation in the air grows heavier with every step,
                and you finally arrive in a magical glade bathed in the soft
                glow of moonlight.

                However, as you reach the center of the glade, where the
                entrance to the Treasure Cove should be, you find a sense
                of emptiness.

                Confusion clouds your mind as you explore the area.
                It becomes apparent that this Treasure Cove is nothing like
                the one described in legends.

                Disheartened, you realize that the owl's guidance has led
                you astray. This was not the treasure you sought, and the
                Treasure Cove was a disappointing dead end. With a heavy heart,
                you retreat, your quest left unfulfilled and your dreams
                shattered.

                """,
                "options": {},
                "outcome": "failure"
            },

            "trust_instincts": {
                "step_text": """
            -------------------------------------------------------------------------
                You choose to trust your instincts and explore your own way
                through the Enchanted Forest. As you venture deeper, the
                ancient trees seem to whisper encouragement, and the air
                becomes charged with mystical energy.

                Suddenly, you encounter a mystical creature, the Spirit
                Guardian, who appears before you in a burst of ethereal light.
                The Spirit Guardian offers you two enchanted artifacts, each
                with it's own magical properties.

            -------------------------------------------------------------------------
                Option 1: Do you accept the Crystal Amulet, said to reveal
                          hidden truths along the chosen path?
                Option 2: Or do you take the Cloak of Shadows, which allows
                          you to move stealthily and avoid potential dangers?
            -------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "crystal_amulet",
                    "option_2": "cloak_of_shadows"
                }
            },

            "mystic_pond": {
                "step_text": """
            --------------------------------------------------------------------------
                You decide to follow the path reflected in the pond's waters.
                The air becomes even more charged with mystical energy as you
                tread the illuminated path. The hidden route leads you to a
                breathtaking waterfall deep within the Enchanted Forest.

                Behind the waterfall, you discover a hidden grotto filled with
                radiant crystals and guarded by ancient spirits. In the heart
                of the grotto lies Captain Blackbeard's treasure, glittering
                with unimaginable wealth.

                Treasure shines with a wealth beyond imagination, a sight
                that would make even the most seasoned sailor's heart race.
                """,
                "options": {},
                "outcome": "success"
            },

            "mischief_fairy": {
                "step_text": """
            --------------------------------------------------------------------------
                You choose to accept the fairy's offer and take her magical
                amulet, trusting it to guide you through the forest. The
                amulet glows with an ethereal light as you continue your
                journey. As you venture deeper into the Enchanted Forest,the
                magical amulet pulsates in rhythm with the heartbeat of the
                forest.

                You arrive at a mysterious crossroad adorned with luminescent
                flowers. The amulet flickers, presenting you with two paths —
                one leading to the towering mountain summit, shrouded in mist,
                and the other to the Whispering Marsh, where the air is thick
                with enchantment.

            --------------------------------------------------------------------------
                Option 1: Do you take the route to the Whispering Marsh,
                          hoping for a different way to treasure?
                Option 2: Or do you follow the path to the mountain summit?
            --------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "whispering_marsh",
                    "option_2": "mountain_summit"
                }
            },

            "temple_of_shadows": {
                "step_text": """
            ---------------------------------------------------------------------------
                As you enter the dimly lit Temple of Shadows, the air thick
                with ancient mystique, you discover what appears to be a
                hidden Treasure Pillar at it's heart. With great anticipation,
                you unearth the structure, expecting Captain Blackbeard's
                legendary riches.

                To your dismay, the Treasure Pillar reveals nothing more than a
                weathered relic. The anticipated golden doubloons, exquisite
                jewels, and priceless artifacts are absent. Your crew,
                initially brimming with excitement, now shares in the loads of
                disappointment. Your quest for treasure has ended in unexpected
                failure.
                """,
                "options": {},
                "outcome": "failure"
            },

            "mountain_summit": {
                "step_text": """
            ---------------------------------------------------------------------------
                You decide to continue ascending higher into the mountains.
                The path is treacherous, and your crew faces many challenges,
                but you persevere. You eventually reach the summit, where the
                air is thin, and the view is breathtaking.

                As you explore the mountain summit, you come across an ancient
                stone altar bathed in the glow of the setting sun. The altar
                seems to emanate a mysterious energy, and nearby, you find an
                old journal that hints at the treasure's connection to
                celestial alignments.
            ---------------------------------------------------------------------------
                Option 1: Do you continue exploring the summit without
                          delving into the mysteries of the altar?
                Option 2: or do you take the journal and study its contents for
                          clues?
            ---------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "explore_summit",
                    "option_2": "journal_clues"
                }
            },

            "cave_depths": {
                "step_text": """
            ----------------------------------------------------------------------------
                 Entering the hidden cave leads you to the Treasure Chamber.
                 As you step into the Chamber, the sight before you is nothing
                 short of breathtaking. The room is illuminated by the radiant
                 glow of Captain Blackbeard's long-lost treasure, casting
                 reflections on the cave's ancient walls.

                 It sparkles with unimaginable wealth — golden doubloons,
                 exquisite jewels, and priceless artifacts, meticulously
                 arranged in the trove, a testament to the legendary Captain's
                 vast riches.

                 The air is heavy with the weight of history, and for a moment,
                 time seems to stand still as you and your crew gaze upon this
                 extraordinary fortune, now yours to claim.
                """,
                "options": {},
                "outcome": "success"
            },

            "explore_valley": {
                "step_text": """
            -----------------------------------------------------------------------------
                You choose to leave the cave, and step into the valley. In the
                distance, you spot a group of nomads, their tents set against
                the backdrop of towering peaks. They are nomads who have
                roamed these valleys for generations.

                As you approach, they welcome you with curiosity sparkling in
                their eyes. The nomads share tales of ancient wisdom and the
                interconnectedness of the natural world. They offer you choice
                to join them into their nomadic fold.

            ------------------------------------------------------------------------------
                Option 1: Will you join them and learn the ancient secrets of
                          these lands, taking a different path?
                Option 2: Or do you politely decline their offer and continue
                          your search for the treasure elsewhere, perhaps in
                          the Enchanted Forest, following your own instincts?
            -------------------------------------------------------------------------------
                """,
                "options": {
                    "option_1": "nomad_group",
                    "option_2": "trust_instincts"
                }
            },

            "crystal_amulet": {
                "step_text": """
            --------------------------------------------------------------------------------
                 You accept the Crystal Amulet, trusting in it's ability to
                 reveal hidden truths along your chosen path. However, as you
                 continue your journey, the amulet's revelations lead you into
                 the heart of a magical illusion. The forest plays tricks on
                 your perception, and you find yourself lost in a maze of
                 illusions.

                 The illusions have disoriented you. Despite your best efforts,
                 the treasure remains elusive. Acknowledging the deception and
                 the unsuccessful quest, you decide to return to your ship.

                 Becoming more reckless and underestimating the dangers of the
                 Enchanted Forest leads to further pitfalls. You find yourself
                 trapped in a magical illusions, unable to find your way out.
                 You and the rest of the crew are trapped forever unable to
                 return back to ship.
                """,
                "options": {},
                "outcome": "failure"
            },

            "cloak_of_shadows": {
                "step_text": """
            --------------------------------------------------------------------------------
                 You decide to take the Cloak of Shadows, allowing you to move
                 stealthily through the Enchanted Forest. The cloak proves to
                 be an invaluable asset and a wise decision, helping you
                 navigate through potential dangers with ease.

                 As you progress, the Cloak of Shadows unveils hidden paths
                 and protects you from magical traps. Your journey becomes a
                 dance of shadows and subtlety, and the heart of the Forest
                 reveals itself to you.

                 Your strategic choice of the Cloak of Shadows has proven to
                 be the key to your success. The mystical garment allowed you
                 to move through the Forest, avoiding mythical creatures and
                 treacherous terrain. Your cautious approach has paid off, and
                 you now stand at the entrance of Captain Blackbeard's long-
                 lost treasure trove. The Treasure is all yours.
                """,
                "options": {},
                "outcome": "success"
            },

            "whispering_marsh": {
                "step_text": """
            --------------------------------------------------------------------------------
                Choosing the path to the Whispering Marsh, you encounter
                mysterious lights and sounds. However, as you venture deeper,
                the path becomes increasingly challenging, and the amulet's
                light starts to fade. Eventually, you find yourself in a dense
                swamp surrounded by mist. The amulet's magic wanes, and you
                realize you are lost.

                The Whispering Marsh proves to be a treacherous maze with no
                sign of the treasure. Realizing the difficulty of the Marsh,
                you choose to retreat and return to Port Haven without the
                treasure. The magical amulet, though dimmed, guides you back
                through the Enchanted Forest.
                """,
                "options": {},
                "outcome": "failure"
            },

            "explore_summit": {
                "step_text": """
            --------------------------------------------------------------------------------
                Opting to continue exploring the summit without investigating
                the mysteries of the altar proves to be a missed opportunity.
                Unaware to you, the altar held vital clues to the treasure's
                location, and you now realize your oversight. Your journey
                through the mountains leads to a challenging path filled with
                unexpected dangers and obstacles, but no treasure in sight.

                Unfortunately, your quest remains incomplete. As you and your
                crew return to Port Haven with heavy hearts, the enigmatic
                altar's secrets continue to haunt you.
                """,
                "options": {},
                "outcome": "failure"
            },

            "journal_clues": {
                "step_text": """
            -------------------------------------------------------------------------------
                You choose to take the journal and study it's contents. As you
                delve into the ancient writings, you decipher clues that lead
                you to a hidden passage deep within the heart of the mountains.
                This passage, known as the Ethereal Gorge, is said to be a
                mystical gateway to a realm where Captain Blackbeard's
                treasure awaits.

                Your crew rejoices as you navigate the secret path, and upon
                arrival, you discover the ethereal realm filled with
                unimaginable wealth. The quest for Captain Blackbeard's
                long-lost treasure, which has driven many to the ends of the
                earth, has finally reached its dazzling conclusion in the
                heart of this mystical realm.
                """,
                "options": {},
                "outcome": "success"
            },

            "nomad_group": {
                "step_text": """
            ---------------------------------------------------------------------------------
                Embracing the nomads' offer, you choose the path of wisdom
                over riches. The nomads welcome you into their fold, revealing
                the hidden wonders of the mountains — their sacred sites, age-
                old rituals, and the tales carried by the mountain winds. As
                you immerse yourself in this ancient way of life, the quest
                for Captain Blackbeard's treasure fades away completely,
                leaving you on a different journey.

                The nomads become your mentors, and the mountains, your home.
                While the allure of untold wealth fades, the truth remains
                that the long-lost treasure of Captain Blackbeard has eluded
                you. Your quest has diverged, and the path you now follow
                leads away from the treasure. The goal remains unattained.
                This unexpected turn has lead you to unfulfilled quest.
                """,
                "options": {},
                "outcome": "failure"
            }
        }

    def display_intro(self):
        """
        Display the game's introduction.
        """
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
                username = input("\nEnter your name: ").strip().lower()

                # Checks if the username is empty or contains only spaces
                if not username.strip():
                    raise ValueError("Username cannot be empty or contain spaces.")

                # Checks if the username contains special characters
                if not username.isalnum():
                    raise ValueError("Username should only contain letters and numbers.")

                # Checks if the username is too short or too long
                if len(username) <= 3 or len(username) > 20:
                    raise ValueError("Username should be between 3 and 20 characters.")

                return username

            except ValueError as e:
                print(f"Invalid Input: {e}")
                print("Please try again.")

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
                print("Congratulations! You have succeeded in ypur quest.")
                break  # End the game
            elif outcome == "failure":
                print("Unfortunately, your quest has ended in failure.")
                break   # End the game
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
            play_choice = input("\nAre you ready to play the Game? (yes/no): ").strip().lower()

            if play_choice == "yes":
                user_name = self.get_username_input()
                print(f"\nWelcome, Captain {user_name}!")
                self.play_game()
                break
            elif play_choice == "no":
                print("\nAhoy, brave adventurer! Your treasure awaits, but it's your choice.")
                print("Enter 'yes' to play the game.")
                retry_choice = input("\nAre you ready to play the Game?(yes/no): ").strip().lower()
                if retry_choice != "yes":
                    print("You should enter 'yes' to play the game.\n")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'")

if __name__ == "__main__":


    # Create an instance of the TreasureQuest class
    game = TreasureQuest()
    # Call the start_game method to begin the game
    game.start_game()
