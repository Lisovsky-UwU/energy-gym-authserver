from . import webgui


@webgui.route('/', defaults={'path': ''})
@webgui.route('/<path:path>')
def index(path):
    if not ('.' in path):
        return webgui.send_static_file('index.html')
    else:
        return webgui.send_static_file(path)
