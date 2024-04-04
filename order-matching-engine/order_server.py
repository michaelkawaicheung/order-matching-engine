import asyncio
import websockets
import json
from datetime import datetime

class Order:
    def __init__(self, price, quantity, is_buy):
        self.price = price
        self.quantity = quantity
        self.is_buy = is_buy
        self.order_time = datetime.now()

class OrderBook:
    def __init__(self):
        self.orders = []
        self.last_price = None

    def process_order(self, order):

        print(f"New order received: Price={order.price}, Quantity={order.quantity}, Buy={order.is_buy}, Time={order.order_time}")

        if order.is_buy:
            self.process_buy_order(order)
        else:
            self.process_sell_order(order)

        self.last_price = order.price

        self.orders.append(order)

    def process_buy_order(self, buy_order):
        for i, sell_order in enumerate(self.orders):
            if sell_order.is_buy:
                continue

            if buy_order.price >= sell_order.price:
                matched_quantity = min(buy_order.quantity, sell_order.quantity)

                # Execute the matched orders
                self.execute_order(buy_order, matched_quantity)
                self.execute_order(sell_order, matched_quantity)

                if sell_order.quantity == 0:
                    # Remove the sell order from the order book
                    del self.orders[i]

                if buy_order.quantity == 0:
                    # No remaining quantity in the buy order
                    break

    def process_sell_order(self, sell_order):
        for i, buy_order in enumerate(self.orders):
            if not buy_order.is_buy:
                continue

            if sell_order.price <= buy_order.price:
                matched_quantity = min(sell_order.quantity, buy_order.quantity)

                # Execute the matched orders
                self.execute_order(sell_order, matched_quantity)
                self.execute_order(buy_order, matched_quantity)

                if buy_order.quantity == 0:
                    # Remove the buy order from the order book
                    del self.orders[i]

                if sell_order.quantity == 0:
                    # No remaining quantity in the sell order
                    break

    def execute_order(self, order, quantity):
        order.quantity -= quantity

        print(f"Order executed: Price={order.price}, Quantity={quantity}, Time={datetime.now()} Last traded price: {self.last_price}")

        if order.quantity > 0:
            # The order still has remaining quantity, update the order book
            self.orders.append(order)

async def handle_order(websocket, path):
    async for message in websocket:
        order_data = json.loads(message)

        if order_data["type"] == "order":
            order = Order(order_data["price"], order_data["quantity"], order_data["is_buy"])
            order_book.process_order(order)

            # Send response to the client
            response = {"status": "Order processed successfully"}
            await websocket.send(json.dumps(response))
        else:
            # Invalid message format
            response = {"status": "Invalid message format"}
            await websocket.send(json.dumps(response))

order_book = OrderBook()
start_server = websockets.serve(handle_order, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()