import os
from datetime import datetime

def add_front_matter_to_md(directory):
    directory = os.path.expanduser(directory)  # ホームディレクトリのショートカットを展開
    files = [f for f in os.listdir(directory) if f.endswith(".md")]
    files.sort()  # ファイル名でソートして一貫性を保持

    for i, filename in enumerate(files, start=1):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r+', encoding='utf-8') as file:
            content = file.read()
            title = filename.replace(".md", "").replace("-", " ").title()
            slug = f"post-{i}"  # 通し番号をslugとして使用
            date = datetime.now().strftime("%Y-%m-%d")
            front_matter = f"---\ntitle: {title}\ndate: {date}\nslug: {slug}\ntags: [tag1, tag2]\nsummary: 'Insert summary here'\n---\n\n"
            file.seek(0, 0)
            file.write(front_matter + content)
            print(f"Added front matter to {filename} with slug {slug}")

# 使用例: ホームディレクトリ下の 'markdown' フォルダを指定
directory_path = '~/content'
add_front_matter_to_md(directory_path)
