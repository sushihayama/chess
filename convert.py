import xml.etree.ElementTree as ET  # 'ET' として xml.etree.ElementTree モジュールをインポート
import re
from datetime import datetime

def safe_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '_', filename)

def parse_blogger_xml(xml_file):
    tree = ET.parse(xml_file)  # XMLファイルを読み込む
    root = tree.getroot()
    namespace = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in root.findall('atom:entry', namespace):
        published_element = entry.find('atom:published', namespace)
        if published_element is not None and published_element.text:
            published_text = published_element.text.strip().replace(':', '')
            published_date = datetime.strptime(published_text, "%Y-%m-%dT%H%M%S%z")
        else:
            published_date = datetime.now()

        title_element = entry.find('atom:title', namespace)
        title = title_element.text.strip() if title_element is not None and title_element.text else f"Post-{published_date.strftime('%Y-%m-%d-%H-%M-%S')}"

        content_element = entry.find('atom:content', namespace)
        content = content_element.text.strip() if content_element is not None and content_element.text else 'No content available.'

        slug = safe_filename(title.lower().replace(' ', '-'))
        file_name = f"{slug}.md"

        with open(file_name, 'w', encoding='utf-8') as md_file:
            md_file.write(f"---\n")
            md_file.write(f"title: {title}\n")
            md_file.write(f"date: {published_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
            md_file.write(f"tags: [tag1, tag2]\n")
            md_file.write(f"---\n\n")
            md_file.write(f"{content}\n")

        print(f"Converted {title}")

# エクスポートファイルのパスを指定
parse_blogger_xml('blog-01-18-2025.xml')
