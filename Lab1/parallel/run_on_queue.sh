#!/bin/bash

## Give the Job a descriptive name
#PBS -N Game_Of_Life_1

## Output and error files
#PBS -o run_omp_GOL.out
#PBS -e run_omp_GOL.err

## How many machines should we get? 
#PBS -l nodes=1:ppn=8

##How long should the job run for?
#PBS -l walltime=01:00:00

## Start 
## Run make in the src folder (modify properly)

module load openmp
cd /home/parallel/parlab14/GOL/

for threads in 1 2 4 6 8
do 

	export OMP_NUM_THREADS=$threads
	./Game_Of_Life 64 1000
	./Game_Of_Life 1024 1000
	./Game_Of_Life 4096 1000

done

##export OMP_NUM_THREADS=8
##./Game_Of_Life 64 1000
