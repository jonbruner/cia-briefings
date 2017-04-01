#!/usr/bin/env python

from PyPDF2 import PdfFileMerger, PdfFileReader
import os, re, datetime
from tqdm import tqdm

def save_merged(merger, current_month, current_month_datetime):
    outfile = '%s/Briefings_%s.pdf' % (out_document_path, current_month)
    this_title = "President's Briefings %s" % current_month_datetime.strftime("%B %Y")
    merger.addMetadata({'/Title':this_title,
                        '/Author':'Central Intelligence Agency',
                        '/Producer':'Jon Bruner'})
    merger.write(outfile)

document_path = "documents/originals"
document_path = os.path.join(os.path.dirname(__file__), document_path)
out_document_path = os.path.join(os.path.dirname(__file__), "documents")

document_list = os.listdir(document_path)

date_regex = re.compile("([0-9]+ [A-Z]+ [0-9]{4})")

# Get dates associated with each file,
# and load path, document title, datetime object,
# and year-month string into a list of tuples
documents = []
for d in document_list:
    this_file = "%s/%s" % (document_path, d)
    this_title = PdfFileReader(this_file).getDocumentInfo().title
    try:
        this_date_string = date_regex.findall(this_title)[0].title()
        this_date = datetime.datetime.strptime(this_date_string, "%d %B %Y")
        this_month = this_date.strftime("%Y-%m")
        documents.append((this_file, this_title, this_date, this_month))
    except:
        # print(this_title)
        pass

# Sort all of the documents by date
documents = sorted(documents, key=lambda tup:tup[2])

merger = PdfFileMerger()
current_month = documents[0][3]
current_month_datetime = documents[0][2]
for d in tqdm(documents):
    # print(d)
    if d[3] != current_month:
        # Package and save file, and reset
        save_merged(merger, current_month, current_month_datetime)
        merger.close()
        merger = PdfFileMerger()
        current_month = d[3]
        current_month_datetime = d[2]

    try:
        this_file = d[0]
        merger.append(this_file)
    except:
        print(d)

# Save final month
save_merged(merger, current_month, current_month_datetime)
