def field(items, *args):
    assert len(args) > 0
    result = []

    for good in items:
        d = {arg: good[arg] for arg in args}
        result.append(d)
    return result

