PDFCC = pdflatex
CONVERT = convert -background white -flatten -density 180 
PDFS = $(shell find . -name '*.tex' | sed 's/tex/pdf/')
PNGS = $(shell find . -name '*.tex' | sed 's/tex/png/')

all: $(PDFS) $(PNGS)

%.pdf: %.tex
	cd $(shell dirname $<); $(PDFCC) $(shell basename $<)

%.png: %.pdf
	mkdir -p img
	$(CONVERT) $< $@; mv $@ ../img/

