
# imports
import requests


# Specify global variables
base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
database = 'pubmed'

def get_pmids(query: str,
              search_format: str,
              starting_index: str,
              max_records: int):

    '''
    Description:
    Args:
        query = the query string to search for. It's a good idea to first test out the string on PubMed.
        search_format = type of output format. XML is default but json is possible.
        starting_index = the index of the first paper in the search results.
                         Usually it will be 0 but when the API is called to get the first 10K (allowable limit) records.
                         However, when using the calls in a loop, reset this number to what the index should be for the first record in the second call.
        max_records = max. number of records to obtain. The default is 20 and the max. allowable IDs returned are 10,000.
    Returns:
        a json object with details about the search and the search results

    '''

    search_suffix = (f'esearch.fcgi?db={database}'
                     f'&term={query}'
                     '&usehistory=y'
                     f'&retmode={search_format}'
                     f'&retstart={starting_index}'
                     f'&retmax={max_records}')

    search_url = base_url + search_suffix

    response = requests.get(search_url)

    if response.status_code != 200:
        print(f'Status code = {response.status_code}')

    if response.encoding != 'UTF-8':
        print(f'Encoding is {response.encoding}!')

    search_output = response.json()

    num_result = search_output['esearchresult']['count']

    print(f'The total number of records matching the search for {query} is {num_result}')

def get_paper_contents(search_output,
                       content_type: str,
                       output_format):

