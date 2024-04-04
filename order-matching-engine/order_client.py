import asyncio
import websockets
import json
import random

async def send_order():
    websocket_url = "ws://localhost:8000"
    async with websockets.connect(websocket_url) as ws:
        while True:
            # Create an order
            order = {
                "type": "order",
                "price": random.randrange(200, 210),
                "quantity": random.randint(1, 100),
                "is_buy": random.choice([True, False])
            }

            # Send the order to the server
            await ws.send(json.dumps(order))

            # Wait for the response from the server
            response = await ws.recv()
            print(f"Server response: {response}")

            # Wait for some time before sending the next order
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(send_order())