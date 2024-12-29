from enum import Enum
from pydantic import BaseModel, computed_field
from typing import ClassVar

"""
"default"
"dark"
"light"
"accent"
"good"
"warning"
"attention"
"""


class Color(Enum):
    DEFAULT = "default"
    DARK = "dark"
    LIGHT = "light"
    ACCENT = "accent"
    GOOD = "good"
    WARNING = "warning"
    ATTENTION = "attention"


class Element(BaseModel):
    @computed_field
    @property
    def type(self) -> str:
        return self.__class__.__name__

    def json(self):
        return self.model_dump_json()


class TextBlock(Element):
    text: str
    color: Color


class Image(Element):
    url: str
    size: str


class Container(BaseModel):
    items: list[Element]


text1 = TextBlock(text="hola", color=Color.DARK)

print(text1.json())


# print(text1)

# # text1.type = "TextBlockxxxxxxxx"

# # text1.type = "TextBlockxxxxxxxx"
# print(text1.type)
