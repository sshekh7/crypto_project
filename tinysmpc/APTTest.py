from tinysmpc import VirtualMachine, PrivateScalar, SharedScalar
from tinysmpc.fixed_point import fixed_point, float_point
from tinysmpc.finite_ring import MAX_INT64, MIN_INT64
from tinysmpc.secret_sharing import Share



#virtual machines
alice = VirtualMachine('alice')
bob = VirtualMachine('bob')
charlie = VirtualMachine('charlie')


#additon and multiplication of SharedScalar
a = PrivateScalar(19, alice)
b = PrivateScalar(12, bob)
c = PrivateScalar(4, charlie)

# Our target is (a*b)+c 
# Currently uses shared sharing, need to change this to elgamal later

#sharing the generated values
a_shared = a.share([alice, bob, charlie])
b_shared = b.share([alice, bob, charlie])
c_shared = c.share([alice, bob, charlie])

# print(a_shared)

res_mul = a_shared*b_shared
res_add = res_mul + c_shared
# print(res_add)
res = res_add.reconstruct(alice)
print(res)