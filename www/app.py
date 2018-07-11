import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

#define a request handler, which will return a testing page
def url_handler_testingpage(request):
	return web.Response(body=b'<h1>Hi gay!</h1><p>you are visiting my testing web-page, just enjoy yourself.</p>', content_type="text/html")

def url_handler_hello(request):
	return web.Response(body=b'<h1>Hello frends</h1>', content_type="text/html")


async def init(loop):
	#create a Application instance
	app = web.Application(loop=loop)
	#register the request handle
	app.router.add_route('GET', '/test', url_handler_testingpage)
	app.router.add_route('GET', '/hello', url_handler_hello)
	#建立服务器协程，监听9002端口
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9002)
	#相当于print
	logging.info('server started at http://127.0.0.1:9002')
	return srv

#创建异步框架的事件轮询实例
loop = asyncio.get_event_loop()

loop.run_until_complete(init(loop))
loop.run_forever()
