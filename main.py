from color import *
from random import *

"""
OWNER: OLIVER
TIME_FINISHED: 12:04 PM

"""


class ChristMasTree:

    star_emoji = '✰'
    reset = ConsoleColors.RESET

    def __init__(self, *, add_star: bool = False):

        self.add_start = add_star


    def set_color(self, row: str,
                  border_only: bool = True,
                  rand_background: bool = False) -> str:

        """Sets the color in perimeters and inside"
            PARAMETERS:
                - Row: the row of *
                - Border_only: boolean
                    You can decide whether to set it only in the perimeter or in random positions
                - rand_background: boolean
                    It allows to add more colours, such as green, blue and cyan

                    if it's false, color besides (border_only (yellow)) will be Green
                    Otherwise picks a random color mentioned above
        """

        color = colors['yellow']

        background_color = [ConsoleColors.BLUE_BOLD,
                            ConsoleColors.GREEN_BOLD,
                            ConsoleColors.CYAN_BOLD]

        if border_only:
            if len(row) <= 1:

                return color + (row[0]
                                if not self.add_start else self.star_emoji)\
                       + self.reset
            else:
                if rand_background:
                    new_row = [choice(background_color[0:2]) + '*' + self.reset
                               for _ in range(len(row[1: len(row) - 1]))]

                    return (color + row[0] + self.reset)\
                           + ''.join(new_row)\
                           + (color + row[-1] + self.reset)
                else:
                    return (color + row[0] + self.reset) + \
                           (colors['green'] + row[1: len(row) - 1] + self.reset)\
                           + (color + row[-1] + self.reset)

        else:
            new_row = []

            for index, item in enumerate(row):
                if index % randint(3, 5) == 0:
                    new_row.append(color + (
                        self.star_emoji
                        if self.add_start and len(row) == 1 else item)
                                   + self.reset)

                else:
                    new_row.append(
                        (colors['green'] if not rand_background else choice(background_color))
                        + item + self.reset
                    )




            return ''.join(new_row)




    def display(self, christmas_message: str,
                destination: str, *,
                message_color: str = None,
                light_perimeter: bool = True,
                rand_color: bool = False) -> None:

        """displays the Tree

           PARAMETERS:
               - christmas_message -> You may choose your own message
               - destination -> You choose someone's name

               - result: christmas_message + destination
        """


        if message_color is None:
            message_color = colors['red']
        else:
            if message_color not in colors:
                raise InvalidColor
            else:
                message_color = message_color

        print(f"{message_color}"
              f"{christmas_message} {destination}"
              f"{self.reset}\n")

        tree = [" " * int(10 - i) + self.set_color("*" * int(i * 2 + 1),
                                                   border_only=light_perimeter, rand_background=rand_color) for i in range(10)]
        trunk = [f'{" " * 9}|||' for _ in range(3)]

        print('\n'.join(tree) + '\n' + '\n'.join(trunk) + '\n' + f'{" " * 5}-----------')

