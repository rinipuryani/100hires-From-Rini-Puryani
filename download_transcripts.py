import os
import urllib.request
import urllib.parse
import re
import json
from youtube_transcript_api import YouTubeTranscriptApi

experts_data = {
    "april-dunford": ["April Dunford Product Positioning", "April Dunford Obviously Awesome", "April Dunford Sales Pitch"],
    "chris-walker": ["Chris Walker Demand Generation vs Lead Generation", "Chris Walker Dark Social", "Chris Walker Revenue Marketing"],
    "dave-gerhardt": ["Dave Gerhardt Founder Led Content", "Dave Gerhardt B2B Marketing Playbook", "Dave Gerhardt Personal Brand"],
    "peep-laja": ["Peep Laja Messaging That Converts", "Peep Laja Category Design", "Peep Laja How Brands Win"],
    "wes-bush": ["Wes Bush Product Led Growth Masterclass", "Wes Bush Freemium Strategy", "Wes Bush User Onboarding"],
    "elena-verna": ["Elena Verna Growth Loops", "Elena Verna Retention", "Elena Verna Activation"],
    "jason-lemkin": ["SaaStr Scaling from 1M to 100M ARR", "Jason Lemkin Hiring GTM"],
    "tk-kader": ["TK Kader Founder Led GTM", "TK Kader AI SaaS", "TK Kader Demand Generation"],
    "harry-stebbings": ["20Growth Harry Stebbings", "Harry Stebbings Elena Verna", "Harry Stebbings Kyle Poyar", "Harry Stebbings Claire Hughes Johnson"],
    "rand-fishkin": ["Rand Fishkin Zero Click Marketing", "Rand Fishkin Audience Research", "Rand Fishkin Modern SEO"]
}

base_dir = os.path.join(os.getcwd(), "research", "youtube-transcripts")

def get_first_video_id(query):
    try:
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            return video_ids[0]
    except Exception as e:
        print(f"Error searching for {query}: {e}")
    return None

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h > 0:
        return f"[{h:02d}:{m:02d}:{s:02d}]"
    else:
        return f"[{m:02d}:{s:02d}]"

for expert, queries in experts_data.items():
    expert_dir = os.path.join(base_dir, expert)
    os.makedirs(expert_dir, exist_ok=True)
    
    for query in queries:
        print(f"Processing: {query}")
        vid_id = get_first_video_id(query)
        if not vid_id:
            print(f"  -> No video found.")
            continue
            
        print(f"  -> Found Video ID: {vid_id}")
        
        try:
            transcript = YouTubeTranscriptApi().fetch(vid_id)
            safe_query = query.replace(' ', '-').lower()
            filename = f"{safe_query}.md"
            filepath = os.path.join(expert_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# Transcript for: {query}\n")
                f.write(f"Video ID: {vid_id}\n")
                f.write(f"Link: https://www.youtube.com/watch?v={vid_id}\n\n")
                
                for entry in transcript:
                    ts = format_timestamp(entry.start)
                    text = entry.text.replace('\n', ' ')
                    f.write(f"{ts} {text}\n")
                    
            print(f"  -> Saved to {filepath}")
        except Exception as e:
            print(f"  -> Error extracting transcript: {e}")

print("Done processing all transcripts!")
