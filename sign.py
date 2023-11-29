from random import randint
from ecpy.curves import Point


class ECDSA:
    """Elliptic Curve Digital Signature Algorithm (ECDSA) implementation."""

    def __init__(self, curve):
        self.curve = curve

    def sign(self, message: int, private_key: int) -> tuple[int, int]:
        """
        Signs a message using ECDSA.

        Args:
            message (int): The message to be signed. It is recommended to sign only the hash value.
            private_key (int): The private key for signing.

        Returns:
            tuple[int, int]: The ECDSA signature (r, s).
        """

        while True:
            k = randint(1, self.curve.order - 1)
            r_point = k * self.curve.generator
            r = r_point.x % self.curve.order

            if r == 0:
                continue

            s = pow(k, -1, self.curve.order) * (message + r * private_key) % self.curve.order

            if s == 0:
                continue

            return r, s

    def verify(self, signature: tuple[int, int], message: int, public_key: Point) -> bool:
        """
        Verifies the ECDSA signature for a given message and public key.

        Args:
            signature (tuple[int, int]): The ECDSA signature (r, s).
            message (int): The original message.
            public_key (Point): The public key.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """

        r, s = signature
        u = message * pow(s, -1, self.curve.order) % self.curve.order
        v = r * pow(s, -1, self.curve.order) % self.curve.order
        c_point = u * self.curve.generator + public_key * v
        return c_point.x == r

    def generate_keys(self) -> tuple[int, Point]:
        """
        Generates a pair of private and public keys.

        Returns:
            tuple[int, Point]: The generated private key and corresponding public key.
        """

        while True:
            d = randint(1, self.curve.order - 1)
            q = d * self.curve.generator

            if not (self.is_point_at_inf(q)) \
                    and 0 <= q.x < self.curve.field and 0 <= q.y < self.curve.field \
                    and self.curve.is_on_curve(q) \
                    and self.is_point_at_inf(self.curve.order * q):
                return d, q

    @staticmethod
    def is_point_at_inf(point: Point) -> bool:
        """Checks if a point is at infinity.

        Args:
            point (Point): The point to be checked.

        Returns:
            bool: True if the point is at infinity, False otherwise.
        """

        return point.__str__() == "inf"
