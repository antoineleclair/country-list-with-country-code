import urllib, json, unicodedata

def get_list(username='demo', lang='en'):
    """Fetches the json of all countries from geonames.org."""
    params = urllib.urlencode({'lang': lang, 'username': username})
    url = 'http://api.geonames.org/countryInfoJSON?%s' % params
    f = urllib.urlopen(url)
    response_text = f.read()
    return json.loads(response_text)["geonames"]

def country_list_generator(country_list, func):
    """Returns a generator of countries.
    They are sorted alphabetically,
    and the func passed as argument is applied to each of them."""
    ordered = sorted(country_list,
        key=lambda k: strip_accents(k['countryName']))
    return (func(country) for country in ordered)

def country_to_option(country):
    """Transforms a country dict to an html option tag,
    The country code is used for the value."""
    return ('<option value="%s">%s</option>\n' % \
        (country['countryCode'], country['countryName'])).encode('utf-8')

def country_to_csharp_dict_pair(country):
    """Transforms a country dict to a C# Dictionary pair.""" 
    return ('{"%s", "%s"},\n' % \
        (country['countryCode'], country['countryName'])).encode('utf-8')
    
def strip_accents(s):
    """Removes the accents from a unicode string.
    This function is used for sorting."""
    return ''.join((c for c in unicodedata.normalize('NFD', s) \
                        if unicodedata.category(c) != 'Mn'))

if __name__ == '__main__':
    country_list = get_list('demo', lang='en')
    with open('output.txt', 'w') as f:
        gen = country_list_generator(country_list, country_to_option)
        f.writelines(gen)
