from checker import accountName

def account_to_nameTag(account: str, region: str):
    if not accountName(account):
        return Exception("Invalid account name")
    
    [name, tag] = account.split('#')
    if tag == '':
        tag = region.upper()
    return [name, tag]
