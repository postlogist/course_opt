# Линейная постановка задачи о выборе реактора
set REACTORS; # Множество реакторов

param cost_proc {REACTORS}; #Переменные затраты на переработку

param cost_rm; #стоимость сырья

param conversion {REACTORS}; #Степень превращения в реакторе

param yield; # Требуемая производительность по продукту


var x {r in REACTORS} >=0 ; # потоки питания реакторов

# Целевая функция - минимум совокупных затрат (сырье + переработка)
minimize TotalCost:
	sum {r in REACTORS} cost_proc[r] * x[r] 
			+ cost_rm * sum {r in REACTORS} x[r];

subject to Yield:
	sum {r in REACTORS} conversion[r] * x[r] = yield;
	

data;

param :	REACTORS :	cost_proc	conversion :=
		r1			2.31		0.8
		r2			1.56		0.667;
		
param yield := 10;
param cost_rm := 5;

end;