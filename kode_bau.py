"""Modul demonstrasi fungsi kalkulasi sesuai standar PEP 8."""


def hitung_total(nilai_awal, faktor_pengali):
    """Menghitung total nilai berdasarkan faktor pengali.

    Args:
        nilai_awal: Nilai dasar input.
        faktor_pengali: Faktor pengali nilai dasar.

    Returns:
        Hasil perkalian nilai dasar dengan pengali.
    """
    return nilai_awal * faktor_pengali


def main():
    """Fungsi utama program."""
    hasil = hitung_total(10, 2)
    print(f"Total: {hasil}")


if __name__ == "__main__":
    main() 
