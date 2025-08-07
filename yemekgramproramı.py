malzemeler = []
sonfiyat = []
tgram = []

malzeme = input("malzeme adını gir : ")
malzemeler.append(malzeme)

while len(malzeme) != 0 :
    gram = float(input("malzeme gramını gir : "))
    tgram.append(gram)
    maliyet = float(input("kg maliyetini gir : "))
    fiyat = maliyet / 1000 * gram
    sonfiyat.append(fiyat)
    print(fiyat)
    print("işlemi bitirmek isterseniz malzeme kısmına hiç birşey yazmayınız")
    malzeme = input("malzeme adını gir : ")
    malzemeler.append(malzeme)


print("yemeğin toplam fiyatı " + str(sum(sonfiyat)) +" tl")
print("kullanılan malzemeler " +str(malzemeler))
print("yemeğin toplam gram biçiminden kütlesi " + str(sum(tgram)))


