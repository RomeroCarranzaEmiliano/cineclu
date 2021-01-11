"""
	ws.py

	The websocket server
"""

# IMPORTS #########################################################################################
from aiohttp import web
import socketio
###################################################################################################

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
	return web.Response(text="Hello World", content_type="text/html")

""" Default connection function """
@sio.event
def connect(sid, envidorn):
	print(sid, ' connected')

""" Default disconnection function """
@sio.event
def disconnect(sid):
	print(sid, ' disconnected')

@sio.on('message')
def print_message(sid, message):
	print("socket id: ", sid)
	print(message)


app.router.add_get('/', index)

if __name__ == '__main__':
	web.run_app(app)