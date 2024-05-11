from . import webgui


@webgui.route('/', defaults={'path': ''})
@webgui.route('/<path:path>')
async def index(path):
    if not ('.' in path):
        return await webgui.send_static_file('index.html')
    else:
        return await webgui.send_static_file(path)