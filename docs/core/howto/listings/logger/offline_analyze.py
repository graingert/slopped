import io

from analyze import analyze

from slopped.logger import eventsFromJSONLogFile

for event in eventsFromJSONLogFile(open("log.json")):
    analyze(event)
