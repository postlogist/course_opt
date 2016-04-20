# Частично целочисленная постановка задачи о выборе реактора
set REACTORS; # Множество реакторов

param cost_proc {REACTORS}; #Переменные затраты на переработку
param fixed_proc {REACTORS}; #Постоянные затраты на переработку

param cost_rm; #стоимость сырья

param conversion {REACTORS}; #Степень превращения в реакторе

param yield; # Требуемая производительность по продукту

param bigM; # Большое число для импликации x -> y

var x {r in REACTORS} >=0 ; # потоки питания реакторов
var y {r in REACTORS} binary; # выбор реакторов

# Целевая функция - минимум совокупных затрат (сырье + переработка)
minimize TotalCost:
	sum {r in REACTORS} (cost_proc[r] * x[r] + fixed_proc[r] * y[r]) 
			+ cost_rm * sum {r in REACTORS} x[r];

subject to Yield:
	sum {r in REACTORS} conversion[r] * x[r] = yield;
	
subject to Select {r in REACTORS} :
	x[r] <= bigM * y[r];


data;

param :	REACTORS :	cost_proc	fixed_proc	conversion :=
		r1			1.74		4.72	0.8
		r2			1.18		3.83	0.667;
		
param yield := 10;
param cost_rm := 5;
param bigM := 20;

end;