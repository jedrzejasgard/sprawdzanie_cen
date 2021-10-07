import configparser
from time import gmtime, strftime
import datetime

# laduje hasla i delikatne dane
config = configparser.ConfigParser()
config.read('konkurencja.ini')


def sprawdź_cene_macma():
    macma_use = config.get('macma','usr')
    macma_pass = config.get('macma','pass')
    pass

def today_data():
    data = strftime('%Y, %m, %d', gmtime()).split(',')
    y = int(data[0])
    m = int(data[1])
    d = int(data[2])
    data = datetime.date(y, m, d).strftime("%V")
    return data


def zapisz_blad(kto_z_konk,text_bledu):
    with open(f"./bledy/{kto_z_konk}-bledy-tydzien{data}.txt", 'a+') as plik:
        plik.write(f"{text_bledu}\n")


def zapisz_wyprzedaz(kto_z_konk,indeksProd,cena_wyp,asgard_prod):
    with open(f"./wyprz/{kto_z_konk}-wyprzedaż-tydzien{data}.txt", 'a+') as plik:
        plik.write(f"Asgard index: {asgard_prod} (konkurencja:{indeksProd}) cena na wyprzedaży : {cena_wyp}\n")


def format_float(wartosc):
    try:
        return round(float(wartosc.replace(',','.')), 2)
    except:
        return round(float(wartosc), 2)



if __name__ == '__main__':
    main()

