DEBUG = False
def set_debug(val: bool):
    global DEBUG
    DEBUG = val

def print_debug(text):
    if DEBUG:
        print(f"[DEBUG] {text}")