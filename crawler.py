import requests
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0"
}


def crawl_contact_pages(base_url, links):

    pages = []

    visited = set()

    for link in links:

        full_url = urljoin(base_url, link)

        if full_url in visited:
            continue

        visited.add(full_url)

        try:

            response = requests.get(
                full_url,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:

                pages.append(
                    (full_url, response.text)
                )

        except:

            continue

    return pages