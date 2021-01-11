"""
	menu.py
"""

# IMPORTS #########################################################################################
import time

###################################################################################################


def print_title():
	""" prints the title """

	title = "|-" + "-"*14 + "-|\n"
	title += "|     CINCLÚ     |\n"
	title += "|-" + "-"*14 + "-|"

	print(title)



def main():
	""" main menu loop """

	opt = -1
	while opt != 0:

		# Print a title
		title = "|-" + "-"*14 + "-|\n"
		title += "|     CINECLÚ    |\n"
		title += "|-" + "-"*14 + "-|"
		print(title)

		print("(0) exit\n(1) create room\n(2) enter room")
		opt = -1
		while opt not in [0, 1, 2]:
			opt = int(input(">> "))

		if opt == 1:
			pass
		elif opt == 2:
			pass



main()