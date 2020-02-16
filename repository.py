class FileRepository:
    def __init__(self, data):
        self.data = data

    def store(self):
        with open('output.txt', "w") as file:
            file.write(self.data)

        print("data stored to file")


class ConsoleRepository:
    def __init__(self, data):
        self.data = data

    def store(self):
        print(self.data)
        print("data printed in console")


class Repository:
    def __init__(self, data, type='console',):
        self.__data = data
        self.__type = type

    def __store_factory(self):
        if self.__type == 'file':
            return FileRepository
        elif self.__type == 'console':
            return ConsoleRepository
        else:
            raise NotImplementedError

    def store(self):
        repository = self.__store_factory()
        repository(self.__data).store()
