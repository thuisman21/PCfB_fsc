//Number of population samples (demes)
4 populations to simulate
//Population effective sizes (number of genes)
N_POP0
N_POP1
N_POP2
N_POP3
//Sample sizes
12
12
12
12
//Growth rates
0
0
0
0
//Number of migration matrices
4
//Migration matrix 0
0.000 MIG01 0.000 0.000
MIG10 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
//Migration matrix 1
0.000 MIG1A 0.000 0.000
MIGA1 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
//Migration matrix 2
0.000 0.000 MIGA2 0.000
0.000 0.000 0.000 0.000
MIG2A 0.000 0.000 0.000
0.000 0.000 0.000 0.000
//Migration matrix 3
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
//historical event: time, source, sink, migrants, new deme size, growth rate, migr mat index
3 historical event
TDIV32 3 2 1 RELANC32 0 1
TDIV02 1 2 1 RELANC02 0 2
TDIV1_ANC02 0 2 1 RELANC12 0 3
//Number of independent loci [chromosomes]
1  0
//Per chromosome: Number of linkage blocks
1
//per block: Datatype, numm loci, rec rate and mut rate + optional parameters
FREQ 1  0 2.49e-8 OUTEXP