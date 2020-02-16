from lxml import etree


class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __read_file(self, file_path):
        try:
            tree = etree.parse(file_path)
            return tree
        except (FileNotFoundError, PermissionError) as err:
            print(err)

    def get_html(self):
        data = self.__read_file(self.file_path)
        return data


class Parser:
    def __init__(self, source_type: str,  xpath: str, url=None, file_path=None):
        self.source_type = source_type
        self.url = url
        self.xpath = xpath
        self.file_path = file_path

    def validate_init_params(self):
        pass

    def loader_factory(self, source_type):
        if source_type == 'file':
            return FileLoader(self.file_path)
        else:
            raise NotImplementedError

    def universal_parser(self, tree):
        try:
            item = tree.xpath(self.xpath)
            return item
        except Exception as err:
            print(err)

    def parse(self):
        loader = self.loader_factory(self.source_type)
        tree = loader.get_html()
        element = self.universal_parser(tree)

        return element[0] if element else None
