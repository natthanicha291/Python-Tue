print('------------------')
print('KPH \t MPH')
print('------------------')

for KPH in range(60, 131, 10):
    MPH = MPH = KPH*0.6214
    print(f"{KPH} \t {MPH:.1f}")

print('------------------')