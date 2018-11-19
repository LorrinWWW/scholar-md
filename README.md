# Markdown to PDF

## Requirements

- pandoc
- texlive
- python3: scholarly

## Quickstart

1. copy your markdown file into the folder and rename it to "paper.md"
2. run

    ```bash
    $ make
    ```

3. open paper.pdf

note if there are something wrong with the looks, it is possible to modify paper.tex and then generate the correct pdf file.

## Functionality

- Convert md to latex file

    ```bash
    $ make latex
    ```

- Covert md to pdf file

    ```bash
    $ make pdf
    ```

- Generate .bib file according to footnotes of the md file

    ```bash
    $ make bib
    ```

    Note this will only generate the .bib file, and won't modify the original md file nor add into the pdf file.

    Please modify .tex file by hand.

## Still in working
