#!/usr/bin/python3

import psutil
import sys
from tabulate import tabulate


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
	process = None
	try:
		process = psutil.Process(int(pid))
		mem_info = process.memory_info()

		stack_size = process.memory_info().data
		heap_size = mem_info.rss - stack_size
		text_size = mem_info.text
		data_size = mem_info.rss - text_size
		return stack_size, heap_size, text_size, data_size

	except psutil.NoSuchProcess:
		print("\033[31mProcess with PID not found\033[0m")
		return 0, 0, 0, 0


if __name__ == "__main__":
	print_logo()
	while True:
		try:
			pid = input("Enter the pid of the process you wanna monitor (type 'exit' to quit) :")
			if pid.lower() == "exit":
				print("\033[31mExiting ... \033[0m")
				break
			stack, heap, text, data = get_info_process(int(pid))
			if stack == 0 or heap == 0 or text == 0 or data == 0:
				continue
			labels = ['stack', 'heap', 'text', 'data']
			sizes = {stack, heap, text, data}
			data = [
				["\033[1;31mStack\033[0m", stack],
				["\033[1;31mHeap\033[0m", heap],
				["\033[1;31mText\033[0m", text],
				["\033[1;31mData\033[0m", data]
				]
			headers = ["\033[1;33mMemory Segment\033[0m", "\033[1;33mUsage (bytes)\033[0m"]
			table = tabulate(data, headers, tablefmt="grid")
			print(table)
		except ValueError:
			print("\033[31mInvalid input. Please enter a valid integer PID or 'exit' to quit. \033[0m")
		except KeyboardInterrupt:
			print("")
			pass
		except EOFError:
			print("\033[31m\nExiting by Ctrl-D ... \033[0m")
			break
