from crawler import Parser
from repository import Repository


def get_element_path(element):
    def format_element(item):
        item_str = f'{item.tag}'
        item_class = item.attrib.get("class", "")
        if item_class:
            item_str += f'.{item_class}'
        return item_str

    tmp_list = []
    element_str = format_element(element)
    tmp_list.append(element_str)

    for item in element.iterancestors():
        item_str = format_element(item)
        tmp_list.append(item_str)

    path = '/'.join(tmp_list[::-1])
    return path


if __name__ == "__main__":
    xpath = '//div[@class="panel-body"]/*[normalize-space(text()) = "Make everything OK"]'

    parser = Parser(source_type='file', xpath=xpath, file_path='samples/sample-4-the-mash.html')
    element = parser.parse()

    if hasattr(element, 'text'):
        element_path = get_element_path(element)
        Repository(data=element_path).store()
    else:
        print("Element not found")
