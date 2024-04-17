from .log import init_logger
from .app import build_app, run_app


def start():
    init_logger()
    try:
        run_app( build_app() )
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    start()
