from enum import Enum


class EmailConstants(Enum):
    WELCOME_SUBJECT = "Welcome Message"
    HTML_TYPE = "html"

    def __repr__(self) -> str:
        return self.value
