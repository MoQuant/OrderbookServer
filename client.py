import websocket
import json
import time

dt = lambda: int(time.time())
t0 = dt()

c = websocket.create_connection('ws://localhost:8080')

while True:
    data = c.recv()
    print(f'Running: {dt() - t0} | {len(data)}')