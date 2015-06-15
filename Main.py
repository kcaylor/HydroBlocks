import os
Parallel = False#True 
njobs = 1#800#80000#5000#8000#800#400
ncores = 32
mpi_type = 'mpirun'#'ibrun'

if Parallel == True:
 
 #Run the model using MPI (w/OMP)
 #os.system('aprun -n %d -d %d python Driver.py parallel' % (njobs,ncores))
 if mpi_type == 'ibrun':
  os.system('ibrun python Driver.py parallel')
 if mpi_type == 'mpirun':
  os.system('mpirun -n %d python Driver.py parallel' % njobs*ncores)

elif Parallel == False:

 #Run the model without MPI (w/OMP)
 os.system('python Driver.py serial')
