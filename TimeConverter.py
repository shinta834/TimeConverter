def timeConverter (x):
    # menentukan jam
    hour = (x % 86400)// 3600
    # menentukan menit
    minute = (x%3600) // 60
    # menentukan detik
    seconds = x%60
    # print output
    text = 'Konversi : {:02d}:{:02d}:{:02d}'
    print(text.format(hour,minute,seconds))

# User Input
x= int(input('Masukkan detik : '))
timeConverter(x)