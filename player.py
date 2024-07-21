import string
import requests
import json
from categories import Categories


class Player:
    def __init__(self, uuid: string, path: string):
        self._uuid = uuid
        self._username = self._request_username()
        self._path = path

        self._data = {}
        self._load_data()

    def get_username(self) -> string:
        return self._username

    def get_playtime(self) -> int:
        return self._data["play_time"]

    def get_data(self, field_name: string):
        return self._data[field_name]

    # getting username from api
    def _request_username(self):
        url = f"https://sessionserver.mojang.com/session/minecraft/profile/{self._uuid}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                name = response.json()["name"]
                return name

        except Exception:
            print(f"Failed to load username for followng id: {self._uuid}. Using uuid instead of name {Exception}")
            return self._uuid

    # loading data from file
    def _load_data(self):
        with open(f"{self._path}/{self._uuid}.json", "r") as file:
            data = json.load(file)["stats"]

        for c in Categories:
            if c.field_name != "mined" and c.field_name != "killed" and c.field_name != "broken":
                self._data[c.field_name] = round(data["minecraft:custom"][f"minecraft:{c.field_name}"] / c.divide_by, 1)
            else:
                self._data[c.field_name] = 0
                try:
                    for i in data[f"minecraft:{c.field_name}"]:
                        self._data[c.field_name] += data[f"minecraft:{c.field_name}"][i]
                except KeyError:
                    self._data[c.field_name] = 0
