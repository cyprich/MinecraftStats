from player import Player
from categories import Categories


class Evaluater:
    def __init__(self, *args: Player):
        self._players = [p for p in args]
        self._points = {}

        for p in self._players:
            self._points[p.get_username()] = 0

        self._evaluate()

    def _sort(self, dictionary: dict, reverse: bool, extended_dictionary: bool = False) -> list[tuple]:
        if extended_dictionary:
            result = sorted(dictionary.items(), key=lambda item: item[1][0])
        else:
            result = sorted(dictionary.items(), key=lambda item: item[1])

        if reverse:
            return list(reversed(result))
        return list(result)

    def _print(self, result: list[tuple], category: Categories):
        print(f"Vyhodnotenie kategórie {category.short_desc.upper()} ({category.long_desc})")

        for i in range(len(result)):
            name = result[i][0]
            value = result[i][1]
            unit = ""

            match category.category:
                case 1:
                    unit = "hodín"
                case 2:
                    unit = "minút"
                case 3:
                    unit = "sekúnd"

            if category.category != 0:
                print(f"  {i + 1}. miesto: {name} (v priemere {category.action} raz za {value[0]} {unit}, celkovo {value[1]})")
            else:
                print(f"  {i + 1}. miesto: {name} nahral {value} hodín")

            self._points[name] += 3 - i

        print()

    def _evaluate(self):
        result = {}
        for c in Categories:
            for p in self._players:
                data = p.get_data(c.field_name)
                playtime = p.get_playtime()

                if c.category > 0 and data == 0:
                    result[p.get_username()] = (0, 0)

                else:
                    match c.category:
                        case 0:
                            result[p.get_username()] = data  # playtime
                        case 1:
                            result[p.get_username()] = (round(playtime / data, 1), round(data))  # per hour
                        case 2:
                            result[p.get_username()] = (round(playtime / data * 60, 1), round(data))  # per minute
                        case 3:
                            result[p.get_username()] = (round(playtime / data * 60 * 60, 1), round(data))  # per second

            self._print(self._sort(result, c.reverse, False if c.category == 0 else True), c)

    def print_points(self):
        print()
        print("Celkové umiestnenie")

        pos = 1
        for p in self._players:
            name = p.get_username()
            value = self._points[name]

            print(f"  {pos}. miesto: {name} získal {value} bodov")
            pos += 1
