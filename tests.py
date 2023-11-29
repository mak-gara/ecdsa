import unittest
import secrets

from ecpy.curves import Curve

from sign import ECDSA


class ECDSATestCase(unittest.TestCase):
    def setUp(self) -> None:
        curve = Curve.get_curve("secp256k1")
        self.ecdsa = ECDSA(curve)

    def _run_sign_and_verify_test(self, expected_verification_result, subtraction_size=0):
        """Common logic for signing and verifying tests."""

        for i in range(5):
            message = int(secrets.token_hex(32), 16)
            private_key, public_key = self.ecdsa.generate_keys()
            signature = self.ecdsa.sign(message, private_key)
            is_verified = self.ecdsa.verify(signature, message - subtraction_size, public_key)

            print(f"Message: {hex(message)}")
            print(f"Private Key: {hex(private_key)}")
            print(f"Public Key: {public_key}")
            print(f"R: {hex(signature[0])}")
            print(f"S: {hex(signature[1])}")
            print(f"Verifying Status: {is_verified}\n")

            self.assertEqual(is_verified, expected_verification_result)

    def test_signing_and_failed_verification(self):
        """Test the signing and failed verification of ECDSA signatures."""

        self._run_sign_and_verify_test(False, 1)

    def test_signing_and_success_verification(self):
        """Test the signing and successful verification of ECDSA signatures."""

        self._run_sign_and_verify_test(True)


if __name__ == '__main__':
    unittest.main()
