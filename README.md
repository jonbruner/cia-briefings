# The CIA's daily presidential briefings, 1961-1977

The Central Intelligence Agency has released a fascinating historical record by declassifying (most of) [the daily presidential briefings](https://www.cia.gov/library/readingroom/presidents-daily-brief) that it delivered during the Kennedy, Johnson, Nixon, and Ford administrations.

The CIA has published these briefings as a collection of several thousand individual PDF files. This repo provides code for downloading these files in bulk and collating them into easier-to-handle monthly collections.

## [Download the documents from GitHub](https://github.com/jonbruner/cia-briefings/tree/master/docs/pdfs)
View and download [monthly collated PDFs right here on GitHub](https://github.com/jonbruner/cia-briefings/tree/master/docs/pdfs), or just [download the zipfile](https://github.com/jonbruner/cia-briefings/archive/master.zip) of the entire repo. You'll find the PDFs in `docs/pdfs`.

## Scrape and collate them yourself
1. Requirements
    - Python 2.7 or Python 3.x
    - [TQDM](https://pypi.python.org/pypi/tqdm) for friendly progress bars:
        ```
        pip install tqdm
        ```
2. The scripts anticipate that they'll be run in a directory with subdirectories called `documents` and `documents/originals`. If you clone this repo, they should be there, but if not you'll need to create them.

3. Run `./scrape_documents.py` to download all individual PDFs to `documents/originals`. On a reasonably fast Internet connection this will take 10-20 minutes.

4. Run `./merge_documents.py` to merge the original PDFs into monthly collections in the `documents` directory.

5. If you want to zip the collated documents into annual tarballs, run `./zip_briefings.sh`.
