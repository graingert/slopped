import io
import sys

from slopped.logger import eventsFromJSONLogFile, textFileLogObserver

output = textFileLogObserver(sys.stdout)

for event in eventsFromJSONLogFile(open("log.json")):
    output(event)
