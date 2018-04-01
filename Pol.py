# -*- coding: utf-8 -*-

from unicodedata import normalize
import optparse
import codecs

import locale
import re
import math
from math import sqrt, floor
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


__version__ = '1.1'


def generate_array(key=u''):
    key = key.decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    key_word = raw_input("Введите ключ \n").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    ALPH = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩШЫЬЪЭЮЯ1234567890'

    key_word_raw = key_word.upper()
    key_word = ''
    for sym in key_word_raw:
        if sym.upper() in ALPH:
            key_word += sym

    print key_word

    alphabet_1 = (key_word+ALPH)
    alphabet=u''
    for i in alphabet_1:
        if i not in alphabet and i!=u' ': alphabet+=i
    print(alphabet)
    print 'длина алфавита:'
    print(len(alphabet))





    if len(alphabet) == 31 or 37 or 41 or 43 or 53 or 47 or 59 or 61 or 67 or 71 or 73 or 79 :
        alphabet = alphabet +'$'
    array = []
    _tmp = []
    key = re.sub(r'[^а-яА-Я]+', '', key)
    key = key.upper()
    lenalp=len(alphabet)
    sqrtlen=int(sqrt(lenalp))
    print sqrtlen


    i = 2
    for i in range(1,sqrtlen+1,1):
        delit = lenalp//i
        if i*delit==lenalp:
 
            ran2 = i
 
            ran1 = delit

    




    if key:
        for k in key:
            alphabet = alphabet.replace(k, '')

        alphabet = key + alphabet

    for y in range(ran1):
        for x in range(ran2):
            _tmp.append(alphabet[0 + ran2 * y + x])
        array.append(_tmp)
        _tmp = []

    return array

def display_array(array):


    row_labels = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83']
    print '     1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10'
    for row_label, row in zip(row_labels, array):
        print '%s %s  ' % (row_label, ' '.join('%03s' % i for i in row))


def format_cipher(data):

            codesym = "".join(data[i:i+3] for i in range(0, len(data), 3))
            
            words = codesym.split()
            new_text = ''
            for w in words:
                if len(w) == 2:
                    new_text +='0'+w+' '

                else:
                    new_text+=w+' '
            
            cip_f = open('cipher.txt', 'w')
            cip_f.write(new_text)
            return new_text


def encode(words, array):


    cipher = ''
#  words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents

    for word in words.upper():
        for i in range(len(array)):
            if word in array[i]:
                oy = str(i + 1)
                ox = str((array[i].index(word) + 1))
                cipher += oy + ox+' '


    return cipher


def decode(numbers, array):



    numbers = re.sub(r'[\D]+[S]', '', numbers)
    sym_word = ''.join(numbers)
    sym_word = sym_word.split()

    sym_word_new = ''
    for w in sym_word:
        if len(w)==3:
            sym_word_new += w
        else:
            sym_word_new+= ''

    text = ''

    for number in range(0, len(sym_word_new), 3):
        try:
            oy = int(sym_word_new[number:number+2]) -1
            ox = int(sym_word_new[number + 2]) - 1
        
            text += array[oy][ox]
        except IndexError:
            pass
        continue
    dec_f = open('decode_message.txt', 'w')
    dec_f.write(text)
    return text


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__,
                                   usage='Usage: %prog [options] [args]')
    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-k', dest='key', action='store', default='', type='string',
                      help='klucz transformacji szachownicy')


    (options, args) = parser.parse_args()

    print ''
    print 'Шифрование. Квадрат Полибия'
    print ''
    

    if options.decrypt:
        print 'Вы находитесь в режиме дешифрования.\n'
    else:
        print 'Вы находитесь в режиме шифрования.\n'

    array = generate_array(key=options.key)



    print 'Полученная матрица:'
    display_array(array)

    while 1:
            print ''
            try:
                text = raw_input(' Введите текст:\n\n').decode(sys.stdin.encoding or locale.getpreferredencoding(True))

                if options.decrypt:
                    print u' Ответ:\n\n   ' + decode(text, array)
                else:
                    print u' Ответ:\n\n  '  + format_cipher(encode(text, array))
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)
