# Solutions to Cooley's Game

## Intro

Sup B. Here are my findings.

Basically, you can arrive at any terminal node from the top. 
I formulated the entire thing as a linear program, case you're interested.
I'm not sure how what this means for your model, but it could also definitely be my implementation.
Fortunately, there is a really easy/terrible way to check this hypothesis: **manually check the answers I got.**
I love helping you out bud, but really not feeling like crunching these numbers by hand, but I figured I'd share them with you if you want to do so yourself.

Below I list the

  - exogenous variables I used and their values
  - each solution i found leading to each of the terminal nodes, named per your PDF
    - note: these are just one solution of many I found per node
  - the actual code from my program which plugs in the equations

Bottom line, I think you should double check these results and my equations to confirm that the model you proposed can't be decided just given exogenous variables.
I think of this as a proof by contradiction :-)
    
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

##  Solution leading to terminal node t1

### Here are the values of the endogenous variables

	ignore=1.0
	xi=0.0
	xj=-0.059041408
	yi=0.3318

### Here are the utilities of each actor at each terminal node

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
		d: 0.42032 = 0.009*xi + 0.420318
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
		d: 0.42032 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t2

### Here are the values of the endogenous variables

	ignore=1.0
	xi=-1.9978022
	xj=0.0
	yi=1.8478022

### Here are the utilities of each actor at each terminal node

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
		d: 0.40234 = 0.009*xi + 0.420318
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
		d: 0.40234 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t3

### Here are the values of the endogenous variables

	ignore=1.0
	xi=22.422222
	xj=-4.2431436
	yi=-18.029079

### Here are the utilities of each actor at each terminal node

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
		d: 0.62212 = 0.009*xi + 0.420318
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
		d: 0.62212 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t4

### Here are the values of the endogenous variables

	ignore=1.0
	xi=-1.9978022
	xj=-0.059041408
	yi=2.1478022

### Here are the utilities of each actor at each terminal node

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
		d: 0.40234 = 0.009*xi + 0.420318
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
		d: 0.40234 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t5

### Here are the values of the endogenous variables

	ignore=1.0
	xi=6.1868889
	xj=-11.015733
	xk=-18.103336
	yi=0.0

### Here are the utilities of each actor at each terminal node

	 t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	 t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	 t3
		a: -5.02496 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.27912 = -0.009*xi + 0.3348
		d: 5.45484 = -0.091*xi - 0.517*xj + 0.322717110266
	 t4
		a: 0.10000 = 0.1
		r: 0.87781 = 0.091*xi + 0.3148
		d: -0.26881 = -0.091*xi + 0.2942
	 t5
		a: -10.91573 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 11.29485 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.420318
	 t6
		a: -10.91573 = xj + 0.1
		r: 6.46989 = xi + yi + 0.283
		d: 5.45484 = -xi - xj - yi + 0.626
	 t7
		a: -5.02496 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.27912 = -0.009*xi + 0.3348
		d: 5.45484 = -0.091*xi - 0.517*xj + 0.322717110266
	 t8
		a: 0.10000 = 0.1
		r: 6.46989 = xi + yi + 0.283
		d: -5.56089 = -xi - yi + 0.626
	 t9
		a: 0.10000 = 0.1
		r: 0.87781 = 0.091*xi + 0.3148
		d: -0.26881 = -0.091*xi + 0.2942
	 t10
		a: -18.00334 = xk + 0.1
		r: 24.57322 = xi - xk + yi + 0.283
		d: -5.56089 = -xi - yi + 0.626
	 t11
		a: -10.91573 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 11.29485 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

	LP Leading to t5:
	MAXIMIZE
	1*ignore + 0
	SUBJECT TO
	_C1: ignore = 1
	
	_C2: 1.009 xi + yi >= 0.0518
	
	_C3: - 0.909 xi - 0.483 xj - yi >= -0.303282889734
	
	_C4: 0.909 xi - 0.426 xk + yi >= 0.0575289879931
	
	_C5: 1.009 xi + yi >= 0.205682
	
	_C6: - 0.1 xi - xj + 0.574 xk >= 0.00572898799314
	
	_C7: 0.091 xi - 0.574 xk >= -0.207528987993
	
	_C8: 0.009 xi >= 0.055682
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to terminal node t6

### Here are the values of the endogenous variables

	ignore=1.0
	xi=0.2
	xj=0.0
	yi=-0.15

### Here are the utilities of each actor at each terminal node

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
		a: -10.31704 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 10.75004 = 0.091*xi - 0.574*xk + 0.340528987993
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
		a: -18.00334 = xk + 0.1
		r: 18.43634 = xi - xk + yi + 0.283
		d: 0.57600 = -xi - yi + 0.626
	 t11
		a: -10.31704 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 10.75004 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.42212 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t7

### Here are the values of the endogenous variables

	ignore=1.0
	xi=-1.6844286
	xj=0.0
	xk=-0.66145264
	yi=0.0

### Here are the utilities of each actor at each terminal node

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
		d: 0.40516 = 0.009*xi + 0.420318
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
		d: 0.40516 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t8

### Here are the values of the endogenous variables

	ignore=1.0
	xi=0.0
	xj=0.0
	yi=0.0518

### Here are the utilities of each actor at each terminal node

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
		d: 0.42032 = 0.009*xi + 0.420318
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
		d: 0.42032 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t9

### Here are the values of the endogenous variables

	ignore=1.0
	xi=-1.9978022
	xj=0.0
	yi=0.0

### Here are the utilities of each actor at each terminal node

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
		d: 0.40234 = 0.009*xi + 0.420318
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
		d: 0.40234 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	

##  Solution leading to terminal node t10

### Here are the values of the endogenous variables

	ignore=1.0
	xi=0.051337958
	xj=-0.025499521
	xk=-0.025499521
	yi=0.0

### Here are the utilities of each actor at each terminal node

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
		d: 0.42078 = 0.009*xi + 0.420318
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
		d: 0.42078 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

##  Solution leading to terminal node t11

### Here are the values of the endogenous variables

	ignore=1.0
	xi=6.1868889
	xj=0.0
	xk=1.342397
	yi=-6.1907709

### Here are the utilities of each actor at each terminal node

	 t1
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	 t2
		a: 0.10000 = 0.1
		r: 0.13300 = 0.133
		d: 0.47600 = 0.476
	 t3
		a: 0.67017 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.27912 = -0.009*xi + 0.3348
		d: -0.24029 = -0.091*xi - 0.517*xj + 0.322717110266
	 t4
		a: 0.10000 = 0.1
		r: 0.87781 = 0.091*xi + 0.3148
		d: -0.26881 = -0.091*xi + 0.2942
	 t5
		a: 0.24612 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.13300 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.420318
	 t6
		a: 0.10000 = xj + 0.1
		r: 0.27912 = xi + yi + 0.283
		d: 0.62988 = -xi - xj - yi + 0.626
	 t7
		a: 0.67017 = 0.1*xi + 0.517*xj + 0.0514828897338
		r: 0.27912 = -0.009*xi + 0.3348
		d: -0.24029 = -0.091*xi - 0.517*xj + 0.322717110266
	 t8
		a: 0.10000 = 0.1
		r: 0.27912 = xi + yi + 0.283
		d: 0.62988 = -xi - yi + 0.626
	 t9
		a: 0.10000 = 0.1
		r: 0.87781 = 0.091*xi + 0.3148
		d: -0.26881 = -0.091*xi + 0.2942
	 t10
		a: 1.44240 = xk + 0.1
		r: -1.06328 = xi - xk + yi + 0.283
		d: 0.62988 = -xi - yi + 0.626
	 t11
		a: 0.24612 = -0.1*xi + 0.574*xk + 0.0942710120069
		r: 0.13300 = 0.091*xi - 0.574*xk + 0.340528987993
		d: 0.47600 = 0.009*xi + 0.420318

### Here is information about the linear program that was formulated

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
	
	_C8: 0.009 xi >= 0.055682
	
	VARIABLES
	ignore free Continuous
	xi free Continuous
	xj free Continuous
	xk free Continuous
	yi free Continuous
	

## Here's the actual equations in my code
```python

    pd1 = .626
    pr1 = .283
    pa = .1
    pd2 = .426
    pr2 = .483
    k = .15
    
    ba=pa
    bd=pd1
    br=pr1

    xi = LpVariable("xi")
    xj = LpVariable("xj")
    xk = LpVariable("xk")
    yi = LpVariable("yi")

    t6 = TerminalNode("t6", {
        "d": bd - xi - xj - yi,
        "r": br + xi + yi,
        "a": ba + xj,
    })

    t7 = TerminalNode("t7", {
        "d": (bd-xi-xj)+(pd2+pa)*(br+xi)*(pd2/(pd2+pa))-pr2*(bd-xi-xj)-k*(pd2/(pd2+pa)),
        "r": (br+xi)+pr2*(bd-xi+ba)-(pd2+pa)*(br+xi)-k,
        "a": (ba+xj)+(pd2+pa)*(br+xi)*(pa/(pd2+pa))-pr2*(ba+xj)-k*(pa/(pd2+pa)),
    })

    r1 = FolderNode((t6, t7), lambda x: x.utilities["r"])

    t3 = TerminalNode("t3", {
        "d": (bd-xi-xj)+(pd2+pa)*(br+xi)*(pd2/(pd2+pa))-pr2*(bd-xi-xj)-k*(pd2/(pd2+pa)),
        "r": (br+xi)+pr2*(bd-xi+ba)-(pd2+pa)*(br+xi)-k,
        "a": (ba+xj)+(pd2+pa)*(br+xi)*(pa/(pd2+pa))-pr2*(ba+xj)-k*(pa/(pd2+pa)),
    })

    d1 = FolderNode((r1, t3), lambda x: x.utilities["d"])

    t8 = TerminalNode("t8", {
        "d": bd-xi-yi,
        "r": br+xi+yi,
        "a": ba,
    })

    t9 = TerminalNode("t9", {
        "d": (bd-xi)+pd2*(br+xi)-pr2*(bd-xi)-k,
        "r": (br+xi)+pr2*(bd-xi)-pd2*(br+xi)-k,
        "a": ba,
    })

    r2 = FolderNode((t8, t9), lambda x: x.utilities["r"])

    t4 = TerminalNode("t4", {
        "d": (bd - xi)+pd2*(br+xi)-pr2*(bd-xi)-k,
        "r": (br+xi)+pr2*(bd-xi)-pd2*(br+xi)-k,
        "a": ba,
    })

    d2 = FolderNode((r2, t4), lambda x: x.utilities["d"])

    t10 = TerminalNode("t10", {
        "d": bd - xi-yi,
        "r": br+xi-xk+yi,
        "a": ba+xk,
    })

    t11 = TerminalNode("t11", {
        "d": (bd-xi)+pd2*(bd+xi+ba)-(pr2+pa)*(bd-xi)-k,
        "r": (br+xi-xk)+(pr2+pa)*(bd-xi)*(pr2/(pr2+pa))-pd2*(br+xi-xk)-k*(pr2/(pr2+pa)),
        "a": (ba+xk)+(pr2+pa)*(bd-xi)*(pa/(pr2+pa))-pd2*(ba+xk)-k*(pa/(pr2+pa)),
    })

    r3 = FolderNode((t10, t11), lambda x: x.utilities["r"])

    t5 = TerminalNode("t5", {
        "d": (bd-xi)+pd2*(bd+xi+ba)-(pr2+pa)*(bd-xi)-k,
        "r": (br+xi-xk)+(pr2+pa)*(bd-xi)*(pr2/(pr2+pa))-pd2*(br+xi-xk)-k*(pr2/(pr2+pa)),
        "a": (ba+xk)+(pr2+pa)*(bd-xi)*(pa/(pr2+pa))-pd2*(ba+xk)-k*(pa/(pr2+pa)),
    })

    d3 = FolderNode((r3, t5), lambda x: x.utilities["d"])

    a0 = FolderNode((d1,d2,d3), lambda x: x.utilities["a"])

    t2 = TerminalNode("t2", {
        "d": bd+pd1*br-pr1*bd-k,
        "r": br+pr1*bd-pd1*br-k,
        "a": ba,
    })

    r0 = FolderNode((a0, t2), lambda x: x.utilities["r"])

    t1 = TerminalNode("t1", {
        "d": bd+pd1*br-pr1*bd-k,
        "r": br+pr1*bd-pd1*br-k,
        "a": ba,
    })

```
