import os
import re
import urllib.request

experts = [
    {
        "slug": "april-dunford",
        "name": "April Dunford",
        "topic": "Positioning",
        "url": "https://aprildunford.substack.com"
    },
    {
        "slug": "chris-walker",
        "name": "Chris Walker",
        "topic": "Demand Generation",
        "url": "https://refinelabs.com/blog"
    },
    {
        "slug": "dave-gerhardt",
        "name": "Dave Gerhardt",
        "topic": "Content Marketing",
        "url": "https://www.exitfive.com/newsletter"
    },
    {
        "slug": "peep-laja",
        "name": "Peep Laja",
        "topic": "Messaging & Conversion",
        "url": "https://cxl.com/blog/"
    },
    {
        "slug": "wes-bush",
        "name": "Wes Bush",
        "topic": "Product-Led Growth",
        "url": "https://productled.com/blog/"
    },
    {
        "slug": "elena-verna",
        "name": "Elena Verna",
        "topic": "Growth Strategy",
        "url": "https://elenaverna.com"
    },
    {
        "slug": "jason-lemkin",
        "name": "Jason Lemkin",
        "topic": "SaaS Scaling",
        "url": "https://www.saastr.com"
    },
    {
        "slug": "tk-kader",
        "name": "TK Kader",
        "topic": "Founder GTM",
        "url": "https://unstoppablegtm.com"
    },
    {
        "slug": "harry-stebbings",
        "name": "Harry Stebbings",
        "topic": "Executive Interviews",
        "url": "https://www.thetwentyminutevc.com"
    },
    {
        "slug": "rand-fishkin",
        "name": "Rand Fishkin",
        "topic": "SEO & Organic Growth",
        "url": "https://sparktoro.com/blog"
    }
]

base_dir = r"c:\Users\rinip\100hires-From-Rini-Puryani\research\other"
os.makedirs(base_dir, exist_ok=True)

for exp in experts:
    print(f"Fetching {exp['url']}...")
    try:
        req = urllib.request.Request(exp['url'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        # Basic HTML cleaning
        html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.IGNORECASE|re.DOTALL)
        html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.IGNORECASE|re.DOTALL)
        html = re.sub(r'<nav.*?>.*?</nav>', '', html, flags=re.IGNORECASE|re.DOTALL)
        html = re.sub(r'<footer.*?>.*?</footer>', '', html, flags=re.IGNORECASE|re.DOTALL)
        
        # Extract paragraphs and headers
        blocks = re.findall(r'<p.*?>(.*?)</p>|<h[1-3].*?>(.*?)</h[1-3]>', html, flags=re.IGNORECASE|re.DOTALL)
        
        extracted = []
        for block in blocks:
            for item in block:
                if item.strip():
                    clean = re.sub(r'<.*?>', '', item).strip()
                    # unescape some common html entities
                    clean = clean.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
                    # remove multiple whitespaces
                    clean = re.sub(r'\s+', ' ', clean)
                    if len(clean) > 20:  # Only keep somewhat meaningful sentences
                        extracted.append(clean)
                        
        # Take the first 30 meaningful text blocks to represent the "main content"
        content = "\n\n".join(extracted[:30])
        
        if not content.strip():
            content = "Could not extract readable text automatically."
            
    except Exception as e:
        print(f"Failed {exp['url']}: {e}")
        content = f"Failed to fetch content from URL: {e}"

    filepath = os.path.join(base_dir, f"{exp['slug']}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Other Content: {exp['name']}\n\n")
        f.write(f"**Topic:** {exp['topic']}\n\n")
        f.write(f"## Websites & Newsletters\n")
        f.write(f"**Source URL:** {exp['url']}\n\n")
        f.write(f"### Extracted Main Content\n\n")
        f.write(content + "\n")
        
print("All websites processed!")
