from misty.information import *
from misty.action import *


class Misty:
    def __init__(self, ip: str) -> None:
        self.ip = ip
        self.infos = Info(ip)
        self.actions = Action(ip)

    def __str__(self) -> str:
        return "A Misty II robot with IP address %s" % self.ip

    def action(self, endpoint: str, data: dict) -> bool:
        r = self.actions.perform_action(endpoint, data)
        return r

    def info(self, endpoint: str) -> dict:
        r = self.infos.get_info(endpoint)
        return r
