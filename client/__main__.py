"""
	__main__.py

"""

# IMPORTS #########################################################################################
import subprocess

###################################################################################################


# We run in shell the telnet interface and the VCL GUI

PASSWORD = "contraseña"
HOST = "127.0.0.1"
PORT = "8000"

subprocess.Popen(["vlc", "--extraintf", "telnet", "--telnet-password", PASSWORD, "--telnet-host", HOST, "--telnet-port", PORT], 
	shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

