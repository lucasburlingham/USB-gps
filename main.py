from gps import *
import asyncio
import websockets


running = True

gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)


async def send(websocket):
    while True:

        nx = gpsd.next()
        # For a list of all supported classes and fields refer to:
        # https://gpsd.gitlab.io/gpsd/gpsd_json.html
        if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', "Unknown")
            longitude = getattr(nx, 'lon', "Unknown")
            speed = getattr(nx, 'speed', "Unknown")

            # Eliminate normal GPS noise
            if speed < 1:
                speed = 0

            output = '[' + str(longitude) + ',' + \
                str(latitude) + ',' + str(speed) + ']'

            # Print to console
            print(output)

            # Send to websocket
            await websocket.send(output)
            await asyncio.sleep(2)

start_server = websockets.serve(send, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
