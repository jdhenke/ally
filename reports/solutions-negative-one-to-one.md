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
	xi=-0.85
	xj=-1.0
	xk=-1.0
	yi=1.0

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
		a: -0.55052 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34245 = -0.009*xi + 0.3348
		d: 0.91707 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.23745 = 0.091*xi + 0.3148
		d: 0.37155 = -0.091*xi + 0.2942
	t5
		a: -0.39473 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.83718 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41267 = 0.009*xi + 0.420318
	t6
		a: -0.90000 = xj + 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 1.47600 = -xi - xj - yi + 0.626
	t7
		a: -0.55052 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34245 = -0.009*xi + 0.3348
		d: 0.91707 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.43300 = xi + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.23745 = 0.091*xi + 0.3148
		d: 0.37155 = -0.091*xi + 0.2942
	t10
		a: -0.90000 = xk + 0.1
		r: 1.43300 = xi - xk + yi + 0.283
		d: 0.47600 = -xi - yi + 0.626
	t11
		a: -0.39473 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.83718 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41267 = 0.009*xi + 0.420318

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
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t2

### Endogenous Variables

	ignore=1.0
	xi=-0.7872329
	xj=-1.0
	xk=0.53257345
	yi=1.0

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
		a: -0.54424 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34189 = -0.009*xi + 0.3348
		d: 0.91136 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.24316 = 0.091*xi + 0.3148
		d: 0.36584 = -0.091*xi + 0.2942
	t5
		a: 0.47869 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: -0.03681 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41323 = 0.009*xi + 0.420318
	t6
		a: -0.90000 = xj + 0.1
		r: 0.49577 = xi + yi + 0.283
		d: 1.41323 = -xi - xj - yi + 0.626
	t7
		a: -0.54424 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34189 = -0.009*xi + 0.3348
		d: 0.91136 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.49577 = xi + yi + 0.283
		d: 0.41323 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.24316 = 0.091*xi + 0.3148
		d: 0.36584 = -0.091*xi + 0.2942
	t10
		a: 0.63257 = xk + 0.1
		r: -0.03681 = xi - xk + yi + 0.283
		d: 0.41323 = -xi - yi + 0.626
	t11
		a: 0.47869 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: -0.03681 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41323 = 0.009*xi + 0.420318

### Linear Program Information

	LP Leading to t2:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: 1.009 xi + yi >= 0.205682
	
	_C6: - 0.1 xi - xj + 0.574 xk >= 0.00572898799314
	
	_C7: 0.091 xi - 0.574 xk <= -0.207528987993
	
	_C8: xi <= 1
	
	_C9: xi >= -1
	
	_C10: xj <= 1
	
	_C11: xj >= -1
	
	_C12: xk <= 1
	
	_C13: xk >= -1
	
	_C14: yi <= 1
	
	_C15: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t3

### Endogenous Variables

	ignore=1.0
	xi=-0.67175352
	xj=-0.17824648
	xk=-1.0
	yi=1.0

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
		a: -0.10785 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34085 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.25367 = 0.091*xi + 0.3148
		d: 0.35533 = -0.091*xi + 0.2942
	t5
		a: -0.41255 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.85340 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41427 = 0.009*xi + 0.420318
	t6
		a: -0.07825 = xj + 0.1
		r: 0.61125 = xi + yi + 0.283
		d: 0.47600 = -xi - xj - yi + 0.626
	t7
		a: -0.10785 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34085 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.61125 = xi + yi + 0.283
		d: 0.29775 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.25367 = 0.091*xi + 0.3148
		d: 0.35533 = -0.091*xi + 0.2942
	t10
		a: -0.90000 = xk + 0.1
		r: 1.61125 = xi - xk + yi + 0.283
		d: 0.29775 = -xi - yi + 0.626
	t11
		a: -0.41255 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.85340 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41427 = 0.009*xi + 0.420318

### Linear Program Information

	LP Leading to t3:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: 0.909 xi + 0.483 xj + yi >= 0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: 1.009 xi + yi >= 0.205682
	
	_C6: 0.2 xi + 0.517 xj - 0.574 xk >= 0.042788122273
	
	_C7: - 0.009 xi >= -0.2018
	
	_C8: - 0.091 xi - 0.517 xj >= 0.153282889734
	
	_C9: xi <= 1
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
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
	xk=-1.0
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
		a: -0.49973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.93273 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42212 = 0.009*xi + 0.420318
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
		a: -0.90000 = xk + 0.1
		r: 1.33300 = xi - xk + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	t11
		a: -0.49973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.93273 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42212 = 0.009*xi + 0.420318

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
	
	_C9: xi <= 1
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t7

### Endogenous Variables

	ignore=1.0
	xi=-1.0
	xj=-0.12047002
	xk=-0.53148275
	yi=-1.0

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
		a: -0.11080 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34380 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.22380 = 0.091*xi + 0.3148
		d: 0.38520 = -0.091*xi + 0.2942
	t5
		a: -0.11080 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.55460 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41132 = 0.009*xi + 0.420318
	t6
		a: -0.02047 = xj + 0.1
		r: -1.71700 = xi + yi + 0.283
		d: 2.74647 = -xi - xj - yi + 0.626
	t7
		a: -0.11080 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.34380 = -0.009*xi + 0.3348
		d: 0.47600 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: -1.71700 = xi + yi + 0.283
		d: 2.62600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.22380 = 0.091*xi + 0.3148
		d: 0.38520 = -0.091*xi + 0.2942
	t10
		a: -0.43148 = xk + 0.1
		r: -1.18552 = xi - xk + yi + 0.283
		d: 2.62600 = -xi - yi + 0.626
	t11
		a: -0.11080 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.55460 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.41132 = 0.009*xi + 0.420318

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
	
	_C9: xi <= 1
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t8

### Endogenous Variables

	ignore=1.0
	xi=0.2
	xj=-1.0
	xk=-1.0
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
		a: -0.44552 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33300 = -0.009*xi + 0.3348
		d: 0.82152 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.33300 = 0.091*xi + 0.3148
		d: 0.27600 = -0.091*xi + 0.2942
	t5
		a: -0.49973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.93273 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42212 = 0.009*xi + 0.420318
	t6
		a: -0.90000 = xj + 0.1
		r: 0.33300 = xi + yi + 0.283
		d: 1.57600 = -xi - xj - yi + 0.626
	t7
		a: -0.44552 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.33300 = -0.009*xi + 0.3348
		d: 0.82152 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.33300 = xi + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.33300 = 0.091*xi + 0.3148
		d: 0.27600 = -0.091*xi + 0.2942
	t10
		a: -0.90000 = xk + 0.1
		r: 1.33300 = xi - xk + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	t11
		a: -0.49973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.93273 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42212 = 0.009*xi + 0.420318

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
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to t10

### Endogenous Variables

	ignore=1.0
	xi=1.0
	xj=-1.0
	xk=-1.0
	yi=-0.9572

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
		a: -0.36552 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.32580 = -0.009*xi + 0.3348
		d: 0.74872 = -0.091*xi - 0.517*xj + 0.322717110266
	t4
		a: 0.10000 = 0.1
		r: 0.40580 = 0.091*xi + 0.3148
		d: 0.20320 = -0.091*xi + 0.2942
	t5
		a: -0.57973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 1.00553 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42932 = 0.009*xi + 0.420318
	t6
		a: -0.90000 = xj + 0.1
		r: 0.32580 = xi + yi + 0.283
		d: 1.58320 = -xi - xj - yi + 0.626
	t7
		a: -0.36552 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.32580 = -0.009*xi + 0.3348
		d: 0.74872 = -0.091*xi - 0.517*xj + 0.322717110266
	t8
		a: 0.10000 = 0.1
		r: 0.32580 = xi + yi + 0.283
		d: 0.58320 = -xi - yi + 0.626
	t9
		a: 0.10000 = 0.1
		r: 0.40580 = 0.091*xi + 0.3148
		d: 0.20320 = -0.091*xi + 0.2942
	t10
		a: -0.90000 = xk + 0.1
		r: 1.32580 = xi - xk + yi + 0.283
		d: 0.58320 = -xi - yi + 0.626
	t11
		a: -0.57973 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 1.00553 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42932 = 0.009*xi + 0.420318

### Linear Program Information

	LP Leading to t10:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: - 1.009 xi - yi >= -0.205682
	
	_C6: - xj + xk >= 0
	
	_C7: xi - xk + yi >= -0.15
	
	_C8: - xi - yi >= -0.15
	
	_C9: xi <= 1
	
	_C10: xi >= -1
	
	_C11: xj <= 1
	
	_C12: xj >= -1
	
	_C13: xk <= 1
	
	_C14: xk >= -1
	
	_C15: yi <= 1
	
	_C16: yi >= -1
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	
## Total Results
7 leaves had at least 1 solution: `['t1', 't10', 't2', 't3', 't6', 't7', 't8']`
