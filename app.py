import requests

from search import search_websites
from parser import find_contact_links
from crawler import crawl_contact_pages
from extractor import extract_data
from exporter import save_leads
from company import get_company_name


keyword = input("Enter Keyword: ")

websites = search_websites(keyword)

print(f"\n✅ Found {len(websites)} websites\n")

all_leads = []

for index, website in enumerate(websites, start=1):

    print("=" * 60)
    print(f"[{index}/{len(websites)}] Scanning: {website}")

    try:

        response = requests.get(
            website,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code != 200:
            continue

        html = response.text

        company_name = get_company_name(html)

        links = find_contact_links(html)

        pages = crawl_contact_pages(
            website,
            links
        )

        for url, page_html in pages:

            data = extract_data(page_html)

            data["website"] = url
            data["company"] = company_name

            all_leads.append(data)

            print(url)
            print("Company :", company_name)
            print("Emails  :", data["emails"])
            print("Phones  :", data["phones"])

    except Exception as e:

        print("Error:", e)

save_leads(all_leads)

print("\n==============================")
print("Finished")
print("Total Leads:", len(all_leads))
print("==============================")