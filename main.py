from bloomfilter import BloomFilter
from random import shuffle

def main():
    number_of_items = 20
    false_positive_probability = 0.1
    bloom = BloomFilter(number_of_items, false_positive_probability)
    word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','genial']
    word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook',
               'geeksforgeeks','twitter']
    print('bloomfilter size: ', bloom.bit_size)
    print('false_positive_probability', bloom.false_positive_probability)
    print('hash_count: ', bloom.hash_count)

    for item in word_present:
        bloom.add(item)
    shuffle(word_present)
    shuffle(word_absent)
    random_list = word_present[:5] + word_absent[:5]
    shuffle(random_list)
    for word in random_list:
        print('word: ', word)
        if bloom.check(word):
            if word in word_absent:
                print('false positive')
            else:
                print('word most likely member')
        else:
            print('word not present')
    

if __name__ == "__main__":
    main()
