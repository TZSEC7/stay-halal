import requests
import os
import sys
import time


os.system('clear')

# Color
m = '\033[31;1m'
r = '\033[0m'
b = '\033[1m'
y = '\033[32;1m'


def al():
    os.system('figlet stay-halal')
    url = "https://equran.id/api/surat"
    response = requests.get(url)
    print()
    x = '\033[32;1m[\033[31;1m+\033[32;1m]\033[0m'
    if response.status_code == 200:
        data = response.json()
        for surat in data:
            print(f"{x} Nomor:", surat['nomor'])
            print(f"{x} Nama:", surat['nama'])
            print(f"{x} Nama Latin:", surat['nama_latin'])
            print(f"{x} Jumlah Ayat:", surat['jumlah_ayat'])
            print(f"{x} Tempat Turun:", surat['tempat_turun'])
            print(f"{x} Arti:", surat['arti'])
            #print("Deskripsi:", surat['deskripsi'])
            #print("Link Audio:", surat['audio'])
            print("-"*40)
    # Now 'data' contains the JSON response from the API.
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

al()
pil = input('Zaunkssec > ')
print()
url = f"https://equran.id/api/v2/surat/{pil}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # If the response contains JSON data
    # You can now work with the 'data' variable, which contains the response data.
    #print(data)
    # Accessing specific values in the 'data' dictionary
    surat_name = data['data']['nama']
    jumlah_ayat = data['data']['jumlahAyat']
    tempat_turun = data['data']['tempatTurun']
    arti = data['data']['arti']

# Accessing values within the 'audioFull' dictionary
    audio_links = data['data']['audioFull']
    audio_link_01 = audio_links['01']

# Accessing values within the 'ayat' list
    first_ayat = data['data']['ayat'][0]
    nomor_ayat = first_ayat['nomorAyat']
    teks_arab = first_ayat['teksArab']
    teks_indonesia = first_ayat['teksIndonesia']

# Accessing the 'suratSelanjutnya' information
    next_surat_name = data['data']['suratSelanjutnya']['nama']
    next_surat_ayat_count = data['data']['suratSelanjutnya']['jumlahAyat']

# Checking if 'suratSebelumnya' exists
    surat_sebelumnya = data['data']['suratSebelumnya']

# Printing the values
    print(f"{y}Surat Name{r}: {surat_name}")
    print(f"{y}Jumlah Ayat{r}: {jumlah_ayat}")
    print(f"{y}Tempat Turun{r}: {tempat_turun}")
    print(f"{y}Arti{r}: {arti}\n")
    ayat_data = data['data']['ayat']
    for ayat in ayat_data:
        nomor_ayat = ayat['nomorAyat']
        teks_arab = ayat['teksArab']
        teks_indonesia = ayat['teksIndonesia']
        teks_latin = ayat['teksLatin']
        print("-"*40)
        print(f"{y}Nomor Ayat{r}: {nomor_ayat}")
        print(f"{y}Teks Arab{r}: {teks_arab}")
        print(f"{y}Teks Latin{r}: {teks_latin}")
        print(f"{y}Teks Indonesia{r}: {teks_indonesia}\n")

    print(f"Nama Surat Selanjutnya: {next_surat_name}")
    print(f"Jumlah Ayat Surat Selanjutnya: {next_surat_ayat_count}")

# Check if 'suratSebelumnya' exists
    if surat_sebelumnya:
        print("Surat Sebelumnya exists")
    else:
        print("Surat Sebelumnya does not exist")
