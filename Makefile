all:
	cd src;	python generate.py; rsync -a build/ionptable/* ..

