def divideAndSort(bil):
	# Ubah jadi string, lalu split berdasarkan '0'
	Lbil = str(bil).split('0')
	# Ubah semua isi List bilangan menjadi int, lalu urutkan descending
	for i in range(len(Lbil)):
		Lbil[i] = int(Lbil[i])
	Lbil.sort(reverse=True)
	# Ubah kembali tiap isi List biangan menjadi string
	for i in range(len(Lbil)):
		Lbil[i] = str(Lbil[i])
	# Semua isi List bilangan disatukan
	Lbil = "".join(Lbil)
	# Menuliskan ke layar hasil
	print(Lbil)

def cetak_gambar(iter):
	if (iter % 2 == 1 and iter > 0):
		print('--- panjang ---')
		for i in range(iter):
			for j in range(iter):
				if (i == int(iter / 2)):
					print('*', end='')
				else:
					if (j == 0 or j == iter-1):
						print('*', end='')
					else:
						print('=', end='')
			print('')