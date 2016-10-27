#!/usr/bin/python

import argparse
import requests
import pyperclip

__version__ = '0.0.4'

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="tempel your source code to http://tempel.blankon.in",
        epilog=None
    )
    #required args
    parser.add_argument('language', action='store', nargs='?',
                    help='language of source code; bash c cpp css diff html html+django ini java lua make perl php python rst ruby sql text xml yaml',
                    default='text', choices=['bash', 'c', 'cpp', 'css', 'diff', 'html', 'html+django', 'ini', 'java', 'lua', 'make', 'perl', 'php', 'python',
                    'rst', 'ruby', 'sql', 'text', 'xml', 'yaml'])

    group = parser.add_mutually_exclusive_group()
    #optional args
    group.add_argument('-t', '--text', help='from text', default=False)
    group.add_argument('-f', '--filename', help='from file', default=False)    

    parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    if args.language in ['bash', 'c', 'cpp', 'css', 'diff', 'html', 'html+django',
                         'ini', 'java', 'lua', 'make', 'perl', 'php', 'python',
                         'rst', 'ruby', 'sql', 'text', 'xml', 'yaml'
                        ]:
        if args.text:
            content = args.text
        elif args.filename:
            content = from_file(args.filename)
        else:
            content = pyperclip.paste()

        tempel = 'http://tempel.blankon.in'
        values = {
        'language' : args.language,
        'content' : content
        }
        print 'URL: ', post(tempel, values)
    else:
        print('Please use specified language in help')

def from_file(berkas):
    """"""
    try:
        f = open(berkas, mode='r')
        return f.read()
    except ValueError as e:
        print(e)

def post(url, values):
    try:
        response = requests.request('POST', url, data=values)
        return response.url
    except ValueError as e:
        print(e)

if __name__ == "__main__":
   get_args()
