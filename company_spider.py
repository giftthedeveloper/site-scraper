# import requests

# def get_website_url(site_name):
#     """Gets the website URL of the given site name.

#     Args:
#     site_name: The name of the website.

#     Returns:
#     The website URL.
#     """
#     url = 'https://www.{}.com'.format(site_name)
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.url
#     else:
#         return None

# if __name__ == '__main__':
#     site_name = input('Enter the name of the website: ')
#     website_url = get_website_url(site_name)
#     if website_url:
#         print('The website URL is: {}'.format(website_url))
#     else:
#         print('The website URL could not be found.')
