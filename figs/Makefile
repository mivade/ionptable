PDFCC = pdflatex
CONVERT = pdf2svg
PDFS = $(shell find . -name '*.tex' | sed 's/tex/pdf/')
IMGDIR = '../static/img/'
SVGS = $(shell find . -name '*.tex'  | sed 's/tex/svg/')

.PHONY:
	echo $(PDFS)
	echo $(SVGS)

all: $(PDFS) $(SVGS)

nodes.pdf: nodes.tex
	echo 'nothing to do'

nodes.png: nodes.tex
	echo 'nothing to do'

%.pdf: %.tex
	cd $(shell dirname $<); $(PDFCC) $(shell basename $<)

%.svg: %.pdf
	mkdir -p $(IMGDIR)
	$(CONVERT) $< $@; mv $@ $(IMGDIR)
