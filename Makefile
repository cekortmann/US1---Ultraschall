all: build/US1.pdf

build/US1.pdf: US1.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build US1.tex
	lualatex  --output-directory=build US1.tex
	biber build/US1.bcf
	lualatex  --output-directory=build US1.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
