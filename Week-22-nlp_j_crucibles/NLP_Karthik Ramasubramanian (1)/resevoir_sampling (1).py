import sys
import random
import codecs
 
#if len(sys.argv) == 3:
#    input = open(sys.argv[2],'r')
#elif len(sys.argv) == 2:
#    input = sys.stdin;
#else:
#    sys.exit("Usage:  python samplen.py <lines> <?file>")
 
#N = int(sys.argv[1]);
reviews = 'C:\\Knowledge Base\\GreyAtom\\nlp-in-python-master\\intermediate\\review_text_all.txt'
reviews_small = 'C:\\Knowledge Base\\GreyAtom\\nlp-in-python-master\\intermediate\\review_text_all_small.txt'

input = codecs.open(reviews, 'r', encoding='utf_8')
N = 2000
sample = [];
 
for i,line in enumerate(input):
    if i < N:
        sample.append(line)
    elif i >= N and random.random() < N/float(i+1):
        replace = random.randint(0,len(sample)-1)
        sample[replace] = line
		

with codecs.open(reviews_small, 'w', encoding='utf_8') as review_txt_file:
    for line in sample:
        review_txt_file.write(line)