import pdfkit


url = 'http://127.0.0.1:8000/api/home/'
dist = 'media/PDFs/1.pdf'


pdfkit.from_url(url, dist)
