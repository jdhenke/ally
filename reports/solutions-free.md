# Solutions to Cooley's Game
## Exogenous Variables
	pd1=0.626
	pr1=0.283
	pa=0.1
	pd2=0.426
	pr2=0.483
	k=0.15

	ba=0.1
	bd=0.626
	br=0.283

##  Solution leading to t1

### Endogenous Variables

	ignore=1.0
	xi=0.0
	xj=-0.059041408
	yi=0.3318

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 0.02096 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.35324 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t5
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742
	t6
		a: 0.04096 = xj + 0.1
		r: 0.61480 = xi + yi + 0.283
		d: 0.35324 = -xi - xj - yi + 0.626
	t7
		a: 0.02096 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.35324 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.61480 = xi + yi + 0.283
		d: 0.29420 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t10
		a: ?None?  = xk + 0.1
		r: ?None?  = xi - xk + yi + 0.283
		d: 0.29420 = -xi - yi + 0.626
	t11
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t1:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: - 0.909 xi - yi >= -0.3318
	
	_C6: xj <= 0
	
	_C7: xi + yi >= -0.15
	
	_C8: - xi - yi <= -0.15
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t2

### Endogenous Variables

	ignore=1.0
	xi=-1.9978022
	xj=0.0
	yi=1.8478022

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: -0.14830 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.50452 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t5
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.13300 = xi + yi + 0.283
		d: 0.77600 = -xi - xj - yi + 0.626
	t7
		a: -0.14830 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.50452 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.13300 = xi + yi + 0.283
		d: 0.77600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t10
		a: ?None?  = xk + 0.1
		r: ?None?  = xi - xk + yi + 0.283
		d: 0.77600 = -xi - yi + 0.626
	t11
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t2:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: - 1.009 xi - yi >= -0.0518
	
	_C3: 0 xi + 0 xj >= 0
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: - 0.909 xi - yi >= -0.3318
	
	_C6: 0.1 xi + 0.517 xj <= 0.0485171102662
	
	_C7: xi + yi <= -0.15
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t3

### Endogenous Variables

	ignore=1.0
	xi=22.422222
	xj=-4.2431436
	yi=-18.029079

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 0.10000 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t5
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742
	t6
		a: -4.14314 = xj + 0.1
		r: 4.67614 = xi + yi + 0.283
		d: 0.47600 = -xi - xj - yi + 0.626
	t7
		a: 0.10000 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 4.67614 = xi + yi + 0.283
		d: -3.76714 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t10
		a: ?None?  = xk + 0.1
		r: ?None?  = xi - xk + yi + 0.283
		d: -3.76714 = -xi - yi + 0.626
	t11
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t3:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: 0.909 xi + 0.483 xj + yi >= 0.303282889734
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: 0.909 xi + yi >= 0.3318
	
	_C6: 0.1 xi + 0.517 xj >= 0.0485171102662
	
	_C7: - 0.009 xi >= -0.2018
	
	_C8: - 0.091 xi - 0.517 xj >= 0.153282889734
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t4

### Endogenous Variables

	ignore=1.0
	xi=-1.9978022
	xj=-0.059041408
	yi=2.1478022

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: -0.17882 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.53504 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t5
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742
	t6
		a: 0.04096 = xj + 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 0.53504 = -xi - xj - yi + 0.626
	t7
		a: -0.17882 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.53504 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t10
		a: ?None?  = xk + 0.1
		r: ?None?  = xi - xk + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t11
		a: ?None?  = -0.1*xi + 0.574*xk + 0.0942710120069
		r: ?None?  = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t4:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: 0.909 xi + yi >= 0.3318
	
	_C6: xj <= 0
	
	_C7: 0.091 xi >= -0.1818
	
	_C8: - 0.091 xi >= 0.1818
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t5

### Endogenous Variables

	ignore=1.0
	xi=22.422222
	xj=-41.570429
	xk=-68.506058
	yi=0.0

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: -19.19821 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: 19.77421 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t5
		a: -41.47043 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 41.70343 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742
	t6
		a: -41.47043 = xj + 0.1
		r: 22.70522 = xi + yi + 0.283
		d: 19.77421 = -xi - xj - yi + 0.626
	t7
		a: -19.19821 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: 19.77421 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 22.70522 = xi + yi + 0.283
		d: -21.79622 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t10
		a: -68.40606 = xk + 0.1
		r: 91.21128 = xi - xk + yi + 0.283
		d: -21.79622 = -xi - yi + 0.626
	t11
		a: -41.47043 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 41.70343 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t5:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: 1.009 xi + yi >= 0.3518
	
	_C6: - 0.1 xi - xj + 0.574 xk >= 0.00572898799314
	
	_C7: 0.091 xi - 0.574 xk >= -0.207528987993
	
	_C8: 0.009 xi >= 0.2018
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t6

### Endogenous Variables

	ignore=1.0
	xi=0.2
	xj=0.0
	yi=-0.15

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 0.07148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33300 = -0.009*xi + 0.3348
		d: 0.30452 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.33300 = 0.091*xi + 0.3148
		d: 0.27600 = -0.091*xi + 0.2942
	t5
		a: -39.24821 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 39.68121 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27600 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.33300 = xi + yi + 0.283
		d: 0.57600 = -xi - xj - yi + 0.626
	t7
		a: 0.07148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33300 = -0.009*xi + 0.3348
		d: 0.30452 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.33300 = xi + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.33300 = 0.091*xi + 0.3148
		d: 0.27600 = -0.091*xi + 0.2942
	t10
		a: -68.40606 = xk + 0.1
		r: 68.83906 = xi - xk + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	t11
		a: -39.24821 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 39.68121 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27600 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t6:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: - 0.909 xi - yi >= -0.0318
	
	_C5: 0 xi >= 0
	
	_C6: xj >= 0
	
	_C7: xi + yi >= -0.15
	
	_C8: - xi - xj - yi >= -0.15
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t7

### Endogenous Variables

	ignore=1.0
	xi=-1.6844286
	xj=0.0
	xk=-0.66145264
	yi=0.0

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: -0.11696 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34996 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.16152 = 0.091*xi + 0.3148
		d: 0.44748 = -0.091*xi + 0.2942
	t5
		a: -0.11696 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.56692 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25904 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: -1.40143 = xi + yi + 0.283
		d: 2.31043 = -xi - xj - yi + 0.626
	t7
		a: -0.11696 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34996 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: -1.40143 = xi + yi + 0.283
		d: 2.31043 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.16152 = 0.091*xi + 0.3148
		d: 0.44748 = -0.091*xi + 0.2942
	t10
		a: -0.56145 = xk + 0.1
		r: -0.73998 = xi - xk + yi + 0.283
		d: 2.31043 = -xi - yi + 0.626
	t11
		a: -0.11696 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.56692 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25904 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t7:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: - 1.009 xi - yi >= -0.0518
	
	_C3: 0 xi + 0 xj >= 0
	
	_C4: - 0.909 xi + 0.426 xk - yi >= -0.0575289879931
	
	_C5: 0 xi >= 0
	
	_C6: 0.2 xi + 0.517 xj - 0.574 xk >= 0.042788122273
	
	_C7: - 0.009 xi >= -0.2018
	
	_C8: - 0.091 xi - 0.517 xj >= 0.153282889734
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t8

### Endogenous Variables

	ignore=1.0
	xi=0.0
	xj=0.0
	yi=0.0518

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 0.05148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.32272 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t5
		a: -0.28540 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.72020 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.33480 = xi + yi + 0.283
		d: 0.57420 = -xi - xj - yi + 0.626
	t7
		a: 0.05148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.32272 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.33480 = xi + yi + 0.283
		d: 0.57420 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t10
		a: -0.56145 = xk + 0.1
		r: 0.99625 = xi - xk + yi + 0.283
		d: 0.57420 = -xi - yi + 0.626
	t11
		a: -0.28540 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.72020 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t8:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: - 0.909 xi - yi >= -0.3318
	
	_C6: xj <= 0
	
	_C7: xi + yi >= -0.15
	
	_C8: - xi - yi >= -0.15
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t9

### Endogenous Variables

	ignore=1.0
	xi=-1.9978022
	xj=0.0
	yi=0.0

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: -0.14830 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.50452 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t5
		a: -0.08562 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.53840 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: -1.71480 = xi + yi + 0.283
		d: 2.62380 = -xi - xj - yi + 0.626
	t7
		a: -0.14830 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.35278 = -0.009*xi + 0.3348
		d: 0.50452 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: -1.71480 = xi + yi + 0.283
		d: 2.62380 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.13300 = 0.091*xi + 0.3148
		d: 0.47600 = -0.091*xi + 0.2942
	t10
		a: -0.56145 = xk + 0.1
		r: -1.05335 = xi - xk + yi + 0.283
		d: 2.62380 = -xi - yi + 0.626
	t11
		a: -0.08562 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.53840 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.25622 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t9:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: - 1.009 xi - yi >= -0.0518
	
	_C3: 0 xi + 0 xj >= 0
	
	_C4: - 0.909 xi - yi >= -0.0318
	
	_C5: 0 xi >= 0
	
	_C6: 0.1 xi + 0.517 xj <= 0.0485171102662
	
	_C7: 0.091 xi >= -0.1818
	
	_C8: - 0.091 xi >= 0.1818
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	yi free Continuous
	

##  Solution leading to t10

### Endogenous Variables

	ignore=1.0
	xi=0.051337958
	xj=-0.025499521
	xk=-0.025499521
	yi=0.0

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 0.04343 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33434 = -0.009*xi + 0.3348
		d: 0.33123 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.31947 = 0.091*xi + 0.3148
		d: 0.28953 = -0.091*xi + 0.2942
	t5
		a: 0.07450 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.35984 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27466 = 0.009*xi + 0.2742
	t6
		a: 0.07450 = xj + 0.1
		r: 0.33434 = xi + yi + 0.283
		d: 0.60016 = -xi - xj - yi + 0.626
	t7
		a: 0.04343 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33434 = -0.009*xi + 0.3348
		d: 0.33123 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.33434 = xi + yi + 0.283
		d: 0.57466 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31947 = 0.091*xi + 0.3148
		d: 0.28953 = -0.091*xi + 0.2942
	t10
		a: 0.07450 = xk + 0.1
		r: 0.35984 = xi - xk + yi + 0.283
		d: 0.57466 = -xi - yi + 0.626
	t11
		a: 0.07450 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.35984 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27466 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t10:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: - 1.009 xi - yi >= -0.3518
	
	_C6: - xj + xk >= 0
	
	_C7: xi - xk + yi >= -0.15
	
	_C8: - xi - yi >= -0.15
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t11

### Endogenous Variables

	ignore=1.0
	xi=22.422222
	xj=0.0
	xk=3.9162913
	yi=-22.572222

### Utilties of Terminal Nodes

	t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	t3
		a: 2.29371 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: -1.71771 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t5
		a: 0.10000 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.13300 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.13300 = xi + yi + 0.283
		d: 0.77600 = -xi - xj - yi + 0.626
	t7
		a: 2.29371 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.13300 = -0.009*xi + 0.3348
		d: -1.71771 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.13300 = xi + yi + 0.283
		d: 0.77600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 2.35522 = 0.091*xi + 0.3148
		d: -1.74622 = -0.091*xi + 0.2942
	t10
		a: 4.01629 = xk + 0.1
		r: -3.78329 = xi - xk + yi + 0.283
		d: 0.77600 = -xi - yi + 0.626
	t11
		a: 0.10000 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.13300 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t11:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: - 0.909 xi + 0.426 xk - yi >= -0.0575289879931
	
	_C5: 0 xi >= 0
	
	_C6: - 0.1 xi - xj + 0.574 xk >= 0.00572898799314
	
	_C7: 0.091 xi - 0.574 xk >= -0.207528987993
	
	_C8: 0.009 xi >= 0.2018
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	
## Total Results
11 leaves had at least 1 solution: `['t1', 't10', 't11', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9']`
