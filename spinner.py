# import re
import os
import sys
import spin2 as sp
from synonyms import load
import json

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            print ("- > File name: "+os.path.join(self.dirname, fname))
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
    # def funk(*args):
    #     print()

#---------------------------------end of spinner class ---------------------------------#

if __name__ == '__main__':
    result      = []
    inp         = sys.argv[1]
    param       = sys.argv[2]
    # pers        = 0.7
    filein      = os.path.join('input', inp)
    fileout     = os.path.join('output', inp) 
    lib         = load(open('syn.txt'))
    s           = sp.Magic(lib)

    for data in json.loads( open( filein ).read() ):
        print(data)
        tmp = data
        for param in ( sys.argv[2:] ):
            tmp[param] = s(data[param])
        result += [tmp]

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    with open(fileout, 'w') as outfile:
        str_ = json.dumps(result, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
