#!/usr/bin/python3
"""
text indection function
"""


def text_indentation(text):
    """
    text must be a string
    otherwise raise a TypeError exception with the message text
    must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/5-text_indentation.txt")
