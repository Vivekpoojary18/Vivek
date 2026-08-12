import sys, re, json

content = sys.stdin.read()

match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);</script>', content)
if match:
    data = json.loads(match.group(1))
    questions = data[1][1]
    for q in questions:
        title = q[1]
        entry_id = q[4][0][0]
        print(f"TITLE: {title} | ENTRY_ID: entry.{entry_id}")
else:
    print("Entry IDs found:", set(re.findall(r'entry\.\d+', content)))
    print("Matches:", re.findall(r'\[\[(\d{8,11}),"([^"]+)"', content))
