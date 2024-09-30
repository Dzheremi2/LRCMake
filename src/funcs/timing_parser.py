import re
from ..variables import Variables

def parser(page):
    # Returns unrefined string
    pattern = r'\[([^\[\]]+)\]'
    return re.search(pattern, page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value)[0]

def get_ms(page):
    # Return refined string (in ms)
    pattern = r"(\d+):(\d+).(\d+)"
    mm, ss, ms = re.search(pattern, parser(page)).groups()
    print(f"{mm}:{ss}.{ms}")
    total_ss = int(mm) * 60 + int(ss)
    total_ms = total_ss * 1000 + int(ms)
    return total_ms