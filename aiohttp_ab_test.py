from aiohttp import web
import json

async def wshandle(request):
    text = json.dumps({'hello': 'world'})
    text += request.match_info.get("name", "no name param")
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get("/", wshandle),
                web.get("/{name}", wshandle)])
web.run_app(app)

