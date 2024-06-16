all: thesis.pdf abstract-cs.pdf abstract-en.pdf poster/poster.pdf

%.pdf: force
	latexmk $*.tex -pdf

clean:
	latexmk -C
	rm *.xmpdata *.xmpi *.bbl thesis.run.xml

#	rm -rf aux
	#rm -f thesis.pdf abstract.pdf abstract-cs.pdf abstract-en.pdf

.PHONY: force
