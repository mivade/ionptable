PDFCC = pdflatex
CONVERT = convert -background white -flatten -density 180 
PDFS = $(shell find . -name '*.tex' | sed 's/tex/pdf/')
PNGS = $(shell find . -name '*.tex'  | sed 's/tex/png/')

.PHONY:
	echo $(PDFS)
	echo $(PNGS)

all: $(PDFS) $(PNGS)

nodes.pdf: nodes.tex
	echo 'nothing to do'

nodes.png: nodes.tex
	echo 'nothing to do'

%.pdf: %.tex
	cd $(shell dirname $<); $(PDFCC) $(shell basename $<)

%.png: %.pdf
	mkdir -p ../img
	$(CONVERT) $< $@; cp $@ ../img/
