from parser import find_contact_links
import requests

website = input("Enter Website URL: ")

try:
    response = requests.get(
        website,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    if response.status_code == 200:

        print("✅ Website Loaded Successfully")

        html = response.text

        links = find_contact_links(html)

        print("\n========== CONTACT LINKS ==========\n")

        if links:
            for link in links:
                print(link)
        else:
            print("No Contact Links Found")

        print("\n========== FIRST 500 CHARACTERS ==========\n")
        print(html[:500])

    else:
        print(f"Website returned {response.status_code}")

except Exception as e:
    print("Error:", e)