from enum import Enum
import string


class Categories(Enum):
    PLAYTIME = ("play_time", "Najväčší hráč", "Hráč, ktorý strávil najviac času hraním na serveri", "", 0, 72_000, True)
    DEATHS = ("deaths", "Zdochlina", "Hráč, ktorý najviac krát zomrel", "zomrel", 1)
    JUMPS = ("jump", "Hopko skočko", "Hráč, ktorý najviac krát vyskočil", "vyskočil", 3)
    SLEEP = ("sleep_in_bed", "Spachtoš roka", "Hráč, ktorý najviac krát išiel spať", "spal", 2)
    # FLY = ("fly_one_cm", "Celkom úlet", "Hráč, ktorý najviac lietal", " km", 2, 100_000)
    # SPRINT = ("sprint_one_cm", "Unavené nohy", "Hráč, ktorý najviac utekal", " km", 1, 100_000)
    # WALK = ("walk_one_cm", "Nie až tak unavené nohy", "Hráč, ktorý najviac kráčal", " km", 1, 100_000)
    DAMAGE_DEALT = ("damage_dealt", "Bitkár", "Hráč, ktorý spôsobil najviac damage", "ubral srdiečko", 3)
    DAMAGE_TAKEN = ("damage_taken", "Zbitý", "Hráč, ktorý dostal najviac damage", "stratil srdiečko", 3)
    MINED = ("mined", "Baník", "Hráč, ktorý vykopal najviac blokov", "vykopal blok", 3)
    KILLED = ("killed", "Zabijak", "Hráč, ktorý zabil najviac tvorov", "zabil tvora", 3)
    BROKEN = ("broken", "Kazič", "Hráč, ktorý zničil najviac nástrojov", "zničil nástroj", 1, 1, True)

    def __init__(
            self, field_name: string, short_desc: string, long_desc: string, action: string, category: int,
            divide_by: int = 1,
            reverse: bool = False
    ):
        self.field_name = field_name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.action = action
        self.category = category
        self.divide_by = divide_by
        self.reverse = reverse
