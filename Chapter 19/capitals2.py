# 19-19 debug capitals.py when reading in cities2.csv

def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()

            if 'quit' == line.lower():  # capitals.py uses "if 'quit' in line.lower()"
                return

            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            
            print(city.title(), country.title(), sep=',')

if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])