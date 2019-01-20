import pdfkit


url = 'http://localhost:8000/api/receipt/2/'
dist = 'media/PDFs/1.pdf'


pdfkit.from_url(url, dist)
