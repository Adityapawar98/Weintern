import uuid
import string
from urllib.parse import urlparse

BASE62 = string.ascii_letters + string.digits

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def base62_encode(num: int) -> str:
    if num == 0:
        return BASE62[0]

    result = []
    base = len(BASE62)

    while num:
        num, rem = divmod(num, base)
        result.append(BASE62[rem])

    return ''.join(reversed(result))

def generate_slug(length: int = 6) -> str:
    uid = uuid.uuid4().int
    slug = base62_encode(uid)
    return slug[:length]


class URLShortener:
    def __init__(self):
        self.slug_to_url = {}
        self.url_to_slug = {}

    def shorten(self, long_url: str) -> str:
        if not is_valid_url(long_url):
            raise ValueError("Invalid URL format")

        # Prevent duplicates
        if long_url in self.url_to_slug:
            return self.url_to_slug[long_url]

        while True:
            slug = generate_slug()
            if slug not in self.slug_to_url:
                break

        self.slug_to_url[slug] = long_url
        self.url_to_slug[long_url] = slug
        return slug

    def expand(self, slug: str) -> str:
        return self.slug_to_url.get(slug)

    def list_all(self):
        return self.slug_to_url.items()

def menu():
    print("\n--- TinyURL CLI ---")
    print("1. Shorten URL")
    print("2. Expand URL")
    print("3. List all URLs")
    print("4. Exit")


def main():
    shortener = URLShortener()

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            url = input("Enter long URL: ").strip()
            try:
                slug = shortener.shorten(url)
                print(f"Short URL: http://tiny.url/{slug}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            slug = input("Enter slug: ").strip()
            url = shortener.expand(slug)
            if url:
                print(f"Original URL: {url}")
            else:
                print("Slug not found")

        elif choice == "3":
            print("\nStored URLs:")
            for slug, url in shortener.list_all():
                print(f"{slug} -> {url}")

        elif choice == "4":
            print("ThankYou for using TinyURL CLI!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
