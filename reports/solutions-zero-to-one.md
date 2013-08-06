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
	xj=0.0
	xk=0.0
	yi=0.15

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
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 0.47600 = -xi - xj - yi + 0.626
	t7
		a: 0.05148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.32272 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t10
		a: 0.10000 = xk + 0.1
		r: 0.43300 = xi - xk + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t11
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
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
	
	_C9: xi <= 1
	
	_C10: xi >= 0
	
	_C11: xj <= 1
	
	_C12: xj >= 0
	
	_C13: xk <= 1
	
	_C14: xk >= 0
	
	_C15: yi <= 1
	
	_C16: yi >= 0
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t2

### Endogenous Variables

	ignore=1.0
	xi=0.051337958
	xj=0.0
	xk=1.0
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
		a: 0.05662 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33434 = -0.009*xi + 0.3348
		d: 0.31805 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.31947 = 0.091*xi + 0.3148
		d: 0.28953 = -0.091*xi + 0.2942
	t5
		a: 0.66314 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: -0.22880 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27466 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.33434 = xi + yi + 0.283
		d: 0.57466 = -xi - xj - yi + 0.626
	t7
		a: 0.05662 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33434 = -0.009*xi + 0.3348
		d: 0.31805 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.33434 = xi + yi + 0.283
		d: 0.57466 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31947 = 0.091*xi + 0.3148
		d: 0.28953 = -0.091*xi + 0.2942
	t10
		a: 1.10000 = xk + 0.1
		r: -0.66566 = xi - xk + yi + 0.283
		d: 0.57466 = -xi - yi + 0.626
	t11
		a: 0.66314 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: -0.22880 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27466 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t2:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: - 0.909 xi + 0.426 xk - yi >= -0.0575289879931
	
	_C5: 0 xi >= 0
	
	_C6: - 0.1 xi - xj + 0.574 xk >= 0.00572898799314
	
	_C7: 0.091 xi - 0.574 xk <= -0.207528987993
	
	_C8: xi <= 1
	
	_C9: xi >= 0
	
	_C10: xj <= 1
	
	_C11: xj >= 0
	
	_C12: xk <= 1
	
	_C13: xk >= 0
	
	_C14: yi <= 1
	
	_C15: yi >= 0
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t6

### Endogenous Variables

	ignore=1.0
	xi=0.0
	xj=0.0
	xk=0.0
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
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
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
		a: 0.10000 = xk + 0.1
		r: 0.33480 = xi - xk + yi + 0.283
		d: 0.57420 = -xi - yi + 0.626
	t11
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742

### Linear Program Information

	LP Leading to t6:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi + yi >= 0.0318
	
	_C5: - 0.909 xi - yi >= -0.3318
	
	_C6: xj >= 0
	
	_C7: xi + yi >= -0.15
	
	_C8: - xi - xj - yi >= -0.15
	
	_C9: xi <= 1
	
	_C10: xi >= 0
	
	_C11: xj <= 1
	
	_C12: xj >= 0
	
	_C13: xk <= 1
	
	_C14: xk >= 0
	
	_C15: yi <= 1
	
	_C16: yi >= 0
	
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
	xk=0.0
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
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
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
		a: 0.10000 = xk + 0.1
		r: 0.33480 = xi - xk + yi + 0.283
		d: 0.57420 = -xi - yi + 0.626
	t11
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
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
	
	_C9: xi <= 1
	
	_C10: xi >= 0
	
	_C11: xj <= 1
	
	_C12: xj >= 0
	
	_C13: xk <= 1
	
	_C14: xk >= 0
	
	_C15: yi <= 1
	
	_C16: yi >= 0
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t10

### Endogenous Variables

	ignore=1.0
	xi=0.0
	xj=0.0
	xk=0.0
	yi=0.057529

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
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742
	t6
		a: 0.10000 = xj + 0.1
		r: 0.34053 = xi + yi + 0.283
		d: 0.56847 = -xi - xj - yi + 0.626
	t7
		a: 0.05148 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33480 = -0.009*xi + 0.3348
		d: 0.32272 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.34053 = xi + yi + 0.283
		d: 0.56847 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.31480 = 0.091*xi + 0.3148
		d: 0.29420 = -0.091*xi + 0.2942
	t10
		a: 0.10000 = xk + 0.1
		r: 0.34053 = xi - xk + yi + 0.283
		d: 0.56847 = -xi - yi + 0.626
	t11
		a: 0.09427 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.34053 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.27420 = 0.009*xi + 0.2742

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
	
	_C9: xi <= 1
	
	_C10: xi >= 0
	
	_C11: xj <= 1
	
	_C12: xj >= 0
	
	_C13: xk <= 1
	
	_C14: xk >= 0
	
	_C15: yi <= 1
	
	_C16: yi >= 0
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	
## Total Results
5 leaves had at least 1 solution: `['t1', 't10', 't2', 't6', 't8']`
