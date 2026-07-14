from bs4 import BeautifulSoup


def get_company_name(html):

    soup = BeautifulSoup(html, "html.parser")

    if soup.title:
        return soup.title.text.strip()

    return "Unknown"