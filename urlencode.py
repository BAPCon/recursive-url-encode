from urllib.parse import quote

def recursive_urlencode(d):

    def add_item_str(key, value, base):
        pairs = []
        new_base = base + [key]
        if isinstance(value, (list, dict, tuple)):
            pairs += recursion(value, new_base)
        else:
            if len(new_base) > 1:
                first = quote(str(new_base.pop(0)))
                rest = map(lambda x: quote(x), (str(x) for x in new_base))
                new_pair = f"{first}[{']['.join(str(x) for x in rest)}]={quote(to_utf8(value))}"
            else:
                new_pair = f"{quote(to_utf8(key))}={quote(to_utf8(value))}"
            pairs.append(new_pair)
        return pairs

    def recursion(d, base=[]):
        pairs = []

        if isinstance(d, (dict, list, tuple)):
            for key, value in (d.items() if isinstance(d, dict) else enumerate(d)):
                pairs += add_item_str(key, value, base)
        return pairs

    return '&'.join(recursion(d))

def to_utf8(s):
    return str(s).encode('utf-8')