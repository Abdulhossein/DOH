import requests
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# آدرس فایل حاوی لیست سرویس‌دهنده‌ها
PROVIDERS_URL = 'https://github.com/Abdulhossein/DOH/raw/refs/heads/main/DoH%20provider%20URLs.txt'
README_PATH = 'README.md'

# تابع بررسی وضعیت یک سرویس
def check_doh_provider(url, timeout=10):
    try:
        # ارسال درخواست DoH برای یک دامنه ساده (مثل google.com)
        doh_url = f"{url.rstrip('/')}?name=google.com&type=A"
        headers = {'Accept': 'application/dns-json'}
        response = requests.get(doh_url, headers=headers, timeout=timeout)
        
        # بررسی موفقیت‌آمیز بودن پاسخ
        if response.status_code == 200:
            data = response.json()
            if 'Answer' in data and len(data['Answer']) > 0:
                return url, True
        return url, False
    except Exception:
        return url, False

# بارگذاری لیست سرویس‌دهنده‌ها
def load_providers():
    response = requests.get(PROVIDERS_URL)
    if response.status_code != 200:
        print("Failed to fetch providers list.")
        sys.exit(1)
    # خطوط خالی را حذف کرده و هر خط را به عنوان یک URL در نظر بگیرید
    providers = [line.strip() for line in response.text.splitlines() if line.strip()]
    return providers

# به‌روزرسانی جدول README با وضعیت‌های جدید
def update_readme(working_urls, non_working_urls):
    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()

    # پیدا کردن جدول وضعیت با استفاده از الگوی منظم
    table_pattern = r'(\| Who runs it \| Base URL \| Working\*\| Comment \|\n)(?:\|.*\|\n)*?(\n)'
    match = re.search(table_pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        print("Could not find status table in README.")
        sys.exit(1)
    
    # ساخت ردیف‌های جدید جدول
    new_rows = []
    for url in working_urls:
        # پیدا کردن نام سرویس‌دهنده از URL (برای پر کردن ستون اول)
        # شما می‌توانید این بخش را بر اساس ساختار README خود سفارشی کنید
        provider_name = url.split('/')[2] if '://' in url else 'Unknown'
        new_rows.append(f"| {provider_name} | {url} | :heavy_check_mark: | |")
    
    for url in non_working_urls:
        provider_name = url.split('/')[2] if '://' in url else 'Unknown'
        new_rows.append(f"| {provider_name} | {url} | :x: | |")
    
    # جایگزینی جدول قدیمی با جدول جدید
    new_table = match.group(1) + '\n'.join(new_rows) + match.group(2)
    updated_content = content[:match.start()] + new_table + content[match.end():]
    
    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"README updated. Working: {len(working_urls)}, Non-working: {len(non_working_urls)}")

# تابع اصلی
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
    
    print("\nUpdating README...")
    update_readme(working_urls, non_working_urls)
    
    print("Done!")
    sys.exit(0)

if __name__ == "__main__":
    main()
