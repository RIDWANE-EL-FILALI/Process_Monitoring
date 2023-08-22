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
		process = psutil.Process(pid)
		mem_info = process.memory_info()

		# Calculate the total memory used by the process
		total_memory = mem_info.rss

		# Calculate the "Stack" and "Text" sizes (as before)
		stack_size = process.memory_info().data
		text_size = mem_info.text

		# Calculate the estimated "Heap" size
		heap_size = total_memory - (stack_size + text_size)
		
		process_name = process.name()
		cpu_percent = process.cpu_percent()
		num_threads = process.num_threads()
		return stack_size, heap_size, text_size, total_memory, process_name, cpu_percent, num_threads
	except psutil.NoSuchProcess:
		print("\033[31mProcess with PID not found\033[0m")
		return 0, 0, 0, 0

def Killprocess(pid):
	try:
		print("\033[31mKilling the process ... \033[0m")
		process = psutil.Process(pid)
		process.terminate()
		print(f"\033[31mProcess with PID : {pid} terminated 💀\033[0m")
		return True
	except psutil.NoSuchProcess:
		return False

def is_kernel_process(pid):
    try:
        process = psutil.Process(pid)
        return process.cpu_percent() is None
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def get_process_list():
    process_list = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        process_info = proc.info
        process_list.append((process_info['pid'], process_info['name']))
    return process_list


if __name__ == "__main__":
	print_logo()
	while True:
		try:
			pid = input("\033[1;4;32mEnter the pid of the process you wanna monitor (type 'exit' to quit) (type 'show to see the list of processes):\033[0m")
			if pid.lower() == "show":
				process_list = get_process_list()       
				headers = ['PID', 'Name']
				print(tabulate(process_list, headers, tablefmt="simple"))
				continue
			if pid.lower() == "exit":
				print("\033[31mExiting ... \033[0m")
				break
			if is_kernel_process(int(pid)):
				print("\033[31mKernel processes cannot be monitored because the memory layout for these process is different :\033[0m")
				continue
			stack, heap, text, data, process_name, cpu_percent, num_threads = get_info_process(int(pid))
			if stack == 0 and heap == 0 and text == 0 and data == 0:
    				continue
			data = [
				["\033[1;31mStack\033[0m", stack],
				["\033[1;31mHeap\033[0m", heap],
				["\033[1;31mText\033[0m", text],
    				["\033[1;31mData\033[0m", data],
    				["\033[1;31mProcess Name\033[0m", process_name],
    				["\033[1;31mCPU Percent\033[0m", cpu_percent],
    				["\033[1;31mNumber of Threads\033[0m", num_threads],
			]
			headers = ["\033[1;33mInfo\033[0m", "\033[1;33mValue\033[0m"]
			table = tabulate(data, headers, tablefmt="grid")

			print(table)
			kill = input("\033[1;33mType 'kill' to kill the process else it will skip :\033[0m")
			if (kill.lower() == "kill"):
				Killprocess(int(pid))
		except ValueError:
			print("\033[31mInvalid input. Please enter a valid integer PID or 'exit' to quit. \033[0m")
		except KeyboardInterrupt:
			print("")
			pass
		except EOFError:
			print("\033[31m\nExiting by Ctrl-D ... \033[0m")
			break
