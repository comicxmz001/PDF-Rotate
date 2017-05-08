import PyPDF2
import os
import sys

class pdfRotater(object):
	"""
		Inspired by John D. Cook
		http://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with-python/
	"""
	def __init__(self):
		pass

	def rotate(self, name):
		baseName = os.path.basename(name)
		fileDir = os.path.dirname(name)
		pdfAbsPath = os.path.join(fileDir, baseName)

		if not os.path.isfile(pdfAbsPath):
			print "Invalid file name: {}".format(name)
			return False

		pdf = open(pdfAbsPath, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdf)
		pdfWriter = PyPDF2.PdfFileWriter()

		count = 1
		pageCount = pdfReader.numPages
		for pagenum in xrange(pageCount):
			page = pdfReader.getPage(pagenum)
			# rotate
			print "Processing page {} -- {}%.".format(str(count), str(100*count/pageCount))
			page.rotateClockwise(180)
			pdfWriter.addPage(page)
			count += 1

		print "Generating PDF..."
		newPDFName = os.path.join(fileDir,baseName[:-4]+'_rotated.pdf')
		newPDF = open(newPDFName,'wb')
		pdfWriter.write(newPDF)
		newPDF.close()
		print "\"{}\" is generated.".format(newPDFName)
		pdf.close()

		return True


file = 'xxx.pdf'
# print os.path.split(file)
pdfRotater().rotate(file)
