'''
* Amdahl's Law:
- S: speed of parallelism -> (1 - S): speed of sequential
T1 = S + (1 - S) = 1

- Using p processors to speed up the sequential part
Tp = S + (1 - S) / p

- Then we have the speedup using p processors
(T1 / Tp) = 1 / [S + (1 - S) / p]
(T1 / Tp) < 1 / S
'''
