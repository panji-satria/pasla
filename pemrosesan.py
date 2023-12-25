#pemrosesan.py

import concurrent.futures

def pemrosesan_paralel(data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        hasil = list(executor.map(proses_tugas, data))
    return hasil

def proses_tugas(item):
    # Implementasi pemrosesan untuk setiap item
    return item * 2  #belum disesuaikan
