import inspect
import logging
logger = logging.getLogger(__name__)

class EventHandler:

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        try:
            self.__handlers.remove(handler)
        except ValueError:
            pass
        return self

    def __call__(self, *args, **kwargs):
        for handler in self.__handlers:
            handler(*args, **kwargs)

    async def invoke_async(self, *args, **kwargs):
        for handler in self.__handlers:
            if inspect.iscoroutinefunction(handler):
                await handler(*args, **kwargs)
            else:
                handler(*args, **kwargs)
