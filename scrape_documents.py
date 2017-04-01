#!/usr/bin/env python

import urllib.request, re, os
from tqdm import tqdm
from multiprocessing import Pool

document_path = "documents/originals"
document_path = os.path.join(os.path.dirname(__file__), document_path)

url_search = re.compile("(https:[a-zA-Z0-9\.\/_]+DOC_[0-9]+.pdf)")
filename_search = re.compile("(DOC_[0-9]+.pdf)")

def download_document(url):
    this_filename = filename_search.findall(url)[0]
    urllib.request.urlretrieve(url, "%s/%s" % (document_path, this_filename))

# Kennedy and Johnson administrations are here:
# https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1961-1969
# with 125 pages in the index

# Nixon and Ford administrations are here:
# https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1969-1977
# with 126 pages in the index

# ?page= indexing begins with 0 on the CIA's site

collections = [('https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1961-1969', 126, 'Kennedy-Johnson'),
        ('https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1969-1977', 127, 'Nixon-Ford')]

for collection in collections:
    print("Starting", collection[2])
    pages = tqdm(range(0, collection[1]), desc="Pages")
    for pagenum in pages:
        index_page = urllib.request.urlopen("%s?page=%d" % (collection[0], pagenum)) \
            .read().decode('utf-8')

        document_urls = url_search.findall(index_page)

        # There are typically 20 results on each index page, so we spin up
        # 20 simultaneous download threads
        with Pool(20) as p:
            results = p.map(download_document, document_urls)
    print("Finished", collection[2])
