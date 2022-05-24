pref = "\033["
reset = f"{pref}0m"

class colors:
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"

# Alternative to print, uses white color by default but accepts any color 
# from the Colors class. Name it as you like.
def puts(text, color=colors.white, is_bold=False):
    print(f'{pref}{1 if is_bold else 0};{color}' + text + reset, end="")
