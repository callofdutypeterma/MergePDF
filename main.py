from PyPDF2 import PdfFileMerger

def mergePDF(path, num):
    merger = PdfFileMerger()
    for cpage in range(1, num + 1):
        merger.append(open(path + '/P%d.pdf' % cpage, 'rb'))

    merger.write(path + '/Merged.pdf')
    merger.close()

mergePDF('C:/Users/Peter/Desktop/delete/chinaimg', 165)