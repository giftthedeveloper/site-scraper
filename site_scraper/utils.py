import requests
import difflib

def suggest_website_name(site_name):
    words = site_name.split()
    combinations = []
    for i in range(1, len(words) + 1):
        combinations.append(''.join(words[:i]))
    return combinations

def get_website_url(site_name):

    try:
        site_name = site_name.strip().replace(' ', '')
        url = 'https://www.{}.com'.format(site_name)
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if response status is not 
        return response.url
    except requests.exceptions.RequestException:
        #give suggestions if you can't find the url
        suggestions = suggest_website_name(site_name)
        closest_matches = difflib.get_close_matches(site_name, suggestions, n=3, cutoff=0.6)
        suggestion_str = ', '.join(closest_matches)
        return f"Error: The website URL could not be found. Did you mean: {suggestion_str}?" if closest_matches else f"Error: The website URL could not be found."
    except Exception:
        return f"An unexpected error occurred while processing the request."

if __name__ == '__main__':
    site_name = input('Enter the name of the website: ')
    website_url = get_website_url(site_name)
    print(website_url)
