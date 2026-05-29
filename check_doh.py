[1] 

import requests
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# آدرس فایل حاوی لیست سرویس‌دهنده‌ها
PROVIDERS_URL = 'https://github.com/Abdulhossein/DOH/raw/refs/heads/main/DoH%20provider%20URLs.txt'
README_PATH = 'README.md'

# تابع بررسی وضعیت یک سرویس (بدون تغییر)
def check_doh_provider(url, timeout=10):
    try:
        doh_url = f"{url.rstrip('/')}?name=google.com&type=A"
        headers = {'Accept': 'application/dns-json'}
        response = requests.get(doh_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            if 'Answer' in data and len(data['Answer']) > 0:
                return url, True
        return url, False
    except Exception:
        return url, False

def load_providers():
    response = requests.get(PROVIDERS_URL)
    if response.status_code != 200:
        print("Failed to fetch providers list.")
        sys.exit(1)
    providers = [line.strip() for line in response.text.splitlines() if line.strip()]
    return providers

# ==================== بخش جدید برای بازسازی کامل README ====================

def generate_full_readme(working_urls, non_working_urls):
    # 1. محتوای ثابت README که قبل از جدول می‌آید (لطفاً این متن را با محتوای واقعی فایل خودتان جایگزین کنید)
    readme_header = """# DoH - DNS over HTTPS

DoH queries resolve over HTTPS for privacy, performance, and security. DoH also makes it easier to use a name server of your choice instead of the one configured for your system.

# Spec
[RFC 8484 - DNS Queries over HTTPS (DoH)](https://tools.ietf.org/html/rfc8484)

# Publicly available servers

"""

    # 2. جدول جدید را به صورت کامل می‌سازیم
    # خط اول: هدرها
    table = "| Who runs it | Base URL | Working* | Comment |\n"
    # خط دوم: جداکننده‌ها (تراز چپ برای ستون اول و چهارم، وسط برای بقیه)
    table += "|:---|:---|:---:|:---|\n"

    # 3. ردیف‌های سرویس‌های فعال
    for url in working_urls:
        provider_name = url.split('/')[2] if '://' in url else 'Unknown'
        table += f"| {provider_name} | {url} | ✅ | |\n"

    # 4. ردیف‌های سرویس‌های غیرفعال
    for url in non_working_urls:
        provider_name = url.split('/')[2] if '://' in url else 'Unknown'
        table += f"| {provider_name} | {url} | ❌ | |\n"

    # کل محتوای فایل README را می‌سازیم
    full_readme_content = readme_header + table

    return full_readme_content

# ==================== بخش اصلی (بدون تغییر) ====================

def main():
    print("Loading DoH providers...")
    providers = load_providers()
    print(f"Found {len(providers)} providers to check.")

    working_urls = []
    non_working_urls = []

    print("Checking providers' statuses...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_doh_provider, url): url for url in providers}
        for future in as_completed(future_to_url):
            url, is_working = future.result()
            if is_working:
                working_urls.append(url)
                print(f"✓ {url}")
            else:
                non_working_urls.append(url)
                print(f"✗ {url}")

    print("\nRegenerating README...")
    # اینجا کل فایل README از نو ساخته می‌شود
    new_readme_content = generate_full_readme(working_urls, non_working_urls)

    # فایل را با محتوای جدید می‌نویسیم
    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(new_readme_content)

    print(f"README updated. Working: {len(working_urls)}, Non-working: {len(non_working_urls)}")
    print("Done!")

if __name__ == "__main__":
    main()
