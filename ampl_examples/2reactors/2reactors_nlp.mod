# Нелинейная постановка задачи о выборе реактора
set REACTORS; # Множество реакторов

param cost_proc {REACTORS}; #Коэффициенты для затрат на переработку
param a {REACTORS}; # Показатель степени для затрат на переработку
param cost_rm; #стоимость сырья

param conversion {REACTORS}; #Степень превращения в реакторе

param x_start {REACTORS}; # начальное приближение

param yield; # Требуемая производительность по продукту

var x {r in REACTORS} >=1e-10 := x_start[r]; # потоки питания реакторов
# Без нижней границы не считается, т.к. бесконечны частные производные в нуле
# x_start - начальное приближение

# Целевая функция - минимум совокупных затрат (сырье + переработка)
minimize TotalCost:
	sum {r in REACTORS} cost_proc[r] * x[r]^a[r] 
			+ cost_rm * sum {r in REACTORS} x[r];

subject to Yield:
	sum {r in REACTORS} conversion[r] * x[r] = yield;
	

data;

param :	REACTORS :	cost_proc	a	conversion	x_start :=
		r1			5.5			0.6	0.8			1
		r2			4.0			0.6	0.667		1;
		
param yield := 10;
param cost_rm := 5;

end;


 			

