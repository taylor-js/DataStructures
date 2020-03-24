class Dictionary: 
    def __init__(self):
        self.dictionary = {}

    def insert(self, key, value):
        self.dictionary[key] = value

    def remove(self, key):
        del self.dictionary[key]

    def printPairs(self):
        return self.dictionary

    def search(self, field):
        for key,value in self.dictionary.items():
            if key == field:
                return value

if __name__ == '__main__':
    d = Dictionary()
    d.insert('First Name', 'Brian')
    d.insert('Last Name', 'Stephenson')
    d.insert('Age', '33')
    d.insert('Gender', 'Male')
    d.insert('Ethnicity', 'Black')
    d.insert('Country', 'United States')
    d.insert('Email Address', 'Brian.Stephenson@mail.com')
    d.remove('Ethnicity')
    print(d.printPairs())
    print(d.search('First Name'))
    #print(ht.search('Gender'))
    #print(ht.search('Country'))