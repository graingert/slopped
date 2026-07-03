from transparent_element import ExampleElement

from slopped.web.template import flattenString


def renderDone(output):
    print(output)


flattenString(None, ExampleElement()).addCallback(renderDone)
