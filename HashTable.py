class HashTable: 
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
    ht = HashTable()
    ht.insert('First Name', 'Brian')
    ht.insert('Last Name', 'Stephenson')
    ht.insert('Age', '33')
    ht.insert('Gender', 'Male')
    ht.insert('Ethnicity', 'Black')
    ht.insert('Country', 'United States')
    ht.insert('Email Address', 'Brian.Stephenson@mail.com')
    ht.remove('Ethnicity')
    print(ht.printPairs())
    print(ht.search('First Name'))
    #print(ht.search('Gender'))
    #print(ht.search('Country'))