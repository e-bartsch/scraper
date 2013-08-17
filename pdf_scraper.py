import pyPdf
import sys

f = open(sys.argv[1],'rb')

pdf = pyPdf.PdfFileReader(f)
pgs = pdf.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

emails = []

for pg in range(pgs):

    p = pdf.getPage(pg)
    o = p.getObject()

    if o.has_key(key):
        ann = o[key]
        for a in ann:
            u = a.getObject()
            if u[ank].has_key(uri) and 'mailto:' in u[ank][uri]:
                email = u[ank][uri].replace('mailto:', '')
                if email not in emails:
                	emails.append(email)

for email in emails:
	print email

f.close()