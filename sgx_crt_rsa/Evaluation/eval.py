import math

def list_to_int(l):
    r = 0;
    
    for i in range(0, len(l)):
        r <<= 8;
        r |= l[len(l) - i - 1]
        
    return r

def compute_GCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

p = 0xEECFAE81B1B9B3C908810B10A1B5600199EB9F44AEF4FDA493B81A9E3D84F632124EF0236E5D1E3B7E28FAE7AA040A2D5B252176459D1F397541BA2A58FB6599
q = 0xC97FB1F027F453F6341233EAAAD1D9353F6C42D08866B1D05A0F2035028B9D869840B41666B42E92EA0DA3B43204B5CFCE3352524D0416A5A441E700AF461503
n = 0xBBF82F090682CE9C2338AC2B9DA871F7368D07EED41043A440D6B6F07454F51FB8DFBAAF035C02AB61EA48CEEB6FCD4876ED520D60E1EC4619719D8A5B8B807FAFB8E0A3DFC737723EE6B4B7D93A2584EE6A649D060953748834B2454598394EE0AAB12D7B61A51F527A9A41F6C1687FE2537298CA2A8F5946F8E5FD091DBDCB
d = 0xA5DAFC5341FAF289C4B988DB30C1CDF83F31251E0668B42784813801579641B29410B3C7998D6BC465745E5C392669D6870DA2C082A939E37FDCB82EC93EDAC97FF3AD5950ACCFBC111C76F1A9529444E56AAF68C56C092CD38DC3BEF5D20A939926ED4F74A13EDDFBE1A1CECC4894AF9428C2B7B8883FE4463A4BC85B1CB3C1
e = 17;

dP   = 0x54494CA63EBA0337E4E24023FCD69A5AEB07DDDC0183A4D0AC9B54B051F2B13ED9490975EAB77414FF59C1F7692E9A2E202B38FC910A474174ADC93C1F67C981
dQ   = 0x471E0290FF0AF0750351B7F878864CA961ADBD3A8A7E991C5C0556A94C3146A7F9803F8F6F8AE342E931FD8AE47A220D1B99A495849807FE39F9245A9836DA3D
invQ = 0xB06C4FDABB6301198D265BDBAE9423B380F271F73453885093077FCD39E2119FC98632154F5883B167A967BF402B4E9E2E0F9656E698EA3666EDFB25798039F7

# Test ciphertext
ct = 0x1253E04DC0A5397BB44A7AB87E9BF2A039A33D1E996FC82A94CCD30074C95DF763722017069E5268DA5D1C0B4F872CF653C11DF82314A67968DFEAE28DEF04BB6D84B1C31D654A1970E5783BD6EB96A024C2CA2F4A90FE9F2EF5C9C140E5BB48DA9536AD8700C84FC9130ADEA74E558D51A74DDF85D8B50DE96838D6063E0955

# Correct plaintext
pt_exp = 0x00EB7A19ACE9E3006350E329504B45E2CA82310B26DCD87D5C68F1EEA8F55267C31B2E8BB4251F84D7E0B2C04626F5AFF93EDCFB25C9C2B3FF8AE10E839A2DDB4CDCFE4FF47728B4A1B7C1362BAAD29AB48D2869D5024121435811591BE392F982FB3E87D095AEB40448DB972F3AC14F7BC275195281CE32D2F1B76D4D353E2D

# We can also compute the correct plaintext here...
pt = pow(ct, d, n)

# CRT formula
# mp = pow(ct, dP, p)
# mq = pow(ct, dQ, q)
# diff = (mp - mq)         
# h = (invQ * diff)
# m = (mq + h * q) % n

# working real-world examples for faulty decryptions (or signatures)
pt_fault = [0x9f, 0x7b, 0x9c, 0xb8, 0x74, 0xce, 0xf7, 0x52, 0x3e, 0x91, 0x1a, 0xed, 0x33, 0x55, 0xc8, 0x65, 0xbe, 0xd5, 0xdb, 0x6a, 0x3c, 0x74, 0x94, 0xb5, 0xad, 0x80, 0xaa, 0x60, 0x77, 0x5a, 0xa6, 0x42, 0x2d, 0xc2, 0xc4, 0x40, 0xc2, 0xa0, 0xc2, 0x1d, 0x94, 0x19, 0x19, 0x55, 0xd4, 0xad, 0xa6, 0x49, 0x24, 0x37, 0xf1, 0xca, 0x17, 0xef, 0xa6, 0xe8, 0x66, 0x56, 0xbf, 0x04, 0x74, 0xa5, 0x2e, 0xec, 0xb6, 0x7b, 0xac, 0x50, 0xf5, 0x4c, 0x54, 0x29, 0x90, 0x7b, 0xee, 0x3b, 0x98, 0xe9, 0xde, 0x6b, 0xc1, 0x41, 0x57, 0xcd, 0xc9, 0x1b, 0x70, 0x4c, 0xd9, 0xd1, 0xe0, 0xac, 0x9b, 0xf9, 0x41, 0xb3, 0x61, 0x32, 0x59, 0xc7, 0xad, 0xd4, 0x36, 0x29, 0xd2, 0xba, 0xc7, 0xfe, 0xfc, 0x81, 0xaf, 0x71, 0x69, 0x12, 0x2e, 0xc6, 0x72, 0x1f, 0x55, 0x6d, 0x0a, 0x9f, 0xd5, 0x36, 0x11, 0x90, 0x7f, 0xa8]
#pt_fault = [0x90, 0x45, 0xd9, 0x36, 0x42, 0xde, 0xbb, 0x27, 0x48, 0xf0, 0x03, 0xf2, 0xc7, 0x80, 0xd3, 0x82, 0xbf, 0x6c, 0x72, 0x11, 0x1a, 0x60, 0xab, 0x2b, 0xc8, 0x19, 0xea, 0xa0, 0x9a, 0x1b, 0xcf, 0xde, 0x8e, 0x39, 0x23, 0x14, 0x32, 0xcc, 0x60, 0x60, 0x6b, 0x8c, 0xe8, 0xca, 0x4d, 0xfe, 0x3a, 0xae, 0xfb, 0x3d, 0x2f, 0x4f, 0xc9, 0xcb, 0xc3, 0x85, 0xbf, 0x73, 0x3d, 0x2c, 0xa4, 0x6c, 0x9f, 0x7e, 0x35, 0x8d, 0xe9, 0xeb, 0x51, 0x7f, 0xc5, 0x36, 0x5b, 0x63, 0xf9, 0xb3, 0xad, 0xc7, 0x50, 0x8f, 0x37, 0xef, 0x30, 0xdb, 0x80, 0xbb, 0xd5, 0xf7, 0x1d, 0x9d, 0xed, 0xe3, 0x6a, 0xbf, 0xc8, 0x89, 0xa2, 0x77, 0xa8, 0x0e, 0x70, 0x51, 0x5f, 0x91, 0xcc, 0x48, 0x57, 0x11, 0x3c, 0x18, 0x30, 0x4a, 0xbb, 0xd6, 0x58, 0xcc, 0xd0, 0x83, 0x2e, 0x44, 0x67, 0x63, 0x60, 0xee, 0xfa, 0x28, 0x0d, 0x3c]
#pt_fault = [0x5f, 0x01, 0xd3, 0xaa, 0xb5, 0xb7, 0xa8, 0xe5, 0xdd, 0xbc, 0xa5, 0xa2, 0xb3, 0xc0, 0xec, 0x00, 0xaa, 0x21, 0x55, 0xcd, 0x6f, 0xe0, 0x31, 0xdf, 0xa1, 0x15, 0xbc, 0xa6, 0x97, 0x71, 0x80, 0x08, 0xa1, 0x22, 0xc9, 0x47, 0x00, 0xe7, 0x8c, 0x3a, 0x37, 0x2b, 0x8c, 0x4d, 0x9f, 0xea, 0x72, 0x5a, 0x24, 0x9c, 0x3c, 0xa8, 0x67, 0x72, 0x64, 0xe3, 0x5d, 0x6e, 0x02, 0xe4, 0x13, 0x35, 0x3c, 0x8a, 0xf4, 0x4e, 0xed, 0xe2, 0x0b, 0x37, 0x16, 0xf5, 0x99, 0x9e, 0x9c, 0xea, 0x2d, 0xa3, 0x62, 0xe0, 0x5a, 0x68, 0x5b, 0xfd, 0xa6, 0xfd, 0x5d, 0x95, 0xa5, 0x6a, 0x01, 0xe2, 0x52, 0x26, 0x77, 0x92, 0x12, 0xc9, 0xec, 0xfa, 0xef, 0x1c, 0x7b, 0xf3, 0x28, 0x34, 0x02, 0x3e, 0x10, 0x89, 0x28, 0x04, 0x0f, 0xb7, 0x70, 0x96, 0x72, 0x43, 0x54, 0xa1, 0xe5, 0xd9, 0xbd, 0xb6, 0xaf, 0x5e, 0x10, 0xaa]

pt_fault = list_to_int(pt_fault)

print("Correct: " + hex(pt))
print("Faulty:  " + hex(pt_fault))

# Bellcore
print("Factoring with Bellcore: ")
print hex(compute_GCD((pt - pt_fault) % n, n))

# Lenstra
print("Factoring with Lenstra:  ")
print hex(compute_GCD((pow(pt_fault, e, n) - ct) % n, n))