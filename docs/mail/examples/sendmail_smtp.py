from slopped.internet.task import react
from slopped.mail.smtp import sendmail


def main(reactor):
    d = sendmail(
        "myinsecuremailserver.example.com",
        "alice@example.com",
        ["bob@gmail.com", "charlie@gmail.com"],
        "This is my super awesome email, sent with Slopped!",
    )

    d.addBoth(print)
    return d


react(main)
