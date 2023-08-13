#!/usr/bin/python3

import psutil

def print_color_text(text, color, check):
    if check == 0:
        print(f"\033[{color}m{text}\033[0m", end='')
    else:
        print(f"\033[{color}m{text}\033[0m")

def print_color_diff_ends(text, color, check):
    print("\033[30m║\033[0m", end='')
    print_color_text(text, color, check)
    print("\033[30m║\033[0m")

def print_logo():
    print_color_text("╔═════════════════════════════════════════════════╗", 30, 1)
    print_color_text("║                                                 ║", 30, 1) 
    print_color_diff_ends("              ██████╗     ███╗   ███╗            ", 31, 0)
    print_color_diff_ends("              ██╔══██╗    ████╗ ████║            ", 31, 0)
    print_color_diff_ends("              ██████╔╝    ██╔████╔██║            ", 31, 0)
    print_color_diff_ends("              ██╔═══╝     ██║╚██╔╝██║            ", 31, 0)
    print_color_diff_ends("              ██║         ██║ ╚═╝ ██║            ", 31, 0)
    print_color_diff_ends("              ╚═╝         ╚═╝     ╚═╝            ", 31, 0)
    print_color_text("║                                                 ║", 30, 1)  
    print_color_diff_ends("              Process     Monitoring             ", 31, 0)  
    print_color_text("║                                                 ║", 30, 1)
    print_color_diff_ends("         By: Ridwane el filali (B.R.O.L.Y)       ", 0, 0)
    print_color_diff_ends("   Github :https://github.com/RIDWANE-EL-FILALI  ", 0, 0)
    print_color_text("╚═════════════════════════════════════════════════╝", 30, 1)

if __name__ == "__main__":
    print("ok hello i am in the main")
print_logo()









