#Escreva um código que leia um valor em metros e mostre os valores convertidos em cm e mm

m = float(input('Digite uma medida em metros: '))
cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dm = m/10

print('A medida informada foi {:.2f} m, que corresponde a {:.2f} cm e {:.2f} mm.'.format(m, cm, mm))
print('A medida também equivale a {:.2f} km, {:.2f} hm e {:.2f} dm'.format(km, hm, dm))