import re
from bs4 import BeautifulSoup


def extract_data(html):

    soup = BeautifulSoup(html, "html.parser")

    emails = list(set(re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        html
    )))

    phones = re.findall(
        r"(?:\+?\d[\d\s().-]{7,}\d)",
        html
    )

    clean_phones = []

    for phone in phones:

        digits = re.sub(r"\D", "", phone)

        if len(digits) < 8:
            continue

        if len(set(digits)) <= 2:
            continue

        clean_phones.append(phone.strip())

    phones = list(set(clean_phones))

    facebook = []
    instagram = []
    linkedin = []
    x = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if "facebook.com" in href:
            facebook.append(href)

        elif "instagram.com" in href:
            instagram.append(href)

        elif "linkedin.com/company" in href:
            linkedin.append(href)

        elif "twitter.com" in href or "x.com" in href:
            x.append(href)

    return {
        "emails": list(set(emails)),
        "phones": phones,
        "facebook": list(set(facebook)),
        "instagram": list(set(instagram)),
        "linkedin": list(set(linkedin)),
        "x": list(set(x))
    }