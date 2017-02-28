__author__ = 'luhaoliang'

import argparse

def cmdLineParser():
    parser = argparse.ArgumentParser(description='Marimo powered by S1mba',
                                     usage='python Marimo.py')
    parser.add_argument("-s","--script",dest="script_name",type=str)
    parser.add_argument("-tS",dest="target_single",type=str)
    parser.add_argument("-tF",dest="target_file",type=str)
    parser.add_argument("-nZ","--zoomeye",dest="zoomeye_dork",type=str,help='ZoomEye dork (e.g. "solr country:cn")')
    parser.add_argument('--search-type', metavar='TYPE', dest="search_type",type=str,default='host',help="[ZoomEye] search type used in ZoomEye API, web or host (default:host)")
    parser.add_argument('--limit', metavar='NUM', dest="api_limit", type=int, default=10)
    parser.add_argument("-A",dest="all_script",default=False,action='store_true')
    parser.add_argument("-th","--thread",dest="thread_num",type=int,default=5)
    args = parser.parse_args()
    return args