
import os
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    try:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit()
    except Exception as e:
        print(f"Kesalahan: {e}")
        sys.exit()
        
from googlesearch import search

def google_search(query, num_results=25):
    try:
        search_results = search(query, num_results=num_results)
        
        print("Hasil pencarian untuk '{}':".format(query))
        for i, result in enumerate(search_results, start=1):
            print("{}. {}".format(i, result))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    nama = ["Projek Google Search v1.0", "by Yogi Ario"]
    for i in nama:
        print(i)
    print("\n")
    print("Pencarian ini hanya menghasilkan link yang mengharuskan anda untuk memilih")
    
    while True:
        keyword = input("Masukkan kata kunci pencarian: ")
        
        google_search(keyword)
        
        pilihan = input("Tekan 1 untuk melakukan pencarian ulang atau tekan enter untuk keluar: ")
        if pilihan != '1':
            break
