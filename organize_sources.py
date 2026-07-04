import os
from datetime import datetime

experts = [
    {
        "name": "April Dunford",
        "slug": "april-dunford",
        "topic": "Positioning",
        "linkedin": "**Positioning in the Age of AI** – membahas bagaimana perusahaan SaaS perlu memiliki point of view yang jelas dan memposisikan produk di era AI. [LinkedIn Post](https://www.linkedin.com/posts/aprildunford_in-todays-newsletter-im-talking-about-activity-7463238631441403904-hHDU?utm_source=chatgpt.com)",
        "other": "**In the Age of AI, You Need a Point of View** (Substack) – newsletter tentang positioning untuk SaaS dan AI companies. [Newsletter](https://aprildunford.substack.com?utm_source=chatgpt.com)",
        "annotation": "Pakar terkemuka di bidang product positioning yang membantu perusahaan B2B SaaS menonjol di pasar yang ramai melalui framework 'Obviously Awesome'."
    },
    {
        "name": "Chris Walker",
        "slug": "chris-walker",
        "topic": "Demand Generation",
        "linkedin": "**Demand Gen Isn't Lead Gen** – menjelaskan mengapa demand generation harus berfokus pada menciptakan permintaan, bukan sekadar MQL. [LinkedIn Profile & Posts](https://www.linkedin.com/in/chriswalker171/?utm_source=chatgpt.com)",
        "other": "**Refine Labs Blog** – kumpulan artikel tentang Demand Generation, Dark Social, dan Revenue Marketing. [Refine Labs Blog](https://refinelabs.com/blog?utm_source=chatgpt.com)",
        "annotation": "Pelopor konsep Demand Generation dan Dark Social, berfokus pada transisi dari model lead generation tradisional (MQL) ke strategi yang berpusat pada revenue."
    },
    {
        "name": "Dave Gerhardt",
        "slug": "dave-gerhardt",
        "topic": "Content Marketing",
        "linkedin": "**Founder-Led Marketing** – post mengenai pentingnya founder menjadi wajah utama content marketing B2B. [LinkedIn Profile & Posts](https://www.linkedin.com/in/davegerhardt/?utm_source=chatgpt.com)",
        "other": "**Exit Five Newsletter** – newsletter yang membahas content marketing, demand generation, dan GTM. [Exit Five Newsletter](https://www.exitfive.com/newsletter?utm_source=chatgpt.com)",
        "annotation": "Ahli B2B marketing dengan pendekatan yang menekankan kekuatan storytelling, brand building, dan founder-led content marketing."
    },
    {
        "name": "Peep Laja",
        "slug": "peep-laja",
        "topic": "Messaging & Conversion",
        "linkedin": "**Messaging Is Your Biggest Growth Lever** – insight tentang mengapa messaging lebih penting daripada menambah fitur produk. [LinkedIn Profile & Posts](https://www.linkedin.com/in/peeplaja/?utm_source=chatgpt.com)",
        "other": "**CXL Blog – Messaging Frameworks** – artikel mendalam tentang positioning, messaging, dan conversion optimization. [CXL Blog](https://cxl.com/blog/?utm_source=chatgpt.com)",
        "annotation": "Fokus pada diferensiasi kompetitif dan efektivitas messaging (Copywriting/Messaging strategy) ketimbang hanya mengandalkan perbaikan fitur."
    },
    {
        "name": "Wes Bush",
        "slug": "wes-bush",
        "topic": "Product-Led Growth",
        "linkedin": "**Why Product-Led Growth Wins** – membahas activation dan onboarding sebagai pendorong pertumbuhan SaaS. [LinkedIn Profile & Posts](https://www.linkedin.com/in/wesbush/?utm_source=chatgpt.com)",
        "other": "**ProductLed Blog** – panduan tentang onboarding, activation, freemium, dan PLG. [ProductLed Blog](https://productled.com/blog/?utm_source=chatgpt.com)",
        "annotation": "Pemimpin pergerakan Product-Led Growth (PLG) yang mendikte bagaimana produk SaaS harus dirancang untuk 'menjual dirinya sendiri' tanpa intervensi sales langsung."
    },
    {
        "name": "Elena Verna",
        "slug": "elena-verna",
        "topic": "Growth Strategy",
        "linkedin": "**Growth Loops > Funnels** – menjelaskan mengapa growth loops lebih berkelanjutan daripada funnel tradisional. [LinkedIn Profile & Posts](https://www.linkedin.com/in/elenaverna/?utm_source=chatgpt.com)",
        "other": "**Elena Verna Newsletter** – artikel tentang activation, retention, dan growth strategy untuk SaaS. [Elena Verna Newsletter](https://elenaverna.com?utm_source=chatgpt.com)",
        "annotation": "Spesialis dalam merancang B2B Growth Loops, activation strategies, dan optimalisasi monetisasi PLG vs SLG model."
    },
    {
        "name": "Jason Lemkin",
        "slug": "jason-lemkin",
        "topic": "SaaS Scaling",
        "linkedin": "**Lessons Scaling SaaS** – insight tentang hiring, ARR growth, dan GTM untuk startup SaaS. [LinkedIn Profile & Posts](https://www.linkedin.com/in/jasonlemkin/?utm_source=chatgpt.com)",
        "other": "**SaaStr Blog** – salah satu referensi terbaik tentang scaling SaaS, sales, fundraising, dan customer success. [SaaStr Blog](https://www.saastr.com?utm_source=chatgpt.com)",
        "annotation": "Founder SaaStr yang merupakan perpustakaan pengetahuan terbesar bagi praktisi SaaS, khususnya seputar taktik scaling dari 0 ke $100M ARR."
    },
    {
        "name": "TK Kader",
        "slug": "tk-kader",
        "topic": "Founder GTM",
        "linkedin": "**Founder-Led GTM** – membahas bagaimana founder membangun pipeline sebelum memiliki tim sales besar. [LinkedIn Profile & Posts](https://www.linkedin.com/in/tkkader/?utm_source=chatgpt.com)",
        "other": "**Unstoppable GTM** – artikel tentang AI SaaS, outbound, dan founder-led growth. [Unstoppable GTM](https://unstoppablegtm.com?utm_source=chatgpt.com)",
        "annotation": "Memberikan kerangka kerja terstruktur untuk Founder-Led Go-To-Market strategy, terutama dalam tahap awal pencarian product-market fit (PMF)."
    },
    {
        "name": "Harry Stebbings",
        "slug": "harry-stebbings",
        "topic": "Executive Interviews",
        "linkedin": "**Key GTM Lessons from Top SaaS Founders** – rangkuman insight dari wawancara bersama founder dan investor SaaS. [LinkedIn Profile & Posts](https://www.linkedin.com/in/harrystebbings/?utm_source=chatgpt.com)",
        "other": "**20VC Newsletter** – rangkuman wawancara dengan CEO dan GTM leader dunia SaaS. [20VC Newsletter](https://www.thetwentyminutevc.com?utm_source=chatgpt.com)",
        "annotation": "Host podcast 20VC, menggali strategi GTM, fundraising, dan taktik dari ratusan pendiri serta eksekutif perusahaan SaaS tersukses."
    },
    {
        "name": "Rand Fishkin",
        "slug": "rand-fishkin",
        "topic": "SEO & Organic Growth",
        "linkedin": "**The Hook, Line & Sinker Framework for Viral Content** – membahas kerangka membuat konten yang berpotensi viral dan efektif untuk pemasaran organik. [LinkedIn Post](https://www.linkedin.com/posts/randfishkin_new-posthttpslnkdingahhvjc-on-a-framework-activity-6884031703044775936-Uj7q?utm_source=chatgpt.com)",
        "other": "**SparkToro Blog** – artikel tentang audience research, zero-click marketing, modern SEO, dan content distribution. [SparkToro Blog](https://sparktoro.com/blog?utm_source=chatgpt.com)",
        "annotation": "Ahli dalam audience research dan organik marketing, serta advokat kuat bagi 'Zero-click marketing' untuk menavigasi ekosistem modern."
    }
]

base_dir = r"c:\Users\rinip\100hires-From-Rini-Puryani\research"
linkedin_dir = os.path.join(base_dir, "linkedin-posts")
other_dir = os.path.join(base_dir, "other")

os.makedirs(linkedin_dir, exist_ok=True)
os.makedirs(other_dir, exist_ok=True)

# Generate linkedin-posts and other files
for exp in experts:
    # LinkedIn file
    with open(os.path.join(linkedin_dir, f"{exp['slug']}.md"), 'w', encoding='utf-8') as f:
        f.write(f"# LinkedIn Content: {exp['name']}\n\n")
        f.write(f"**Topik:** {exp['topic']}\n\n")
        f.write(f"## Recent Posts\n")
        f.write(f"{exp['linkedin']}\n")
        
    # Other file
    with open(os.path.join(other_dir, f"{exp['slug']}.md"), 'w', encoding='utf-8') as f:
        f.write(f"# Other Content: {exp['name']}\n\n")
        f.write(f"**Topik:** {exp['topic']}\n\n")
        f.write(f"## Websites & Newsletters\n")
        f.write(f"{exp['other']}\n")

# Generate sources.md
date_str = datetime.now().strftime("%Y-%m-%d")
with open(os.path.join(base_dir, "sources.md"), 'w', encoding='utf-8') as f:
    f.write("# Research Sources\n\n")
    f.write("Daftar 10 *expert* (LinkedIn authors, YouTube creators, podcast hosts) yang mempraktikkan langsung apa yang mereka ajarkan.\n\n")
    
    for i, exp in enumerate(experts, 1):
        f.write(f"## {i}. {exp['name']}\n")
        f.write(f"- **Topic:** {exp['topic']}\n")
        f.write(f"- **Date Collected:** {date_str}\n")
        f.write(f"- **Annotation:** {exp['annotation']}\n")
        f.write(f"- **Local Resources:**\n")
        f.write(f"  - [YouTube Transcripts](../research/youtube-transcripts/{exp['slug']}/)\n")
        f.write(f"  - [LinkedIn Posts](../research/linkedin-posts/{exp['slug']}.md)\n")
        f.write(f"  - [Other Materials](../research/other/{exp['slug']}.md)\n\n")

print("Successfully created linkedin, other, and sources files!")
