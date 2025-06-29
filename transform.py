import pandas as pd

def convert_price_to_idr(price_str, exchange_rate=16000):
    try:
        price_num = float(price_str.replace("$", "").replace(",", ""))
        return price_num * exchange_rate
    except Exception:
        return None

def clean_rating(rating_str):
    try:
        if "Rating:" in rating_str:
            rating_str = rating_str.replace("Rating:", "")
        rating_str = rating_str.replace("⭐", "").strip()
        return float(rating_str.split("/")[0].strip())
    except Exception:
        return None

def extract_number_colors(colors_str):
    try:
        return int(colors_str.split()[0])
    except Exception:
        return None

def clean_size(size_str):
    return size_str.replace("Size: ", "").strip()

def clean_gender(gender_str):
    return gender_str.replace("Gender: ", "").strip()

def transform_data(raw_data):  # <<=== INI YANG DIHARUSKAN
    df = pd.DataFrame(raw_data)
    print(f"Total data awal: {len(df)}")

    df["Price"] = df["Price"].apply(lambda x: convert_price_to_idr(x) if x else None)
    df["Rating"] = df["Rating"].apply(lambda x: clean_rating(x) if x else None)
    df["Colors"] = df["Colors"].apply(lambda x: extract_number_colors(x) if x else None)
    df["Size"] = df["Size"].apply(lambda x: clean_size(x) if x else "")
    df["Gender"] = df["Gender"].apply(lambda x: clean_gender(x) if x else "")

    if df["Price"].isna().any():
        print("⚠️ Ada nilai Price yang gagal diparsing.")
    if df["Rating"].isna().any():
        print("⚠️ Ada nilai Rating yang gagal diparsing.")
    if df["Colors"].isna().any():
        print("⚠️ Ada nilai Colors yang gagal diparsing.")

    print("Jumlah Price NaN:", df["Price"].isna().sum())
    print("Jumlah Title = 'Unknown Product':", (df["Title"] == "Unknown Product").sum())

    # ✅ Hapus duplicate berdasarkan subset kolom penting
    df = df.drop_duplicates(subset=["Title", "Price", "Rating", "Size", "Gender"], keep='first')

    df = df.astype({
        "Title": "string",
        "Price": "float",
        "Rating": "float",
        "Colors": "Int64",
        "Size": "string",
        "Gender": "string",
        "timestamp": "string"
    }, errors='ignore')

    return df.reset_index(drop=True)

def remove_invalid_data(df):
    df = df[df["Title"] != "Unknown Product"]
    df = df.dropna(subset=["Price", "Rating"])
    return df