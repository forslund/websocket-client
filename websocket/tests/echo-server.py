#!/usr/bin/env python

# From https://github.com/aaugustin/websockets/blob/main/example/echo.py

import asyncio
import websockets


async def echo(websocket, path):
    print(">>>>>>>>>>>>>>>>> In echo async! <<<<<<<<<<<<<<<<<")
    async for message in websocket:
        print(">>>>>>>>>>> ECHO <<<<<<<<<<<<<<<")
        await websocket.send(message)


async def main():
    print(">>>>>>>>>>>>>>>> in async main <<<<<<<<<<<<<<<<<<<")
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
print(">>>>>>>>>>>>>>>> Running forever! <<<<<<<<<<<<<<<<<<")
loop.run_forever()
print("DONE!")
