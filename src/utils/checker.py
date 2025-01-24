
def accountName(accountName, region):
    if not accountName:
        return False
    if not isinstance(accountName, str):
        return False
    if len(accountName) < 3:
        return False
    if len(accountName) > 30:
        return False
    if '#' not in accountName:
        return False
    return True