import sys
from typing import Optional

def do_copy(text: str) -> None:
    if sys.platform == "linux":
        from tkinter import Tk
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
    else:
        import pyperclip
        pyperclip.copy(text)


handlers = {}

def process_one(args: list) -> Optional[str]:
    if len(args) == 0:
        return None
    keyword = args.pop(0).upper()
    fun = handlers.get(keyword)
    if fun is None:
        raise Exception("Invalid command: " + keyword)
    return fun(args)


def process_all(args: list) -> str:
    text = ""
    while True:
        res = process_one(args)
        if res is None:
            break
        text += res
    return text

handlers = {
    "T_HAX": lambda x: process_all(["CRINGE", "TEXT", "CHUNGUSAIM.RU", "NEWLINE", "RED", "TEXT", f"{x.pop(0)} has been permanently banned from official CS:GO servers."]),
    "T_VAC": lambda x: process_all(["SILENT", "NEWLINE", "RED", "TEXT", f"{x.pop(0)} has been permanently banned from official CS:GO servers."]),
    "T_CASE": lambda x: process_all(["SILENT", "NEWLINE", "CASE", x.pop(0), "RED", "AWP", "Dragon Lore"]),
    "T_STAT": lambda x: process_all(["SILENT", "NEWLINE", "STAT", x.pop(0), "RED", "AWP", "Dragon Lore"]),
    "T_FTS": lambda x: process_all(["SILENT", "NEWLINE", "ABANDON", x.pop(0), "7 day"]),
    "T_SUDO": lambda x: process_all(["SILENT", "NEWLINE", "DEFAULT", "TEXT", f'{x.pop(0)} : ', "WHITE", "TEXT", x.pop(0) ]),
    "T_SUDOCT": lambda x: process_all(["SILENT", "NEWLINE", "DEFAULT", "TEXT", f'(Counter-Terrorist) {x.pop(0)} : ', "WHITE", "TEXT", x.pop(0)]),
    "T_SUDOT": lambda x: process_all(["SILENT", "NEWLINE", "DEFAULT", "TEXT", f'(Terrorist) {x.pop(0)} : ', "WHITE", "TEXT", x.pop(0)]),

    "SILENT": lambda x: f'playerradio Radio.WePlanted "',
    "CRINGE": lambda x: f'playerradio DeathCry "',

    "TEXT": lambda x: x.pop(0),
    "TRADE": lambda x: process_all(["TEXT", x.pop(0), "WHITE", "TEXT", " has received in trade: ", x.pop(0), "TEXT", x.pop(0) + " | " + x.pop(0)]),
    "CASE": lambda x: process_all(["TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", x.pop(0) + " | " + x.pop(0)]),
    "STAT": lambda x: process_all(["TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", "StatTrak™ " + x.pop(0) + " | " + x.pop(0)]),
    "STAR": lambda x: process_all(["TEXT", x.pop(0), "WHITE", "TEXT", " has opened a container and found: ", x.pop(0), "TEXT", "★ " + x.pop(0) + " | " + x.pop(0)]),
    "VAC": lambda x: process_all([]),
    "ABANDON": lambda x: process_all(["RED", "TEXT", f"{x.pop(0)} abandoned the match and received a {x.pop(0)} competitive matchmaking cooldown."]),
    "NEWLINE": lambda _: '\u2028',
    "COL": lambda x: chr(x.pop()),
    "DEFAULT": lambda _: '\x03',
    "RED": lambda _: '\x07',
    "WHITE": lambda _: '\x01',
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
