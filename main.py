import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

BITLINK_GENERATION_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
BITLINK_SUMMARY_URL = \
    'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}/clicks/summary'
BITLINK_CHECK_URL = 'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}'


def shorten_link(token, link):
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    payload = {'long_url': link}
    response = requests.post(
        BITLINK_GENERATION_URL,
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json().get('link')


def count_clicks(token, link):
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    parsed_link = urlparse(link)
    response = requests.get(
        BITLINK_SUMMARY_URL.format(parsed_link.netloc, parsed_link.path),
        headers=headers
    )
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_bitlink(token, link):
    headers = {'Authorization': 'Bearer {0}'.format(token)}
    parsed_link = urlparse(link)
    response = requests.get(
        BITLINK_CHECK_URL.format(parsed_link.netloc, parsed_link.path),
        headers=headers
    )
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    return parser


def main():
    load_dotenv('bitly_project.env')
    access_token = os.environ['BITLY_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    entered_link = args.link
    try:
        if is_bitlink(access_token, entered_link):
            counted_clicks = count_clicks(access_token, entered_link)
            print('Total clicks: {0}'.format(counted_clicks))
        else:
            print(shorten_link(access_token, entered_link))
    except requests.exceptions.HTTPError:
        print('Please enter a correct url!')


if __name__ == '__main__':
    main()
