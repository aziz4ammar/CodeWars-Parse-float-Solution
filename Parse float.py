def parse_float(string):
    if isinstance(string, list):
        string = ''.join(map(str, string))
    try:
        return float(string)
    except ValueError:
        return None