f=open('vacancy.csv')
a=[i for i in f.readlines()]
def main():
    b=input('Введите название компании:')
    for i in a:
        i=i.split (';')
        if i[4]==b+'\n':
            return print(f'В {i[4]} найдена вакансия: {i[3]}. З/п составит: {i[0]}')
    if b=='None':
        return False
    return print('К сожалению, ничего не удалось найти')
while True:
    if main()==False:
        break



