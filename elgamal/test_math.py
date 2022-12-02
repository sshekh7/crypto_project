import unittest
import elgamal
from VirtualMachine import VirtualMachine
from PrivateScalar import PrivateScalar
def protocol():
    m1 = 10
    m2 = 12
    m3 = 4
    keys = elgamal.generate_keys()
    publicKey = keys['publicKey']
    privateKey = keys['privateKey']
    c1 = elgamal.encrypt(publicKey, str(m1))
    c2 = elgamal.encrypt(publicKey, str(m2))
    c3 = elgamal.encrypt(publicKey, str(m3))

    #additon and multiplication of SharedScalar

    #machines
    alice = VirtualMachine('alice')
    bob = VirtualMachine('bob')
    charlie = VirtualMachine('charlie')

    #sharing
    a = PrivateScalar(c1, alice)
    b = PrivateScalar(c2, bob)
    c = PrivateScalar(c3, charlie)

    # how to divide our private key into three parts
        #share sk1, sk2, sk3 with each parties
    # perform multiplication m1*m2 using p1 and p2
        # share * result with admin
        # share enc(m3) with admin
        # share sk1, sk2, sk3 keys with admin
    # admin: reconstruct private key, perform addition, print output
    print(a)
    print(b)
    print(c)




class GreatestCommonDivisorTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(elgamal.gcd(0, 0), 0)

    def test_any_number_and__one_returns_one(self):
        self.assertEqual(elgamal.gcd(1, 1), 1)
        self.assertEqual(elgamal.gcd(2, 1), 1)
        self.assertEqual(elgamal.gcd(3, 1), 1)

    def test_primes_are_divided_by_one(self):
        self.assertEqual(elgamal.gcd(3, 2), 1)
        self.assertEqual(elgamal.gcd(5, 3), 1)
        self.assertEqual(elgamal.gcd(7, 3), 1)
        self.assertEqual(elgamal.gcd(11, 7), 1)
        self.assertEqual(elgamal.gcd(13, 5), 1)
        self.assertEqual(elgamal.gcd(17, 2), 1)

    def test_coprimes_are_divided_by_one(self):
        self.assertEqual(elgamal.gcd(9, 8), 1)

    def test_not_coprime(self):
        self.assertNotEqual(elgamal.gcd(10, 20), 1)


if __name__ == '__main__':
    # keys = elgamal.generate_keys()
    # print(keys)
    

    # p1 = elgamal.decrypt(keys['privateKey'], c1)
    # p2 = elgamal.decrypt(keys['privateKey'], c2)
    # p3 = elgamal.decrypt(keys['privateKey'], c3)
    # print(p1)
    # print(p2)
    # print(p3)
    protocol()

    # unittest.main()
