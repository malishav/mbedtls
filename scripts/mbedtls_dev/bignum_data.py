"""Base values and datasets for bignum generated tests and helper functions that
produced them."""
# Copyright The Mbed TLS Contributors
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

# Functions calling these were used to produce test data and are here only for
# reproducability, they are not used by the test generation framework/classes
try:
    from Cryptodome.Util.number import isPrime, getPrime #type: ignore #pylint: disable=import-error
except ImportError:
    pass

# Generated by bignum_common.gen_safe_prime(192,1)
SAFE_PRIME_192_BIT_SEED_1 = "d1c127a667786703830500038ebaef20e5a3e2dc378fb75b"

# First number generated by random.getrandbits(192) - seed(2,2), not a prime
RANDOM_192_BIT_SEED_2_NO1 = "177219d30e7a269fd95bafc8f2a4d27bdcf4bb99f4bea973"

# Second number generated by random.getrandbits(192) - seed(2,2), not a prime
RANDOM_192_BIT_SEED_2_NO2 = "cf1822ffbc6887782b491044d5e341245c6e433715ba2bdd"

# Third number generated by random.getrandbits(192) - seed(2,2), not a prime
RANDOM_192_BIT_SEED_2_NO3 = "3653f8dd9b1f282e4067c3584ee207f8da94e3e8ab73738f"

# Fourth number generated by random.getrandbits(192) - seed(2,2), not a prime
RANDOM_192_BIT_SEED_2_NO4 = "ffed9235288bc781ae66267594c9c9500925e4749b575bd1"

# Ninth number generated by random.getrandbits(192) - seed(2,2), not a prime
RANDOM_192_BIT_SEED_2_NO9 = "2a1be9cd8697bbd0e2520e33e44c50556c71c4a66148a86f"

# Generated by bignum_common.gen_safe_prime(1024,3)
SAFE_PRIME_1024_BIT_SEED_3 = ("c93ba7ec74d96f411ba008bdb78e63ff11bb5df46a51e16b"
                              "2c9d156f8e4e18abf5e052cb01f47d0d1925a77f60991577"
                              "e128fb6f52f34a27950a594baadd3d8057abeb222cf3cca9"
                              "62db16abf79f2ada5bd29ab2f51244bf295eff9f6aaba130"
                              "2efc449b128be75eeaca04bc3c1a155d11d14e8be32a2c82"
                              "87b3996cf6ad5223")

# First number generated by random.getrandbits(1024) - seed(4,2), not a prime
RANDOM_1024_BIT_SEED_4_NO1 = ("6905269ed6f0b09f165c8ce36e2f24b43000de01b2ed40ed"
                              "3addccb2c33be0ac79d679346d4ac7a5c3902b38963dc6e8"
                              "534f45738d048ec0f1099c6c3e1b258fd724452ccea71ff4"
                              "a14876aeaff1a098ca5996666ceab360512bd13110722311"
                              "710cf5327ac435a7a97c643656412a9b8a1abcd1a6916c74"
                              "da4f9fc3c6da5d7")

# Second number generated by random.getrandbits(1024) - seed(4,2), not a prime
RANDOM_1024_BIT_SEED_4_NO2 = ("f1cfd99216df648647adec26793d0e453f5082492d83a823"
                              "3fb62d2c81862fc9634f806fabf4a07c566002249b191bf4"
                              "d8441b5616332aca5f552773e14b0190d93936e1daca3c06"
                              "f5ff0c03bb5d7385de08caa1a08179104a25e4664f5253a0"
                              "2a3187853184ff27459142deccea264542a00403ce80c4b0"
                              "a4042bb3d4341aad")

# Third number generated by random.getrandbits(1024) - seed(4,2), not a prime
RANDOM_1024_BIT_SEED_4_NO3 = ("14c15c910b11ad28cc21ce88d0060cc54278c2614e1bcb38"
                              "3bb4a570294c4ea3738d243a6e58d5ca49c7b59b995253fd"
                              "6c79a3de69f85e3131f3b9238224b122c3e4a892d9196ada"
                              "4fcfa583e1df8af9b474c7e89286a1754abcb06ae8abb93f"
                              "01d89a024cdce7a6d7288ff68c320f89f1347e0cdd905ecf"
                              "d160c5d0ef412ed6")

# Fourth number generated by random.getrandbits(1024) - seed(4,2), not a prime
RANDOM_1024_BIT_SEED_4_NO4 = ("32decd6b8efbc170a26a25c852175b7a96b98b5fbf37a2be"
                              "6f98bca35b17b9662f0733c846bbe9e870ef55b1a1f65507"
                              "a2909cb633e238b4e9dd38b869ace91311021c9e32111ac1"
                              "ac7cc4a4ff4dab102522d53857c49391b36cc9aa78a330a1"
                              "a5e333cb88dcf94384d4cd1f47ca7883ff5a52f1a05885ac"
                              "7671863c0bdbc23a")

# Fifth number generated by random.getrandbits(1024) - seed(4,2), not a prime
RANDOM_1024_BIT_SEED_4_NO5 = ("53be4721f5b9e1f5acdac615bc20f6264922b9ccf469aef8"
                              "f6e7d078e55b85dd1525f363b281b8885b69dc230af5ac87"
                              "0692b534758240df4a7a03052d733dcdef40af2e54c0ce68"
                              "1f44ebd13cc75f3edcb285f89d8cf4d4950b16ffc3e1ac3b"
                              "4708d9893a973000b54a23020fc5b043d6e4a51519d9c9cc"
                              "52d32377e78131c1")

# Adding 192 bit and 1024 bit numbers because these are the shortest required
# for ECC and RSA respectively.
INPUTS_DEFAULT = [
        "0", "1", # corner cases
        "2", "3", # small primes
        "4",      # non-prime even
        "38",     # small random
        SAFE_PRIME_192_BIT_SEED_1,  # prime
        RANDOM_192_BIT_SEED_2_NO1,  # not a prime
        RANDOM_192_BIT_SEED_2_NO2,  # not a prime
        SAFE_PRIME_1024_BIT_SEED_3, # prime
        RANDOM_1024_BIT_SEED_4_NO1, # not a prime
        RANDOM_1024_BIT_SEED_4_NO3, # not a prime
        RANDOM_1024_BIT_SEED_4_NO2, # largest (not a prime)
        ]

# Only odd moduli are present as in the new bignum code only odd moduli are
# supported for now.
MODULI_DEFAULT = [
        "53", # safe prime
        "45", # non-prime
        SAFE_PRIME_192_BIT_SEED_1,  # safe prime
        RANDOM_192_BIT_SEED_2_NO4,  # not a prime
        SAFE_PRIME_1024_BIT_SEED_3, # safe prime
        RANDOM_1024_BIT_SEED_4_NO5, # not a prime
        ]

def __gen_safe_prime(bits, seed):
    '''
    Generate a safe prime.

    This function is intended for generating constants offline and shouldn't be
    used in test generation classes.

    Requires pycryptodomex for getPrime and isPrime and python 3.9 or later for
    randbytes.
    '''
    rng = random.Random()
    # We want reproducability across python versions
    rng.seed(seed, version=2)
    while True:
        prime = 2*getPrime(bits-1, rng.randbytes)+1 #pylint: disable=no-member
        if isPrime(prime, 1e-30):
            return prime
