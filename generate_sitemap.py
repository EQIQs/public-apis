import xml.etree.ElementTree as ET
from datetime import datetime
import itertools

def generate_sitemap():
    base_url = "https://www.eqiqs.com"
    frameworks = [
        "temperament", "communication-style", "conflict-style", "career-anchors",
        "values-ethics", "cognitive-aptitude", "big-five", "mbti", "disc",
        "enneagram", "attachment-style", "eq-assessment", "conscientiousness",
        "riasec", "love-language", "leadership-style", "work-values",
        "cognitive-style", "neuro-blueprint", "western-zodiac", "chinese-zodiac"
    ]
    
    # Static pages
    static_pages = [
        "/", "/unified-engine", "/features/customizable-framework-selection", "/features/ai-match-suggestions",
        "/frameworks", "/pricing", "/how-it-works", "/sample-reports", "/compatibility-api"
    ]
    
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Add static pages
    for page in static_pages:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = base_url + page
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "weekly"
        # Set higher priority for the new unified-engine page
        priority = "1.0" if page == "/unified-engine" else "0.8"
        ET.SubElement(url, "priority").text = priority

    # Add individual framework pages
    for fw in frameworks:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}/framework/{fw}"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "monthly"
        ET.SubElement(url, "priority").text = "0.7"

    # Add framework combinations (e.g., mbti-vs-disc)
    # To keep the sitemap manageable, we'll generate combinations of the most popular frameworks
    # The user specifically mentioned "every framework combination", but 21*20 combinations might be too many for a single sitemap if not filtered.
    # However, I will follow the instruction for "every framework combination" but maybe limit to pairs to start.
    combinations = list(itertools.permutations(frameworks, 2))
    for fw1, fw2 in combinations:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}/frameworks/{fw1}-vs-{fw2}"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "monthly"
        ET.SubElement(url, "priority").text = "0.6"

    # Relationship Intelligence combinations (e.g., enneagram-relationship-intelligence)
    for fw in frameworks:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}/frameworks/{fw}-relationship-intelligence"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "monthly"
        ET.SubElement(url, "priority").text = "0.6"

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write("/home/ubuntu/sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Sitemap generated with {len(urlset)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
