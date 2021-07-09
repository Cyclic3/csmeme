import sys
from typing import Optional

def do_copy(text: str) -> None:
    from tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()


handlers = {}


def process_one(args: list) -> Optional[str]:
    if len(args) == 0:
        return None
    keyword = args.pop(0).upper()
    return handlers.get(keyword)(args)


def process_all(args: list) -> str:
    text = ""
    while True:
        res = process_one(args)
        if res is None:
            break
        text += res
    return text

handlers = {
    "SILENT": lambda x: f"""playerradio Radio.WePlanted "{x.pop(0)}\u2028""",
    "CRINGE": lambda x: f"""playerradio DeathCry "{x.pop(0)}\u2028""",
    "HAX": lambda _: """playerradio DeathCry "CHUNGUS.EXITFRAG.RU\u2028""",
    "TEXT": lambda x: x.pop(0),
    "TRADE": lambda x: process_all(["ICON", "TEXT", x.pop(0), "WHITE", "TEXT", " has received in trade: ", x.pop(0), "TEXT", x.pop(0) + " | " + x.pop(0)]),
    "CASE": lambda x: process_all(["ICON", "TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", x.pop(0) + " | " + x.pop(0)]),
    "STAT": lambda x: process_all(["ICON", "TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", "StatTrak™ " + x.pop(0) + " | " + x.pop(0)]),
    "STAR": lambda x: process_all(["ICON", "TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", "★ " + x.pop(0) + " | " + x.pop(0)]),
    "VAC": lambda x: process_all(["RED", "TEXT", f"{x.pop(0)} has been permanently banned from official CS:GO servers."]),
    "ABANDON": lambda x: process_all(["RED", "TEXT", f"{x.pop(0)} abandoned the match and received a {x.pop(0)} competitive matchmaking cooldown."]),
    "NEWLINE": lambda _: '\u2028',
    "WHITE": lambda _: '\x01',
    "ICON": lambda _: '\x03',
    "RED": lambda _: '\x0F',
    # "KNIFE": lambda _: proce
}


if __name__ == "__main__":
    args = list(sys.argv[1:])
    text = ""
    while True:
        res = process_one(args)
        if res is None:
            break
        text += res
    text += '"'
    do_copy(text)
