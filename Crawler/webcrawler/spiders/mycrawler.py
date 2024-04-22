import scrapy
from scrapy.crawler import CrawlerProcess
import os
from bs4 import BeautifulSoup

class MyCrawler(scrapy.Spider):
    name = "mycrawler"
    custom_settings = {
        'CONCURRENT_REQUESTS': 4,
    }

    def __init__(self, seed_url=None, max_pages=None, max_depth=None, *args, **kwargs):
        super(MyCrawler, self).__init__(*args, **kwargs)
        self.start_urls = [seed_url] if seed_url else []
        self.max_pages = int(max_pages) if max_pages else None
        self.max_depth = int(max_depth) if max_depth else None
        self.visited_pages = set()

    def parse(self, response): #parse with beautifulsoup
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.get_text() if soup.title else ""
        
        text_content = soup.get_text()

        url = response.url

        yield {
            'title': title,
            'url': url,
            'text_content': text_content
        }

        doc_name = response.url.split("/")[-1].split('#')[0]  # Remove everything after '#' in the URL
        if not doc_name:
            return  # skip save if doc_name Does Not Exist (DNE)
        filename = f'crawled_docs/{doc_name}.html'
        os.makedirs(os.path.dirname(filename), exist_ok=True)  # Create directory if it doesn't exist
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Add URL
        self.visited_pages.add(response.url)

        if self.max_depth is None or response.meta.get('depth', 0) < self.max_depth:
            for link in response.css('a::attr(href)').getall():
                # Exclude external links
                if response.urljoin(link).startswith(response.url) and link not in self.visited_pages:
                    yield response.follow(link, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1})
        # Max page check
        if self.max_pages is not None and len(self.visited_pages) >= self.max_pages:
            self.logger.info('Reached maximum pages limit. Crawling stopped.')
            return

# Start crawling process
process = CrawlerProcess(settings={
    "FEEDS": {
        "output.json": {"format": "json"},
    },
    "LOG_ENABLED": False,
})

process.crawl(MyCrawler, seed_url='https://en.wikipedia.org/wiki/Michael_Jordan', max_pages=10, max_depth=3)
process.start()