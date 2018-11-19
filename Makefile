
BASE_NAME = paper
MD_FILE = $(BASE_NAME).md
BIB_FILE = $(BASE_NAME).bib
LATEX_FILE = $(BASE_NAME).tex
PDF_FILE = $(BASE_NAME).pdf
IMG_DIR = "./imgs"
CSL_FILE = "./csl/transactions-on-knowledge-discovery-from-data.csl"

FLAGS = --filter pandoc-citeproc --template=template.tex \
		--bibliography=$(BIB_FILE) --csl $(CSL_FILE) \
		-V papersize=a4paper

default: all

all:
	@if [ ! -f $(BIB_FILE) ]; then\
		make bib;\
	fi
	make latex pdf clean_tmp

latex:
	pandoc $(FLAGS) -s $(MD_FILE) -t latex -o $(LATEX_FILE)
	mkdir -p $(IMG_DIR)
	python3 process.py -m replace_ext_image -lf $(LATEX_FILE) -id $(IMG_DIR)

pdf:
	pandoc $(FLAGS) --pdf-engine=xelatex -s $(MD_FILE) -o $(PDF_FILE)

bib:
	python3 process.py -m generate_bib -mf $(MD_FILE) -bf $(BIB_FILE)

clean_tmp:
	rm -f *.log *.out *.aux

clean: clean_tmp
	rm -f $(LATEX_FILE) $(PDF_FILE)
	rm -rf ./imgs

clean_all: clean
	rm -f $(BIB_FILE)
