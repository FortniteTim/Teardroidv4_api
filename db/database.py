from deta import Deta
from os import getenv

deta = Deta(getenv("a0eml3km_WDU5wkUshKuAAJg1ECCe5sgphS96VD7M"))


def client_db():
    return deta.Base("client")


def notification_db():
    return deta.Base("notification")


def command_db():
    return deta.Base("command")


def auth_db():
    return deta.Base("auth")


async def tear_drive():
    return deta.Drive("teardroid")
