import re
from collections import Counter

class Model:
    def __init__(self, data):
        self.data = data
        self.pattern_tu = re.compile(r'<translation\.unit (.*?)</translation\.unit>')
        self.pattern_en = re.compile(r'<en[> ](.*?)</en>')
        self.pattern_id = re.compile(r'id="(.*?)"')

    def get_duplicate_ids(self):
        tu_list = self.pattern_tu.findall(self.data)
        id_en_dict = {}
        for tu in tu_list:
            en = self.pattern_en.findall(tu)
            id = self.pattern_id.findall(tu)
            id_en_dict[id[0]] = en[0]

        counts = Counter(id_en_dict.values())
        duplicate_ids = {k for k, v in id_en_dict.items() if counts[v] > 1}
        return duplicate_ids
   
    def save_duplicate_ids(self,duplicate_ids):
        myfile = open('duplicateIDs.txt', 'w')
        myfile.write('DUPLICATE IDs'+'\n-------------------------')
        for id in duplicate_ids:
            myfile.write(id+'\n')
        myfile.close()

class View:
    @staticmethod
    def user():
        path = input("enter path : ").replace('\\','/').replace('"', '')
        print(path)
        return path
    
    @staticmethod
    def show_duplicate_ids(duplicate_ids):
        for id in duplicate_ids:
            print(id)
        input("done")
        
    @staticmethod
    def save_duplicate_ids():
        input("Duplicates saved")

class Controller:
    def __init__(self):
        self.filePath = View.user()
        
        try:
            with open(self.filePath, 'r', encoding="utf-8") as f:
                data = f.read().replace('\n', '')
            self.model = Model(data)
        except:
            self.model=Model("")
            print("invalid file path")

    def show_duplicates(self):
        duplicate_ids = self.model.get_duplicate_ids()
        View.show_duplicate_ids(duplicate_ids)
        self.model.save_duplicate_ids(duplicate_ids)
    
    def save_duplicates(self):
        duplicate_ids = self.model.get_duplicate_ids()
        self.model.save_duplicate_ids(duplicate_ids)
        View.save_duplicate_ids()

if __name__ == '__main__':
    try:
        controller = Controller()
        controller.save_duplicates()
    except:
        input("Error! Something is wrong!")






