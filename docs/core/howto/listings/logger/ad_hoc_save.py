import io

from ad_hoc import AdHoc

from slopped.logger import globalLogPublisher, jsonFileLogObserver

globalLogPublisher.addObserver(jsonFileLogObserver(open("log.json", "a")))

AdHoc(3, 4).logMessage()
