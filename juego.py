import monstruo

vibora = monstruo.Vibora("Viki", 100, 5, 5, 10,10)
vibora2 = monstruo.Vibora("Fefito", 100, 5, 6, 7, 5)

print(f"{vibora2.name} enveneno a {vibora.name}")
vibora2.envenenar(vibora)
print(f"{vibora.estado}")