import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        # self.data = dict()
        with open(filepath, 'r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f'Cannot extract data from {filepath}')
    return extractor(filepath)


def extract_data_from(filepath):
    factoty_obj = None
    try:
        factoty_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factoty_obj


def main():
    sqlite_factory = extract_data_from('data/person.sq3')
    print('\n')

    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    print()
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print('\n')

    xml_factory = extract_data_from('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'Found: {len(liars)} persons')
    print()
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text)
         for p in liar.find('phoneNumbers')]
        print()


if __name__ == '__main__':
    main()
