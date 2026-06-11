import requests
import xml.etree.ElementTree as ET
import os

def ping_google_indexing(sitemap_path):
    # Note: Google's direct sitemap ping endpoint was deprecated in 2023.
    # The modern way is using the Google Search Console Indexing API or just updating the sitemap in robots.txt.
    # However, for programmatic indexing of new URLs, the Indexing API is preferred.
    # This script simulates the logic for the Indexing API.
    
    print(f"Reading sitemap from {sitemap_path}...")
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        print(f"Found {len(urls)} URLs. Pinging Google Search Console Indexing API...")
        
        # In a real production environment, we would use google-auth and the Indexing API.
        # Since I don't have the service account JSON, I will provide the template code.
        
        # Example Indexing API request:
        # endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
        # for url in urls:
        #     payload = {"url": url, "type": "URL_UPDATED"}
        #     # response = requests.post(endpoint, json=payload, auth=...)
        #     print(f"Indexed: {url}")
        
        print("Indexing request simulation complete.")
        print("Note: In production, ensure GOOGLE_APPLICATION_CREDENTIALS is set.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ping_google_indexing("/home/ubuntu/sitemap.xml")
