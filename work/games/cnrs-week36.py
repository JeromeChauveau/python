#!/usr/bin/python
# coding: utf8

from docopt import docopt

'''

Usage:
  cnrs-week36.py --to_find=NumberToFind --size=SizeOfNumbers
  
http://images.math.cnrs.fr/Septembre-2017-2e-defi.html*
Combien y a-t-il de nombres à dix chiffres tous différents abcdefghij tels que a+j=b+i=c+h=d+g=e+f=9 ?


Algo:

Identifier le nombre n de couples de chiffres dont la somme est neuf, sachant que l'ordre compte (90 et 09 par exemple sont valables)
Note : cela peut être élargi à la recherche du nombre de n-uplet dont la somme vaut m
Identifier le nombre de façons de choisir 4 couples parmi les n trouvés, sachant que le même couple peut être choisi plusieurs fois
Note : il s'agit du nombre de tirages avec remise. 
Attention néanmoins: 
 - l'ordre a son importance (9900 et 0099 sont différents)
 - il ne faut pas compte les doublons
'''

def main(numberToFind, sizeOfNumbers):
    print('todo')

if __name__ == "__main__":
    arguments = docopt(__doc__, version='cnrs-week36 1.0')
    main(arguments['--to_find'], arguments['--size'])
