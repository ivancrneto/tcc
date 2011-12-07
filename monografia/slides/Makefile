SOURCEDOCUMENT=aiaf
PDFVIEWER=evince


#######################################

all: $(SOURCEDOCUMENT).pdf

view: $(SOURCEDOCUMENT).pdf
	$(PDFVIEWER) $(SOURCEDOCUMENT).pdf &

$(SOURCEDOCUMENT).pdf: $(SOURCEDOCUMENT).tex $(SOURCEDOCUMENT).bib
	pdflatex $< && \
	bibtex $(SOURCEDOCUMENT) && \
	pdflatex $< && \
	pdflatex $< || \
	$(RM) $@

clean:
	$(RM) *.aux *.bbl *.blg *.lof *.lot *.log $(SOURCEDOCUMENT).pdf *~ \
	*.toc *.ilg *.sigla *.siglax *.symbols *.symbolsx
