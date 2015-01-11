# PST
python project for calculating bandwidth utilization

To run project you need .dat file of specific structure:
N=3;
K=12;
Q=10;
ro=0.1;
alfa=1.4;
u=0.6;
delta=0.5;
r=[0.5 0.75 0.875 0.93775 0.96 0.975 0.983 0.99 0.996 1];
r2=[0 0.5 0.75 0.875 0.93775 0.96 0.975 0.983 0.99 0.996];
omega=[0.1 0.2 0.2 0.1 0.05 0.05 0.1 0.25 0.1 0.1 ];

Program takes N, K, Q, ro, alfa, u and delta as mandatory parameters, so you can't ommit them.
To run the program simply run from command line:

python main.py /path/to/your/dat/file.dat
