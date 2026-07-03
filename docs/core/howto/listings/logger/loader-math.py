import io

from slopped.logger import eventsFromJSONLogFile

for event in eventsFromJSONLogFile(open("log.json")):
    print(sum(event["values"]))
