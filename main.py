import re

def extract_youtube_links(text):
    url_pattern = r'https?://[^\s"\'<>()\[\],]+'
    urls = re.findall(url_pattern, text)

    youtube_domains = (
        'youtube.com', 'www.youtube.com', 'm.youtube.com',
        'music.youtube.com', 'youtu.be', 'www.youtu.be'
    )
    yt_links = []
    for url in urls:
        url = url.rstrip('.,;:!?\'")]}')
        host_match = re.match(r'https?://([^/]+)', url)
        if host_match and host_match.group(1).lower() in youtube_domains:
            yt_links.append(url)

    seen = set()
    unique_links = []
    for link in yt_links:
        if link not in seen:
            seen.add(link)
            unique_links.append(link)

    return unique_links


if __name__ == "__main__":
    print("Paste your garbage paragraph below.")
    print("When done, type a line containing only: END")
    print("-" * 50)

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)

    garbage = "\n".join(lines)
    links = extract_youtube_links(garbage)

    print()
    for link in links:
        print(link)
    print()
    print(f"Number found: {len(links)}")