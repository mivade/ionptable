PDFCC = pdflatex
CONVERT = convert
PDFS = $(shell find . -name '*.tex' | sed 's/tex/pdf/')

all: $(PDFS)

%.pdf: %.tex
	cd $(shell dirname $<); $(PDFCC) $(shell basename $<)
