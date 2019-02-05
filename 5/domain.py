def domain_name(url):
    result = url.split("//")[-1].split("/")[0].split('?')[0]
    if result[0:4] == 'www.':
        strng = result[4:]
    else:
        strng = result

    return strng.split('.')[0]
