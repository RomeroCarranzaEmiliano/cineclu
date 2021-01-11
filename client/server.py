"""
	server.py

	An object to handle the connection to the websocket server
"""

# IMPORTS #########################################################################################
import socketio

###################################################################################################


class Server():
	def __init__(self, HOST="0.0.0.0", PORT="8080", TOKEN="a_default_token"):
		""" Initialization of the server instance """
		self.HOST = HOST
		self.PORT = PORT
		self.TOKEN = TOKEN
		self.sio = None


	def connect(self):
		""" Connects to the server """

		# Create the client object
		self.sio = socketio.Client()

		# Connect to server
		listening_at = f"{self.HOST}:{self.PORT}"
		self.sio.connect("http://0.0.0.0:8080")

		print(self.sio.sid, " [CONNECTED]")



	def disconnect(self):
		""" Disconnects from the server """

		self.sio.disconnect()

