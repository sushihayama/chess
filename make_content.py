import os
from datetime import datetime

def generate_unique_slug(title, content_dir):
    # 初期のslugを生成
    slug = title.lower().replace(' ', '-')
    original_slug = slug  # オリジナルのslugを保存しておく
    
    # 重複している場合は、番号を付けてslugを再生成
    count = 1
    while os.path.exists(os.path.join(content_dir, f"{slug}.md")):
        slug = f"{original_slug}-{count}"
        count += 1
    
    return slug

def create_new_post(title, category, tags, content_dir="content"):
    # フロントマターを生成
    date = datetime.now().strftime('%Y-%m-%d')
    slug = generate_unique_slug(title, content_dir)  # 重複しないslugを生成
    summary = f"Summary of {title}"

    post_content = f"""Title: {title}
Date: {date}
Category: {category}
Tags: {tags}
Slug: {slug}
Summary: {summary}

# {title}

Content goes here.
"""

    # 新しいファイルを作成
    file_name = os.path.join(content_dir, f"{slug}.md")
    with open(file_name, 'w') as f:
        f.write(post_content)

    print(f"New post created: {file_name}")

# 使用例
create_new_post("new", "chess", "pelican, auto")
