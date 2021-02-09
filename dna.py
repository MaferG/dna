import fileinput
import re 
import sys

def get_db():
    """
    Get data from file and split by "," 
    """
    data = []
    for line in fileinput.input():
        line = line.strip()
        if not line:
            continue
        data.append(map(lambda x: x, line.split(",")))
    return data


def process(data):
    """
    Split data by strings, dna sentence and all persosn whit
    teir data 
    """
    strings = data[0][1:]
    dna = data[-1][0]
    items = {}
    for line in data[1:-1]:
        key, value = line[0], line[1:]
        items[key] = value

    return [strings, dna, items]


def get_dna_str_number(strs, dna):
    """
    Find STR data in dna sentence and returns a list
    with the numbers 
    """
    count = []
    for code in strs:
        res = max(re.findall('((?:' + re.escape(code) + ')*)', dna), key = len) 
        count.append(res.count(code))
    return count


def find_person(count, persons):
    """
    Compares the strings and find the matchS 
    """
    for person in persons:
        numbers = [ int(x) for x in persons[person] ]
        if count == numbers: 
            return person
    return 'No match'


def usage():

    print('python dna.py data.csv sequence.txt'.format(sys.argv[0]))
    exit()


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        usage()

    data = get_db()
    processed = process(data) 
    countFreq = get_dna_str_number(processed[0], processed[1])
    find = find_person(countFreq, processed[2])
    print(find)
