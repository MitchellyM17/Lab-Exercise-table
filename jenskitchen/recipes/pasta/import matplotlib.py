import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Membuat diagram DFD tingkat konteks (aliran data antara entitas dan sistem)

fig, ax = plt.subplots(figsize=(10, 8))

# Membuat entitas eksternal: Pelanggan dan Pemasok
ax.text(0.1, 0.8, 'Pelanggan', fontsize=12, bbox=dict(facecolor='skyblue', edgecolor='black'))
ax.text(0.1, 0.2, 'Pemasok', fontsize=12, bbox=dict(facecolor='skyblue', edgecolor='black'))

# Membuat sistem utama: Penjualan, Produksi, Keuangan
ax.text(0.7, 0.8, 'Penjualan', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))
ax.text(0.7, 0.6, 'Produksi', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))
ax.text(0.7, 0.4, 'Keuangan', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))

# Menambah koneksi antar elemen dengan panah
arrowprops = dict(facecolor='black', arrowstyle='->')

# Panah dari pelanggan ke penjualan
ax.annotate('', xy=(0.5, 0.8), xytext=(0.3, 0.8), arrowprops=arrowprops)
ax.text(0.3, 0.82, 'Pesanan')

# Panah dari penjualan ke produksi
ax.annotate('', xy=(0.75, 0.7), xytext=(0.75, 0.8), arrowprops=arrowprops)
ax.text(0.77, 0.75, 'Info Pesanan')

# Panah dari produksi ke keuangan
ax.annotate('', xy=(0.75, 0.5), xytext=(0.75, 0.6), arrowprops=arrowprops)
ax.text(0.77, 0.55, 'Info Produksi')

# Panah dari keuangan ke pelanggan
ax.annotate('', xy=(0.5, 0.4), xytext=(0.3, 0.4), arrowprops=arrowprops)
ax.text(0.3, 0.42, 'Faktur')

# Panah dari pemasok ke produksi
ax.annotate('', xy=(0.5, 0.6), xytext=(0.3, 0.2), arrowprops=arrowprops)
ax.text(0.3, 0.62, 'Bahan Baku')

# Panah dari produksi ke pemasok
ax.annotate('', xy=(0.3, 0.25), xytext=(0.5, 0.55), arrowprops=arrowprops)
ax.text(0.52, 0.4, 'Permintaan Bahan')

# Menghapus sumbu
ax.axis('off')

plt.title('DFD Tingkat Konteks - XYZ Corporation', fontsize=14)
plt.show()