GET_EVENT, SET_EVENT = "get", "set"

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, value):
        self.value = value
        self.kind = GET_EVENT
        
        
class EventSet:
    def __init__(self, value):
        self.value = value
        self.kind = SET_EVENT


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            result = self.__successor.handle(obj, event)
            if event.kind == GET_EVENT:
                return result


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == GET_EVENT:
            if event.value == int:
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif event.kind == SET_EVENT:
            if isinstance(event.value, int):
                obj.integer_field = event.value
            else:
                super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == GET_EVENT:
            if event.value == float:
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif event.kind == SET_EVENT:
            if isinstance(event.value, float):
                obj.float_field = event.value
            else:
                super().handle(obj, event)



class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == GET_EVENT:
            if event.value == str:
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif event.kind == SET_EVENT:
            if isinstance(event.value, str):
                obj.string_field = event.value
            else:
                super().handle(obj, event)



# obj = SomeObject()
# obj.integer_field = -26
# obj.float_field = 4.9194
# obj.string_field = "cSxWPT"
# chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventGet(str)))
# print(chain.handle(obj, EventSet(100)))
# print(chain.handle(obj, EventGet(int)))
# print(chain.handle(obj, EventSet(0.5)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventSet('new text')))
# print(chain.handle(obj, EventGet(str)))