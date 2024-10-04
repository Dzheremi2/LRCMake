from ...variables import variables

def split_text_on_lines(page):
    list = ((page.controls[2].value).splitlines())
    list.append("")
    variables.current_lyrics_list = list
    return list

def split_text_on_lines_cnt(page):
    return len((page.controls[2].value).splitlines())