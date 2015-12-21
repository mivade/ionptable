PDFCC = -xelatex
CONVERT = pdf2svg
IMGDIR = '../static/img/'
TEXS = $(wildcard *.tex)
PDFS = $(patsubst %.tex,%.pdf,$(TEXS))
SVGS = $(patsubst %.pdf,%.svg,$(PDFS))

all: $(PDFS) $(SVGS) levels.sty

%.pdf: %.tex
	latexmk -xelatex $<

%.svg: %.pdf
	mkdir -p $(IMGDIR)
	$(CONVERT) $< $@; mv $@ $(IMGDIR)
