from element_3 import ExampleElement

from slopped.web.template import flattenString


def renderDone(output):
    print(output)


flattenString(None, ExampleElement()).addCallback(renderDone)
