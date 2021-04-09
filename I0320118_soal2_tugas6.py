print("PENGHITUNGAN NILAI RATA-RATA")

n = int(input("Banyaknya Data: "))

print()
data = []
jml = 0

for i in range(0, n):
    input_data = int(input("Masukkan data ke-%d: " % (i+1)))
    data.append (input_data)
    jml += data[i]
    rata2 = jml / n

print("Nilai Rata-ratanya adalah = %f" % rata2)