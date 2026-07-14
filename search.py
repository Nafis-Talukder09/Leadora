from ddgs import DDGS


def search_websites(keyword):

    print(f"\n🔍 Searching for: {keyword}")

    websites = []

    with DDGS() as ddgs:

        results = ddgs.text(
            keyword,
            max_results=100
        )

        for result in results:

            url = result.get("href")

            if url and url not in websites:
                websites.append(url)

    print(f"\n✅ Found {len(websites)} websites")

    return websites