import pandas as pd
import tkinter as tk
from tkinter import ttk
import time
import amazon_phones as af
import trendyol_phones as tf

af.fetch_amazon_phones()
time.sleep(2)
tf.fetch_trendyol_phones()
time.sleep(2)
df1 = pd.read_excel('amazon_products.xlsx')
df2 = pd.read_excel('trendyol_products.xlsx')


def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = text.strip()
        text = text.replace(',', ' ')
        text = text.replace('.', '')
    return text


df1['Product Name'] = df1['Product Name'].apply(clean_text)
df2['Product Name'] = df2['Product Name'].apply(clean_text)


def clean_price(price):
    if isinstance(price, str):
        price = price.replace(',', '.')
        price = price.replace(' TL', '')

        price = ''.join(char for char in price if char.isdigit() or char == '.')
    try:
        return float(price)
    except ValueError:
        return float('nan')


df1['Price'] = df1['Price'].apply(clean_price)
df2['Price'] = df2['Price'].apply(clean_price)


df1 = df1.sort_values(by='Product Name').reset_index(drop=True)
df2 = df2.sort_values(by='Product Name').reset_index(drop=True)


combined_df = pd.DataFrame({
    'Product Name (Amazon)': df1['Product Name'],
    'Price (Amazon)': df1['Price'],
    'Product Name (Trendyol)': df2['Product Name'].reindex(df1.index).fillna('N/A'),
    'Price (Trendyol)': df2['Price'].reindex(df1.index).fillna('N/A')
})



class PriceComparisonApp:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Ürün Fiyat Karşılaştırması")


        self.tree = ttk.Treeview(root, columns=(
            'Product Name (Amazon)', 'Price (Amazon)', 'Product Name (Trendyol)', 'Price (Trendyol)'), show='headings')
        self.tree.heading('Product Name (Amazon)', text='Ürün Adı (Amazon)')
        self.tree.heading('Price (Amazon)', text='Fiyat (Amazon)')
        self.tree.heading('Product Name (Trendyol)', text='Ürün Adı (Trendyol)')
        self.tree.heading('Price (Trendyol)', text='Fiyat (Trendyol)')
        self.tree.pack(fill=tk.BOTH, expand=True)

        for index, row in data.iterrows():
            self.tree.insert('', 'end', values=(
                row['Product Name (Amazon)'],
                row.get('Price (Amazon)', 'N/A'),
                row.get('Product Name (Trendyol)', 'N/A'),
                row.get('Price (Trendyol)', 'N/A')))



root = tk.Tk()
app = PriceComparisonApp(root, combined_df)
root.mainloop()
