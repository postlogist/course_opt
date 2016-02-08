# Длина
meter = 1
cm = 0.01 * meter
dm = 10 * cm
ft = 0.3048 * meter #фут

# Площадь
meter_sq = meter**2
ft_sq = ft**2

# Объем
meter_cub = meter**3
liter = dm**3

# Масса
gm = 1 
kg = 1000 * gm
ton = 1000 * kg

# Количество вещества
mol = 1 
kmol = 1000 * mol

# Время
second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
year = 365 * day
yearl = 365.25 * day #средняя длительность года с учетом високосных

# Энергия
joule = 1
kJ = 1999 * joule
BTU = 1055.056 * joule
Wh = 3600 * joule
kWh = Wh * 1000
MWh = kWh * 1000

# Мощность
W = joule/second
kW = 1000 * W

# Температура
K = 1

def C_K(C):
	return C + 273.15

def K_C(K):
	return C - 273.15
	
def F_C(F):
	return 5./9 * (F - 32)
	
def C_F(C):
	return 9./5 * C + 32
	
def F_K(F):
	return C_K(F_C(F))
	