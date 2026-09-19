# 19-17 debugging after reading in poorly formatted cities.csv
#       - no problems with cities.csv
#   Now try with cities2.csv
#       - fails on the capital of ecuador: quito

def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            
            if 'quit' in line.lower():
                return
            
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')

if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])