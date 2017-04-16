import os
import sys

import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2

sys.path.append(os.getcwd().replace('www/aio', ''))
import zodiac

@aiohttp_jinja2.template('index.html')
async def index(request):
    return

def sample(request):
    return web.Response(text='Sample')

async def zodiac_message(request):
    zmessage = request.match_info.get('zmessage', 'None')
    if zmessage == 'None':
        return web.Response(text='...')

    message = await zodiac.zodiac(zmessage)
    return web.Response(text=message)


app = web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/sample', sample)
app.router.add_route('GET', '/{zmessage}', zodiac_message)


templates = os.path.join(os.getcwd(), 'www', 'templates')
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(templates))

web.run_app(app, host='127.0.0.1', port=8080)
