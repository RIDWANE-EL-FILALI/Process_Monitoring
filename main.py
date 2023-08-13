#!/usr/bin/python3

import psutil
import sys

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

def get_info_process(pid):
	try:
		process = psutil.Process(int(pid))
		mem_info = process.memory_info()

		stack_size = process.memory_info().data
		heap_size = mem_info.rss - stack_size
		text_size = mem_info.text
		data_size = mem_info.rss - text_size
		return stack_size, heap_size, text_size, data_size

	except psutil.NoSuchProcess:
		print("Process with PID no found")

if __name__ == "__main__":
	print_logo()
	pid = input("Enter the pid of the process you wanna monitor :")
	stack, heap, text, data = get_info_process(int(pid))
	print(f"Memory usage for PID {pid}:")
	print(f"Stack: {stack} bytes")
	print(f"Heap: {heap} bytes")
	print(f"Text: {text} bytes")
	print(f"Data: {data} bytes")


