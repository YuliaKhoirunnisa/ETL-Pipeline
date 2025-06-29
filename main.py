# main.py
from extract import extract_all_pages
from transform import transform_data, remove_invalid_data
from load import save_to_csv, save_to_gsheet

def main():
    print("📥 Mulai proses extract...")
    raw_data = extract_all_pages()
    print("📊 Jumlah data hasil extract:", len(raw_data))

    print("🔧 Mulai proses transform...")
    df_clean = transform_data(raw_data)
    df_clean = remove_invalid_data(df_clean)  # Bersihkan invalid data
    print("🧼 Jumlah data hasil transform:", len(df_clean))

    print("💾 Menyimpan ke CSV...")
    save_to_csv(df_clean, filename="data/fashion_studio_data.csv")

    print("📤 Mengunggah ke Google Sheets...")
    save_to_gsheet(df_clean, "ETL", creds_file="credentials.json")

if __name__ == "__main__":
    main()