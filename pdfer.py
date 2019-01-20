import pdfkit
import hashlib


url = 'http://localhost:8000/api/receipt/2/'


def generatePDF(url):
    name = hashlib.sha224(url.encode()).hexdigest()
    dist = 'media/PDFs/' + name + '.pdf'

    options = {
        'page-size': 'legal',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None
    }

    return pdfkit.from_url(url, dist, options)


if __name__ == "__main__":
    generatePDF(url)
