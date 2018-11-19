
import os, sys
import scholarly
import requests
import re

def dump_file(url, save_to):
    with open(save_to, 'wb') as f:
        f.write(requests.get(url).content)


def replace_ext_image(latex_file, img_dir='./imgs/'):

    ext_img_matcher = re.compile('^\\\\includegraphics{(?P<url>https?://.*)}$')

    with open(latex_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(latex_file, 'w', encoding='utf-8') as f:
        for line in lines:
            m = ext_img_matcher.match(line.strip())
            if m:
                url = m.group('url')
                filepath = os.path.join(img_dir, os.path.basename(url))
                dump_file(url, filepath)
                f.write(f'\\includegraphics{{{filepath}}}\n')
            else:
                f.write(line)

def generate_bib(md_file, bib_file):
    footnote_matcher = re.compile('^\[\^\d+\]: (?P<footnote>.+)$')

    with open(md_file, 'r', encoding='utf-8') as in_file, \
         open(bib_file, 'w', encoding='utf-8') as out_file:

        for line in in_file:
            m = footnote_matcher.match(line.strip())
            if m:
                footnote = m.group('footnote')
                try:
                    result = next(scholarly.search_pubs_query(footnote))
                except Exception as e:
                    continue
                content = requests.get(result.url_scholarbib).content.decode('utf-8')
                out_file.write(content)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--method", required=True, help="choose which method to use")
    ap.add_argument("-mf", "--md_file", required=False)
    ap.add_argument("-lf", "--latex_file", required=False)
    ap.add_argument("-bf", "--bib_file", required=False)
    ap.add_argument("-id", "--img_dir", required=False)
    args = vars(ap.parse_args())

    if args['method'] == 'replace_ext_image':
        replace_ext_image(args['latex_file'], args['img_dir'])
    elif args['method'] == 'generate_bib':
        generate_bib(args['md_file'], args['bib_file'])
    else:
        raise Exception("No such method.")

