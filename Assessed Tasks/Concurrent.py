import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import newspaper
from newspaper import Article
import urllib.request



def load_url(url, timeout):
    ''''
    Function to load all the URLs as they are given from the list
    '''
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def get_headlines():
    ''''
    Will concurrenctly get the results from the URLS as well as set threads to do so and print them as they come in one by one
    '''
    URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]


    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: #will set 5 threads to use for the process
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLs} #will set the array and load all the URLS list which contains the links to the articles into the list
        for future in concurrent.futures.as_completed(future_to_url): #will iterate until all URLS have been loaded and printed
            url = future_to_url[future] #set an array for URLS to be printed from
            try:
                art = future.result() #will set the results are a variable
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc)) #will check for an exception and print if there is one
            else:
                result = newspaper.build(url, memoize_articles=False) #will set the results with newspaper module and build them based on the URLS
                print('\n''The headlines from %s are' % url, '\n')# will print the name of articles and its URL
                for i in range(1,6): #will loop through to print each article
                    art = result.articles[i] #will change as it goes through each article setting the result to a different article
                    art.download() #will download results from webpages
                    art.parse() #will parse the results
                    print(art.title) #will print the results of the URLS and articles

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=2)/2             
    print(elapsed_time) 
