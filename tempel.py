#!/usr/bin/python

import argparse
import clipboard
import requests

__version__ = '0.0.4'

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="tempel your source code to http://tempel.blankon.in",
        epilog=None
    )
    #required args
    parser.add_argument('-l', '--language', action='store', required=True, 
                    help='set language of source code; bash c cpp css diff html html+django ini java lua make perl php python rst ruby sql text xml yaml')

    group = parser.add_mutually_exclusive_group()
    #optional args
    group.add_argument('-t', '--text', help='from text', default=False)
    group.add_argument('-c', '--clipboard', help='from clipboard', default=True)
    group.add_argument('-f', '--filename', help='from file', default=False)    

    parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    if args.text:
        content = args.text
    elif args.filename:
        content = from_file(args.filename)
    else:
        content = clipboard.paste()
    
    tempel = 'http://tempel.blankon.in'
    values = {
      'language' : args.language,
      'content' : content
    }
    response = requests.request("POST", tempel, data=values)
    print 'URL: ', response.url

def from_file(berkas):
    """"""
    try:
        f = open(berkas, mode='r')
        return f.read()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
   #main(sys.argv[1:])
   get_args()
