def get_domain_name(url: str) -> str:
    if '//' in url:
        url = url.split('//')
        if 'www.' in url[1]:
            url_domain = url[1].split('.')
            return url_domain[1]
        else:
            url_domain = url[1].split('.')
            return url_domain[0]
    else:
        url = url.split('.')
        return url[1]    
