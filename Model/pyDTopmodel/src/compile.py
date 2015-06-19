import os
#cmd = 'f2py dynamic_topmodel_tools.f90 -h dynamic_topmodel_tools.pyf -m dynamic_topmodel_tools --overwrite-signature'
#os.system(cmd)
#Create driver library
#cmd = 'f2py dynamic_topmodel_tools.f90 -L/u/sciteam/nchaney/local/lib -lgomp -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -fopenmp -O3 -funroll-loops"'
#cmd = 'f2py dynamic_topmodel_tools.f90 -L/u/sciteam/nchaney/local/lib -lopenblas -lgomp -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -fopenmp -O3 -funroll-loops -ffast-math"'
#cmd = 'f2py dynamic_topmodel_tools.f90 -lgomp -liomp5 -lmkl_rt -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -Ofast -funroll-loops -ffast-math -m64 -Wl,--no-as-needed -openmp -fopenmp"'
cmd = 'f2py --debug dynamic_topmodel_tools.f90 -lgomp -liomp5 -lmkl_rt -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -O3 -funroll-loops -m64 -Wl,--no-as-needed -openmp -fopenmp -g -fbacktrace"'
#cmd = 'gfortran dynamic_topmodel_tools.f90 -L/opt/intel/composer_xe_2013_sp1.2.144/mkl/lib/intel64 -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -L/opt/intel/composer_xe_2013_sp1.2.144/mkl/../compiler/lib/intel64 -liomp5 -lpthread -lm -ldl -w -fno-second-underscore -fcray-pointer -x f77-cpp-input -ffree-form -I/opt/intel/composer_xe_2013_sp1.2.144/mkl/include'
#os.system(cmd)
#cmd = 'f2py --debug dynamic_topmodel_tools.f90 -L"/opt/intel/composer_xe_2013_sp1.2.144/mkl/lib/intel64" -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -L"/opt/intel/composer_xe_2013_sp1.2.144/mkl/../compiler/lib/intel64" -liomp5 -lpthread -lm -ldl -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -fno-second-underscore -fcray-pointer -x f77-cpp-input -ffree-form -I/opt/intel/composer_xe_2013_sp1.2.144/mkl/include"'
#cmd = 'f2py --debug dynamic_topmodel_tools.f90 -ldl -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -O3 -funroll-loops -openmp -fopenmp -g -fbacktrace -m64 -Wl,--no-as-needed"'
#cmd = 'f2py dynamic_topmodel_tools.f90 -lgomp -liomp5 -lmkl_rt -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -O3 -funroll-loops -ffast-math -m64 -Wl,--no-as-needed -openmp -fopenmp"'
#cmd = 'f2py dynamic_topmodel_tools.f90 -lmkl_rt -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=intelem --f90flags="-fast -xHost -axAVX -opt-prefetch -ipo"'
#cmd = 'f2py dynamic_topmodel_tools.f90 -lmkl_rt -lpthread -lm -liomp5 -c dynamic_topmodel_tools.pyf --fcompiler=intelem --f90flags="-fast -xHost -axAVX -opt-prefetch -ipoi -openmp"'
#cmd = 'f2py dynamic_topmodel_tools.f90 /u/sciteam/nchaney/intel/composer_xe_2013_sp1/mkl/lib/intel64/libmkl_intel_ilp64.a /u/sciteam/nchaney/intel/composer_xe_2013_sp1/mkl/lib/intel64/libmkl_core.a /u/sciteam/nchaney/intel/composer_xe_2013_sp1/mkl/lib/intel64/libmkl_sequential.a -lpthread -lm -liomp5 -c dynamic_topmodel_tools.pyf --fcompiler=intelem --f90flags="-fast -xHost -axAVX -opt-prefetch -ipoi -openmp"'
#cmd = 'f2py dynamic_topmodel_tools.f90  -Wl,--start-group /u/sciteam/nchaney/intel/mkl/lib/intel64/libmkl_gf_ilp64.a /u/sciteam/nchaney/intel/mkl/lib/intel64/libmkl_core.a /u/sciteam/nchaney/intel/mkl/lib/intel64/libmkl_gnu_thread.a -Wl,--end-group -ldl -lpthread -lm -c dynamic_topmodel_tools.pyf --fcompiler=gnu95 --f90flags="-w -fopenmp -O3 -funroll-loops -ffast-math -m64 -I/u/sciteam/nchaney/intel/mkl/include"'
os.system(cmd)
#Move to the previous directory
os.system('mv dynamic_topmodel_tools.so ../.')
