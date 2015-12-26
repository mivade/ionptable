all: images
	cd src;	python generate.py; rsync -a build/ionptable/* ..

images:
	cd src/figs; make
