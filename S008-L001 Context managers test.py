class Htmlcm:
    def __init__(self):
        pass

    def __enter__(self):
        self.__begin = '<TABLE><TR><TH>Number</TH></TR>'
        return print(self.__begin)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end = '</TABLE>'
        return print(self.__end)


with Htmlcm():
    pass
