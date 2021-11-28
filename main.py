def sort_sentence(sentence):
    spisok_slov = sorted(sentence.split(), key = len)
    ouyaddgfitrdjlsnfr = " ".join(spisok_slov).capitalize()
    return ouyaddgfitrdjlsnfr

if __name__ == '__main__':
    m = input("Ввести строчку/: \n \n \n \n ")
    print(sort_sentence(m))
