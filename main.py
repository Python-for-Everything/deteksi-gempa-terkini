"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTIOn
"""


def ekstraksi_data():
    """
    Tanggal : 03 Oktober 2024
    Waktu10 : 12:41 WIB
    Magnitudo : 3.8
    Kedalaman : 12 km
    Lokasi : LS=2.48 BT=140.43
    Pusat Gempa : Pusat gempa berada di darat 12 km timurlaut Kab. Jayapura
    Keteragan : Dirasakan (Skala MMI): III Kab. Jayapura
    :param result:
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '03 Oktober 2024'
    hasil['waktu'] = '12:41 WIB'
    hasil['magnitudo'] = 3.8
    hasil['kedalaman'] = 12
    hasil['lokasi'] = {'ls':2.48, 'bt':140.43}
    hasil['pusat_gempa'] = 'Pusat gempa berada di darat 12 km timurlaut Kab. Jayapura'
    hasil['keterangan'] = 'Dirasakan (Skala MMI): III Kab. Jayapura'
    return hasil


def tampilkan_data(result):
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal'{result['tanggal']}")
    print(f"Waktu' {result['waktu']}")
    print(f"Magnitudo' {result['magnitudo']}")
    print(f"Kedalaman' {result['kedalaman']}")
    print(f"Lokasi LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat_gempa' {result['pusat_gempa']}")
    print(f"Keterangan' {result['keterangan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
    
