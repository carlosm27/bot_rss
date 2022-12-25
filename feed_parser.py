import feedparser

rss_link = "https://carlosmv.hashnode.dev/rss.xml"


def list_of_links(link: str):
    feed = feedparser.parse(link)

    list_links = []
    for entry in feed['entries']:
        list_links.append(entry.links[0]['href'])
    return list_links




