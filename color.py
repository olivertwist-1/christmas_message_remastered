class ConsoleColors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    PINK_BOLD = PINK + BOLD
    BLUE_BOLD = BLUE + BOLD
    CYAN_BOLD = CYAN + BOLD
    GREEN_BOLD = GREEN + BOLD
    YELLOW_BOLD = YELLOW + BOLD
    RED_BOLD = RED + BOLD

    PINK_UNDERLINE = PINK + UNDERLINE
    BLUE_UNDERLINE = BLUE + UNDERLINE
    CYAN_UNDERLINE = CYAN + UNDERLINE
    GREEN_UNDERLINE = GREEN + UNDERLINE
    YELLOW_UNDERLINE = YELLOW + UNDERLINE
    RED_UNDERLINE = RED + UNDERLINE


colors = {'pink': ConsoleColors.PINK_BOLD,
              'BLUE': ConsoleColors.BLUE_BOLD,
              'cyan': ConsoleColors.BLUE_BOLD,
              'green': ConsoleColors.GREEN_BOLD,
              'yellow': ConsoleColors.YELLOW_BOLD,
              'red': ConsoleColors.RED_BOLD}


class InvalidColor(Exception):
    def __str__(self):
        return f"Valid Colors: {', '.join(colors.keys())}"
