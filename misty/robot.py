from misty.information import *
from misty.action import *


class Misty:
    def __init__(self, ip: str) -> None:
        self.ip = ip
        self.infos = Info(ip)
        self.actions = Action(ip)

    def __str__(self) -> str:
        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, string = "", dct = {}, method = "dict") -> bool:
        r = self.actions.perform_action(action_name, string, dct, method)
        return r

    def get_info(self, info_name: str) -> dict:
        r = self.infos.get_info(info_name)
        return r
