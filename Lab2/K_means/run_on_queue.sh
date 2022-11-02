#!/bin/bash

## Give the Job a descriptive name
#PBS -N run_kmeans

## Output and error files
#PBS -o run_kmeans_reduction.out
#PBS -e run_kmeans_reduction.err

## How many machines should we get? 
#PBS -l nodes=1:ppn=64

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder (modify properly)

module load openmp
cd /home/parallel/parlab14/K_means
####./kmeans_seq -s 256 -n 16 -c 16 -l 10
for threads in 1 2 4 8 16 32 64
do
	export OMP_NUM_THREADS=$threads
	export GOMP_CPU_AFFINITY="0-${threads}"
	./kmeans_omp_reduction -s 256 -n 1 -c 4 -l 10
done
