def field(items, *args):
    assert len(args) > 0
    result = []

    for good in items:
        d = {arg: good[arg] for arg in args}
        if len(d.keys()) == 1:
            d = list(d.values())
            result += d
        else:
            result.append(d)
    return result
