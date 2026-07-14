from bs4 import BeautifulSoup


def find_contact_links(html):

    soup = BeautifulSoup(html, "html.parser")

    contact_links = []

    keywords = [
        "contact",
        "contact-us",
        "support",
        "help",
        "about",
        "team",
        "company",
        "sales",
        "demo",
        "book",
        "get-in-touch"
    ]

    for link in soup.find_all("a", href=True):

        href = link["href"]

        href_lower = href.lower()

        if any(word in href_lower for word in keywords):

            contact_links.append(href)

    return list(set(contact_links))