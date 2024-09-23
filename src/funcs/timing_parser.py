import re
from ..variables import Variables

def parser(page):
    # Returns unrefined string
    pattern = r'([^\[\]]+)'
    return re.search(pattern, page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value)[0]

def get_ms(page):
    # Return refined string (in ms)
    return int(parser(page).replace(":", "").replace(".", ""))