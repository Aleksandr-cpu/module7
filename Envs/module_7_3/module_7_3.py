
class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctu = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            lst = []
            with open(file, encoding='utf-8') as f:
                for line in f:
                    for i in punctu:
                        line = line.replace(i, ' ')
                    for j in line.split():
                        lst.append(j.lower())
            all_words[file] = lst
        return all_words

    def find(self, word):
        dic = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i != word:
                    count += 1
                else:
                    break
            dic[name] = count+1
        return dic

    def count(self, word):
        dic = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
            dic[name] = count
        return dic





finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))