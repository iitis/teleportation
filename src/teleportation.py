from hamiltonian import *
                                #this file describes  the quantum teleportation protocol

#the operator Unm is the generator defined in the paper, Eq. 3
def u(n,m):
    d=4
    op=sum(np.exp(2*np.pi*1j*k*n/d)*(fock(d,k)*fock(d,(k+m)%d).dag()) for k in range(d))
    return op

#this function calculates the fidelity of the teleportation defined via Eq. 9 in the paper
def teleportation(L,J,mu,w,U):
    d=4
    psi=sum(tensor(fock(d,r),fock(d,r)) for r in range(0,d))/np.sqrt(d) # maximaly entangled state \psi^+
    #psi=(tensor(basis(4,0), basis(4,3))+tensor(basis(4,3), basis(4,0))+tensor(basis(4,1), basis(4,2))+tensor(basis(4,2), basis(4,1)))/2 #hubbard state
    r_in=ket2dm(sum(fock(d,r) for r in range(d)).unit()) # the state to teleporte (density matrix of 1 ququart)
    state=sum(sum(((tensor(u(n,m),identity(d))*psi*psi.dag()*tensor(u(n,m),identity(d)).dag()*two_site_density_matrix(L,J,U,mu,w)).tr())*u(n,-m)*r_in*u(n,-m).dag()
                  for n in range(d)) for m in range(d)) #output state
    return fidelity(r_in,state)**2