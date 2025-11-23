import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import time

# ===========================
# KONFIGURASI DATABASE
# ===========================
HOST = "localhost"
USER = "root"                   # username mySQL
PASSWORD = "aulianurarkan"      # password mySQL
DATABASE = "moduleone"          # nama database
TABLE = "car_rental"            # nama table
CSV_PATH = "car_rental.csv"     # file csv

# ===========================
# HELPER: untuk koneksi ke MySQL
# ===========================
def get_conn():
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return db

# ===========================
# INISIALISASI PROGRAM
# ===========================
def init_program():
    print("Sedang mengakses MySQL database...")
    time.sleep(1)          # Fungsi Delay dalam detik(s)

    conn = get_conn()
    print("Terhubung.")
    time.sleep(0.7)

    print("Memeriksa struktur tabel...")
    time.sleep(1)

    cur = conn.cursor()  # membuat cursor untuk menjalankan perintah SQL

    cur.execute(f"SELECT 1 FROM {TABLE} LIMIT 1")  
    # menjalankan query untuk mengecek apakah tabel ada

    _ = cur.fetchone()  
    # membaca SATU baris hasil query agar buffer MySQL kosong
    # mencegah error "Unread result found" saat query berikutnya

    cur.close()             # menutup cursor

    print("Tabel siap.")
    time.sleep(0.7)

     # ---- CEK & PERBAIKI AUTO_INCREMENT rental_id ----
    conn2 = get_conn()
    cur2 = conn2.cursor()

    cur2.execute("SHOW COLUMNS FROM car_rental LIKE 'rental_id'")
    col_info = cur2.fetchone()
    extra = col_info[5]  # kolom Extra

    # Cek apakah auto increment untuk kolom unik rental_id sudah aktif
    if extra != 'auto_increment':
        print("Kolom rental_id belum AUTO_INCREMENT... memperbaiki struktur tabel...")
        cur2.execute("""
            ALTER TABLE car_rental
            MODIFY COLUMN rental_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;
        """)
        conn2.commit()
        print("Struktur tabel berhasil diperbaiki.")
    else:
        print("Kolom rental_id sudah AUTO_INCREMENT.")

    cur2.close()
    conn2.close()

    print("Loading data...")
    time.sleep(1)

    # buka koneksi baru
    conn2 = get_conn()
    df = pd.read_sql(f"SELECT * FROM {TABLE}", conn2)
    conn2.close()

    print(f"{len(df)} baris telah dimuat.\n")

# ===========================
# 1. Menampilkan Tabel
# ===========================
def menampilkan_tabel():
    
    # Ambil data langsung dari database dan tampilkan (DataFrame).
    conn = get_conn()
    df = pd.read_sql(f"SELECT * FROM {TABLE}", conn)
    conn.close()

    # Pastikan rental_id tampil sebagai integer, bukan float
    if 'rental_id' in df.columns:
        df['rental_id'] = df['rental_id'].astype('Int64')
        
    print("\n=== DATA RENTAL MOBIL ===\n")
    print(df)

# ===========================
# 2. Statistik Data
# ===========================
def statistik_data():
    conn = get_conn()
    df = pd.read_sql(f"SELECT * FROM {TABLE}", conn)
    conn.close()
    print("\n=== STATISTIK DATA ===\n")
    print(df.describe(include="all"))

# ===========================
# 3. Visualisasi Data
# ===========================
def visualisasi_data():
    conn = get_conn()
    df = pd.read_sql(f"SELECT * FROM {TABLE}", conn)
    conn.close()

    # memastikan kolom rental_date adalah datetime jika tersedia
    if 'rental_date' in df.columns:
        df['rental_date'] = pd.to_datetime(df['rental_date'], errors='coerce')

    print("""
    Pilihan Visualisasi:
    1. Pie Chart car_type
    2. Bar Plot branch_city
    3. Histogram rental_cost
    4. Scatter plot (rental_duration vs rental_cost)
    5. Line Plot (Total Pendapatan Per Hari)
    """)

    pilihan = input("Pilih visualisasi (1-5): ").strip()

    if pilihan == "1":
        df["car_type"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
        plt.title("Proporsi Jenis Mobil")
        plt.ylabel('')
        plt.show()

    elif pilihan == "2":
        sns.countplot(data=df, x="branch_city")
        plt.title("Jumlah Penyewaan per Cabang")
        plt.show()

    elif pilihan == "3":
        df["rental_cost"].hist(bins=10)
        plt.title("Distribusi Biaya Sewa")
        plt.xlabel("Biaya")
        plt.ylabel("Frekuensi")
        plt.show()

    elif pilihan == "4":
        sns.scatterplot(data=df, x="rental_duration", y="rental_cost",
                        hue="car_type" if 'car_type' in df.columns else None)
        plt.title("Durasi vs Biaya Sewa")
        plt.show()

    elif pilihan == "5":
        # asumsikan kolom rental_date & rental_cost ada
        daily_revenue = df.groupby(df['rental_date'].dt.date)['rental_cost'].sum()
        plt.figure(figsize=(10,4))
        daily_revenue.plot(marker='o')
        plt.title("Total Pendapatan per Hari")
        plt.xlabel("Tanggal")
        plt.ylabel("Total Pendapatan")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print("Pilihan tidak valid.")

# ===========================
# 4. Menambahkan Data
# ===========================
def menambah_data():
    print("\n=== Tambah Data Rental ===")

    # Input disetiap kolomnya
    # strip() ---> untuk menghapus spasi di depan / belakang, karakter new line (\n) dan tab (\t). 
    # strip() juga menghindari error input karena spasi yang tidak disengaja

    car_type = input("Jenis mobil (SUV/Sedan/etc): ").strip()
    rental_duration = int(input("Durasi sewa (hari): ").strip())
    rental_cost = float(input("Biaya sewa: ").strip())
    customer_gender = input("Gender (Male/Female): ").strip()
    rental_date = input("Tanggal sewa (YYYY-MM-DD): ").strip()
    branch_city = input("Kota cabang: ").strip()

    # koneksi ke MySQL
    conn = get_conn()
    cur = conn.cursor()

    # INSERT tanpa rental_id karena MySQL AUTO_INCREMENT akan mengisi otomatis
    query = f"""
        INSERT INTO {TABLE}
        (car_type, rental_duration, rental_cost, customer_gender, rental_date, branch_city)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cur.execute(query, (
        car_type,
        rental_duration,
        rental_cost,
        customer_gender,
        rental_date,
        branch_city
    ))
    conn.commit()

    # lastrowid ---> integer dari AUTO_INCREMENT
    new_id = cur.lastrowid

    print(f"Data berhasil ditambahkan! rental_id = {new_id}")

    cur.close()
    conn.close()

# ===========================
# 5. Menghapus Data
# ===========================
def menghapus_data():
    print("\n=== Hapus Data Rental ===")

    # Validasi input ---> harus angka
    while True:
        rid = input("Masukkan rental_id yang ingin dihapus: ").strip()

        # cek apakah input terdiri dari digit (angka)
        if rid.isdigit():
            rental_id = int(rid)
            break
        else:
            print("Input tidak valid! Masukkan angka yang benar.\n")

    # Proses delete
    conn = get_conn()
    cur = conn.cursor()

    # Query untuk menghapus baris
    delete_query = f"DELETE FROM {TABLE} WHERE rental_id = %s"
    cur.execute(delete_query, (rental_id,))
    conn.commit()

    # Mengecek jumlah baris di dalam database yang terkena dampak query SQL 
    if cur.rowcount > 0:
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan.")

    cur.close()
    conn.close()

# ===========================
# 6. Export seluruh tabel ke CSV
# ===========================
def export_to_csv():
    print("Mengekspor data ke CSV...")
    conn = get_conn()
    df = pd.read_sql(f"SELECT * FROM {TABLE}", conn)
    conn.close()
    df.to_csv(CSV_PATH, index=False)
    print(f"Sukses: data disimpan ke file '{CSV_PATH}'.")

# ===========================
# MENU UTAMA
# ===========================

# Program utama
if __name__ == "__main__":
    
    # init (akan error/stop jika koneksi/tabel bermasalah)
    init_program()

    while True:
        pilihan = input('''
===============================
      CAR RENTAL SYSTEM
===============================

1. Menampilkan Tabel
2. Melihat Statistik
3. Visualisasi Data
4. Menambahkan Data
5. Menghapus Data
6. Simpan tabel ke CSV
7. Keluar

Masukkan pilihan: ''')

        if pilihan == "1":
            menampilkan_tabel()
        elif pilihan == "2":
            statistik_data()
        elif pilihan == "3":
            visualisasi_data()
        elif pilihan == "4":
            menambah_data()
        elif pilihan == "5":
            menghapus_data()
        elif pilihan == "6":
            export_to_csv()
        elif pilihan == "7":
            print("Keluar program...")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
