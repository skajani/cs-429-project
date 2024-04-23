# CS-429-Project: Creating an Information Retrieval System
## Abstract:
The goal of this project is to create an information retrieval system that can be used to search for documents in a collection of documents. The project involved the development of a web crawler, indexer, and processor to be able to efficently search for documents and view information about these documents. The web crawler, built primarily using Scrapy, allowed me to go through the web pages, extract data from the sites, process it, and store it into a JSON file and save the crawled documents to a folder. The indexer then took this data to create and inverted index using TF-IDF score representation and cosine similarity metrics. Finally, a query handler was created in order to process and handle any queries from the user side. Some next steps that can be incorporated include creating a more sophisticated preprocessing technique, optimizing the algorithims for better efficency, automated actions, and developing a front-end for the end user to be able to easily enter their queries and get information about the documents.
## Overview:
The solution developed in this project is a web crawler, indexer, and query handler that can be used for document retrieval and similarity analysis. Furthermore, utilizing the following 3-stage technique, a information retrieval system was developed:
1. Scrapy Crawler (To Download Web Documents in html format)

2. Scikit-Learn Indexer (To Create an Inverted Index)

3. Processor (To Process Queries and Return Results)
## Design

### Crawler
The crawler was built using the Scrapy framework. The crawler was designed to be able to crawl through the web and download the html documents. It begins at the seed URL, recursivley following links and extracting data that can be used by the Indexer. This crawler makes use of the BeautifulSoup package to parse the html documents and extract the necessary data. The crawler outputs a output.json file along with a folder called 'crawled_docs' which contains all the documents that were downloaded.

### Indexer
The indexer was built with SciKit-Learn in order to process the crawled content and extract important information to build an inverted index. In the indexer, preprocessing was used in order to remove unneeded elements like punctuation, HTML tags, and stop words. These steps help to create an efficent and functional indexer. The indexer then uses the TF-IDF score representation to create a vector representation of the documents. The cosine similarity metrics were then used to calculate the similarity between the query and the documents. We can see output of this in the .pkl files.

### Processor
The processor was built using the Flask framework. The processor was designed to be able to process queries and return results. It uses the TF-IDF and cosines similarity to develop scores and ranking for the documents found in crawled_docs. Through this process, we are able to return the top-K documents that are related to the user's query.

## Architecture
The software architecture comprises three key components: the crawler, indexer, and processor. The crawler systematically traverses web pages, employing Scrapy for efficient crawling and BeautifulSoup for HTML parsing. The indexer processes crawled content, extracting pertinent information and constructing an inverted index for efficent querying. Lastly, the processor integrates indexed data with TF-IDF vectorization and similarity calculations between queries and documents through scikit-learn.

## Operation
To operate this program, the user will begin by going into the crawler and replacing the seed_url variable with the url they want crawled. When sending this crawl request, the user will also send the max_pages and max_depth they would like for this crawler to run, after this the crawler will run and create an output.json file and download the HTML docs into a folder called crawled_docs.

After running the crawler, the user will go to the indexer, where the indexer will be run in order to create a inverted index whilst considering TF-IDF scoring and cosine similarity. Finally, the user will run the processor and enter a query in the test.http file to send a PUT request to the running query handler. The query handler will then process the query and return the top-K documents that are related to the user's query.

## Conclusion
The project was successful in effectivley using Scrapy to crawl and download HTTP documents. The project was also successful in creating an inverted index using TF-IDF scoring and cosine similarity metrics and processing them as a result for the user in Top-K format. Some issues faced were ensuring the accuracy of similarity scores and deciding the correct preprocessing actions to ensure a accurate score that would be helpful and impactful for the end user.

## Data Sources
The data sources used in this project were the following:

https://en.wikipedia.org specifically https://en.wikipedia.org/wiki/Michael_Jordan

The other documents created from the crawler are located in the crawled_docs folder that are related to the seed_url.

## Test Cases
The test cases for this project are located in the test.http file. This is where PUT requests are sent to the query handler and where user queries can be inputted.

## Source Code

Github & Github Desktop was utilized as my version control and repository management tool.
Microsoft Visual Studio Code was utilized as my IDE.
In my code, Python 3.11 was utilized to run the program along with the following packages:

- Scrapy
- beautifulsoup
- Scikit-Learn
- Pickle
- numpy
- Flask

## Bibliography
“Beautiful Soup Documentation.” Beautiful Soup Documentation. Accessed April 2024. https://tedboy.github.io/bs4_doc/.
“Buildwithpython.” YouTube. Accessed April 2024. https://www.youtube.com/@buildwithpython.
Chat OpenAI. Accessed April 2024. https://chat.openai.com.
“Documentation of Scikit-Learn 0.21.3.” learn. Accessed April 2024. https://scikit-learn.org/0.21/documentation.html.
GeeksforGeeks. “Understanding Python Pickling with Example.” GeeksforGeeks, October 27, 2023. https://www.geeksforgeeks.org/understanding-python-pickling-example/.
“Python 3.11.8 Documentation.” 3.11.8 Documentation. Accessed April 2024. https://docs.python.org/3.11/.
“Quickstart.” Quickstart - Flask Documentation (2.3.x). Accessed April 2024. https://flask-docs.readthedocs.io/en/latest/quickstart/.
“Scrapy 2.11 Documentation.” Scrapy 2.11 documentation - Scrapy 2.11.1 documentation, April 11, 2024. https://docs.scrapy.org/en/latest/.
“Welcome to Flask.” Welcome to Flask - Flask Documentation (3.0.x). Accessed April 2024. https://flask.palletsprojects.com/en/3.0.x/.
