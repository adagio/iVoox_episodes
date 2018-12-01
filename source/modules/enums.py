import enum

class ContentMode(enum.Enum):
    text = 0
    href_attribute = 1
    content_attribute = 2

class ValueType(enum.Enum):
    text = 0
    number = 1
