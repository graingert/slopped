# simple-finger.tac
# eg:  slopd -ny simple-finger.tac

import finger

from slopped.application import service

options = {
    "file": "/etc/users",
    "templates": "/usr/share/finger/templates",
    "ircnick": "fingerbot",
    "ircserver": "irc.freenode.net",
    "pbport": 8889,
    "ssl": "ssl=0",
}

ser = finger.makeService(options)
application = service.Application("finger", uid=1, gid=1)
ser.setServiceParent(service.IServiceCollection(application))
