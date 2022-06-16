# Hangman art by @ChristianAuman
# https://replit.com/@ChristianAuman/Hangman

from simple_chalk import *

stages = ["""###################
# ################# [        ]
# #   / /
# #  / /
# # / /
# #/ /
# # /
# #/
# #
# #
# #
# #
# #
# #
# #
# #
# #  _
# #  \\\\
# #   \\\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [#       ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||
# # /         ||--.
# #/          (    )
# #            ˙--˙
# #
# #
# #
# #
# #
# #
# #
# #  _
# #  \\\\
# #   \\\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [##      ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||.-''.
# # /         |/  _  \\
# #/          ||  ☉/☉|
# #           (\◝_ .'
# #            `--'
# #
# #
# #
# #
# #
# #
# #  _
# #  \\\\
# #   \\\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [###     ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||.-''.
# # /         |/  _  \\
# #/          ||  ☉/☉|
# #           (\◝_ .'
# #          .-`--'.
# #         /Y . . Y
# #        // |   |
# #       //  | . |
# #      ')   |   |
# #
# #
# #  _
# #  \\\\
# #   \\\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [####   ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||.-''.
# # /         |/  _  \\
# #/          ||  ☉/☉|
# #           (\◝_ .'
# #          .-`--'.
# #         /Y . . Y\\
# #        // |   | \\\\
# #       //  | . |  \\\\
# #      ')   |   |   (`
# #
# #
# #  _
# #  \\\\
# #   \\\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [######  ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||.-''.
# # /         |/  _  \\
# #/          ||  ☉/☉|
# #           (\◝_ .'
# #          .-`--'.
# #         /Y . . Y\\
# #        // |   | \\\\
# #       //  | . |  \\\\
# #      ')   |   |   (`
# #           ||-
# #           ||
# #  _        ||
# #  \\\\       ||
# #   \\\\      /|
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [####### ]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||.-''.
# # /         |/  _  \\
# #/          ||  ☉/☉|
# #           (\◝_ .'
# #          .-`--'.
# #         /Y . . Y\\
# #        // |   | \\\\
# #       //  | . |  \\\\
# #      ')   |   |   (`
# #           ||-||
# #           || ||
# #  _        || ||
# #  \\\\       || ||
# #   \\\\      /| |\\
##############################
##############################
# #                        # #
: :                        : :
. .                        . .""",

          """###################
# ################# [########]
# #   / /     ||
# #  / /      ||
# # / /       ||
# #/ /        ||
# # /         ||.-''.
# #/          |/  _  \\
# #           ||  x/x|            """+red("""   ██▓     ▒█████    ██████ ▓█████   """)+"""
# #           (\◝_ .'             """+red("""  ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀   """)+"""
# #          .-`--'.              """+red("""  ▒██░    ▒██░  ██▒░ ▓██▄   ▒███     """)+"""
# #         /Y . . Y\\            """+red("""  ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄   """)+"""
# #        // |   | \\\\          """+red("""  ░██████▒░ ████▓▒░▒██████▒▒░▒████▒  """)+"""
# #       //  | . |  \\\\         """+red("""  ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░  """)+"""
# #      ')   |   |   (`          """+red("""  ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░  """)+"""
# #           ||-||               """+red("""    ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░     """)+"""
# #    _      || ||               """+red("""      ░  ░    ░ ░        ░     ░  ░  """)+"""
# #   //      || ||                 
# #  //       || ||
############  /| |\   ########
############\         ########
# #         \\\\             # #
: :          \\\\            : :
. .           `'           . ."""]

win = """ooooo  oooo ooooooo  ooooo  oooo                        
  888  88 o888   888o 888    88                         
    888   888     888 888    88                         
    888   888o   o888 888    88                         
   o888o    88ooo88    888oo88                          
                                                        
                    oooo     oooo ooooo oooo   oooo oo  
                     88   88  88   888   8888o  88 8888 
                      88 888 88    888   88 888o88 8888 
                       888 888     888   88   8888  88  
                        8   8     o888o o88o    88  oo  """


def get_stage(stage: int, game):

    if stage < 0 or stage > 7:
        raise Exception("Stage must be between 0 and 7")
        return False

    stageart = stages[:][stage].split("\n")

    stageart[1] += ((34 - len(stageart[1])) * " ") + bold("Guess the word:")
    stageart[2] += ((34 - len(stageart[2])) * " ") + blue("".join([f"{i} " for i in game.guess]))

    stageart[4] += ((34 - len(stageart[4])) * " ") + gray("Word length: ") + str(len(game.guess))
    stageart[5] += ((34 - len(stageart[5])) * " ") + gray("Wrong guesses: ") + str(game.wrong_guesses) + gray("/") + str(game.guesses)
    stageart[6] += ((34 - len(stageart[6])) * " ") + "".join([f"{i} " for i in game.guessed_letters])

    return "\n".join(stageart)


def get_win():
    return green(win)
