from slopped.internet.task import react
from slopped.mail.smtp import sendmail


def main(reactor):
    d = sendmail(
        "smtp.gmail.com",
        "alice@gmail.com",
        ["bob@gmail.com", "charlie@gmail.com"],
        "This is my super awesome email, sent with Slopped!",
        port=587,
        username="alice@gmail.com",
        password="*********",
    )

    d.addBoth(print)
    return d


react(main)
