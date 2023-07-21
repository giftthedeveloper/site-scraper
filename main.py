import requests
import difflib

def suggest_website_name(site_name):
    """Generate website name suggestions by combining words.

    Args:
    site_name: The name of the website.

    Returns:
    A list of website name suggestions.
    """
    words = site_name.split()
    combinations = []
    for i in range(1, len(words) + 1):
        combinations.append(''.join(words[:i]))
    return combinations

def get_website_url(site_name):
    """Gets the website URL of the given site name.

    Args:
    site_name: The name of the website.

    Returns:
    The website URL or a list of suggestions if the URL is not found.
    """
    site_name = site_name.strip().replace(' ', '')
    url = 'https://www.{}.com'.format(site_name)
    response = requests.get(url)
    if response.status_code == 200:
        return response.url
    else:
        suggestions = suggest_website_name(site_name)
        closest_matches = difflib.get_close_matches(site_name, suggestions, n=3, cutoff=0.6)
        if closest_matches:
            return f"The website URL could not be found. Did you mean: {', '.join(closest_matches)}?"
        else:
            return "The website URL could not be found."

if __name__ == '__main__':
    site_name = input('Enter the name of the website: ')
    website_url = get_website_url(site_name)
    print(website_url)
