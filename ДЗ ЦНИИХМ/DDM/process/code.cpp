// Schwarz without overlapping (Shur complenement Neumann -> Dirichet) 

verbosity=2;
real cpu=clock();
int inside = 2; 
int outside = 1;
border Gamma1(t=1,2){x=t;y=0;label=outside;};
border Gamma2(t=0,1){x=2;y=t;label=outside;};
border Gamma3(t=2,0){x=t ;y=1;label=outside;};

border GammaInside(t=1,0){x = 1-t; y = t;label=inside;};

border GammaArc1(t=1,-2){ x=0; y=t;label=outside;};
border GammaArc2(t=0, 1){ x=t; y=-2;label=outside;};
border GammaArc3(t=-2,0){ x=1; y=t;label=outside;};
int n=4;
mesh Th1 = buildmesh( Gamma1(5*n) + Gamma2(5*n) + GammaInside(5*n) + Gamma3(5*n));
mesh Th2 = buildmesh ( GammaInside(-5*n) + GammaArc1(5*n) +  GammaArc2(5*n) + GammaArc3(5*n));

plot(Th1,Th2);

fespace Vh1(Th1,P1),      Vh2(Th2,P1);
Vh1 u1=0,v1;              Vh2 u2,v2;
Vh1 lambda=0;  // take $\lambda \in V_{h1}$

int i=0;  // for factorization optimization 


problem Pb2(u2,v2,init=i,solver=Cholesky) = 
    int2d(Th2)( dx(u2)*dx(v2)+dy(u2)*dy(v2) )
  + int2d(Th2)( -v2) 
  + int1d(Th2,inside)(-lambda*v2)
  + on(outside,u2= 0 ) ;
problem Pb1(u1,v1,init=i,solver=Cholesky) = 
    int2d(Th1)( dx(u1)*dx(v1)+dy(u1)*dy(v1) )
  + int2d(Th1)( -v1) 
  + int1d(Th1,inside)(+lambda*v1) +    on(outside,u1 = 0 ) ;

varf b(u2,v2,solver=CG) =int1d(Th1,inside)(u2*v2);
matrix B= b(Vh1,Vh1,solver=CG);

//  $\lambda \longrightarrow  \int_{\Gamma_i }(u_1-u_2) v_{1}$
func real[int] BoundaryProblem(real[int] &l)
{ 
   lambda[]=l;
   Pb1; 
   Pb2;
   i++;
   v1=-(u1-u2); 
   lambda[]=B*v1[];
   return lambda[] ;
};

Vh1 p=0,q=0;

//  solve the problem with Conjugue Gradient
LinearCG(BoundaryProblem,p[],q[],eps=1.e-6,nbiter=100);

//  compute the final solution, because CG works with increment
BoundaryProblem(p[]); // solve again  to have right u1,u2
cout << " -- CPU time  schwarz-gc:" <<  clock()-cpu << endl;

plot(u1,u2);

