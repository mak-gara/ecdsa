# ECDSA Implementation

This is a Python implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA). ECDSA is a widely used digital signature algorithm that leverages the mathematical properties of elliptic curves for secure cryptographic operations.

## Python Version Compatibility
This project is developed using Python version 3.10.7. While it may be possible to run the project on earlier Python versions, it is important to note that doing so might result in unexpected side effects or errors. For optimal performance and to prevent potential issues, it's recommended to use Python version 3.10.7 or higher.

## Installation and Dependencies

To utilize the `ECDSA`  implementation, ensure you have Python installed. You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

There is only one dependency, which is the `ECPy` library for working with elliptic curves.

## Usage

To use the ECDSA implementation, follow these steps:

1. Import the necessary components:

   ```python
   from ecpy.curves import Curve
   from sign import ECDSA
   ```

2. Create an instance of the `ECDSA` class by providing an elliptic curve as an argument:

   ```python
   curve_name = # specify your elliptic curve name
   curve = Curve.get_curve(curve_name)
   ecdsa = ECDSA(curve)
   ```
   
   ECPy support the following curves:

   - Short Weierstrass form: y²=x³+a*x+b

   - Twisted Edward a*x²+y2=1+d*x²*y²

   If you want to use a different elliptic curve, you must create the curve yourself using the capabilities of `ECPy`.


4. Generate a pair of private and public keys:

   ```python
   private_key, public_key = ecdsa.generate_keys()
   ```

4. Sign a message using the private key:

   ```python
   message = # specify your message
   signature = ecdsa.sign(message, private_key)
   ```

5. Verify the signature with the public key:

   ```python
   is_valid = ecdsa.verify(signature, message, public_key)
   ```

## Example

Here's a quick example of how to use the ECDSA implementation:

```python
from ecpy.curves import Curve
from sign import ECDSA

curve_name = # specify your elliptic curve name
curve = Curve.get_curve(curve_name)

# Create an instance of the ECDSA class
ecdsa = ECDSA(curve)

# Generate a pair of private and public keys
private_key, public_key = ecdsa.generate_keys()

# Sign a message using the private key
message = # specify your message
signature = ecdsa.sign(message, private_key)

# Verify the signature with the public key
is_valid = ecdsa.verify(signature, message, public_key)
print(f"Is the signature valid? {is_valid}")
```

Make sure to replace the placeholder comments with your actual elliptic curve parameters and message.

## Running Tests
To run the tests for this code, execute the tests.py file.

```shell
python tests.py
```
This will run a series of tests to verify the correctness of the methods of the `ECDSA` class.

Upon executing the tests, you will obtain comprehensive information regarding both the input and output data as shown below:

```text
Test the signing and successful verification of ECDSA signatures.

Message: 0x841a72a62121dbb9b1067ec27a3af95734cd1f0523f9d35710c674c4bafaa176
Private Key: 0x9093adb47676b5ef42fcff24a6c4b1cce96a6dfa4697844c5c1c90f039f91780
Public Key: (0x88685ce4fd34a0be915af3d3a0daf8dc94f52ec9726f59f4ccff658e8c40b35b , 0x35aa17a6170cab71a8ebdc70f4443d1c32122946dca674a0c776313e14286ba8)
R: 0xc9b29672a9c916aab731a165ce79b5ed1f70de7d137532af0c82c3427eafe963
S: 0xaa324a6d964b4663f6cad30d65061498586578837d37cb7f5f79efecb80ac5b
Verifying Status: True

Message: 0xa06cd2dd1fd2a648a91aeb679875cf7f6220ee4059c5733cf2b909972dd61b62
Private Key: 0xee4203eb0a91d7e24ce49c4af9b4ed6461015d2ac847e277f1b63aa4ff554d0e
Public Key: (0xf9a42013d101368b62795c70ec705a3ca3c892391784fc5f81118cfcd1e79fa4 , 0x1839c0ad6e2d1cf4da63566204ff04b6c249fa56b0b936c1a1f5bfab6d74a22c)
R: 0x153be9b53c9ddff631a2d2165c4ef960e9265c58bbc2e1ebebcdc6644829d9c6
S: 0xc6da56f939d1740d722aa17a5f8aeb90055926ec86b2c4c4034421f3c7807cc9
Verifying Status: True

Message: 0x132417130a3571c701359568bc5197f19349e4a73925ed8a4f0fd51dfa9f56c1
Private Key: 0x207c90c6d83a4c7921ba73b023d4a2b87875aa82c3da1e20d011d67aee329f56
Public Key: (0x4a04d2a28f3e3c8e0a5ae1cfc19e587e9179d12ed1260c45d07f97309b23ffde , 0x4af3824d8d24505b99461ae3eff4295492bc8a57589cc62066046d2609bb9842)
R: 0x56347da784ce322913ce70818f06dfe7bc7e6940771c3619ffdfc3634c126095
S: 0xa454acee036b85e6b8ed2ace5fbadbab365d53dcfb76862ac3e190370ff6b129
Verifying Status: True

Message: 0x20fc6d9507487d524739b4b1bc0350b0c35df6547e88655105f5de0ca27472c
Private Key: 0x81f8c69485f300147d7f6ca8f6569294f91641b1d073442b33db5710475b38aa
Public Key: (0xe1b37a4b604bbbbccc09b675e1e7da7f4ed072f7b41fc04975887a948d5b4c4d , 0xf19d3b781513a8d7716a5192116ad107cbf95a63a63877b014138ed28bee9bab)
R: 0xe3462bf02caf562a426a9117caf250e42a3a39db9162219351fcc0a92fd1e5f0
S: 0xa9145df90a51071db8ac366f3f8a0977d5a8da44ced4b34d2fb98183ac6df0a4
Verifying Status: True

Message: 0xdb34dd29138a61073e3c9bc9d4526966759cc2662355409667f64689dc7682db
Private Key: 0x90bdecfe5d550a5b48efe28ba692128e7a9d0fd657ad489f3c2dd79740c9b77a
Public Key: (0x4e3c407c1a02bb6d218a744bd56f9825db4c601b3d46521e88d8cbda1ee34245 , 0x3d5fd391ac8f6022d089217e45561bbdb8bd6ffd48ad652ae455f1a8abc1c644)
R: 0x6b313280ed38c546f1e88590cfedaa0f45a6aa4ab96cbb9ffb471fa1d4d56bd6
S: 0x534ad9fa0ba322b3515a0454ec028c992b62a9a236d0d393e2954552b7373c40
Verifying Status: True
```

```text
Test the signing and failed verification of ECDSA signatures.

Message: 0x1a7e2c6469247ee0249500f9a5556e312972316d835a46ce82b3604cb9d7ddc1
Private Key: 0x96fa4ea5f4de98b5b7737759f4556dd74a2f7e487a6c7342e49035683b93c9d2
Public Key: (0xcbacd33453254a032cca88fca94427f11e3abf9285ed4c553d3370f433635cd6 , 0x245cf50c9e64d26309cdea3400701f83dfe0e7f12b54b2a0c4cf7e175461e3a3)
R: 0x8994cf280c1ea3a6910f1dbfdb85aef0a730b9b36d7d2df50eedea7a0d492a33
S: 0x6959c30a2d899d1001946ec9b6e9ed479e73a7ba8871339aa5278e1b1762cf8d
Verifying Status: False

Message: 0xc57fe91f0cc51232b516877e35bdc6a220a361ed736742a5a5514962ea8d37d3
Private Key: 0xfeec1405e5eade107a8faf29aaa8df48e12fc2b954a1062f8ebd75915c721bb0
Public Key: (0xe83d8fccc24828261a46b02126b7d71a4f5ea715c0b8e5707db20d69c8839a67 , 0x58d1ead5053c25f3df616e250c3992de128a2d4c7768ae481812e024572d18a1)
R: 0x1b96ce5dbad1a4c02ea285240dac712e9d5e7d13783cc25346435594c7fa9bc2
S: 0x1f04a77f8675e3440b89f2c20e2a30d5d666fa67cc3aec18a93334a269c7a1e7
Verifying Status: False

Message: 0xb8a3c852911120a3e17c21033867388abc1441edb25c479ce9923d32d1cd3785
Private Key: 0x349158ebda8a28dd4644224dd8e6056e1e5e6c2ad86dc4cbec958f3c172f0c83
Public Key: (0x59ca4f8ebe661b3b0781ec09a840a725f9a72a2961a9fa05303dc5f86e0d722d , 0x31b2da447e823c54beff9799502e9eff986568d6f6653eb9861da262906b74a9)
R: 0xdfee458aaa22b425cd8fc4b4e17d3a15ce592cf4a81b58f34d1c642a36425bc3
S: 0x2d932544bf4113585dce8522df21475d554f50b1eeb4c2339a24886b139787da
Verifying Status: False

Message: 0xcb696decffd462c75b31df74b9213ac9042429ff318717c9f56211131544eae8
Private Key: 0x356f3d5fd8712a1268491dd087c5b30d03afb95dda171a1b9146615994f3e572
Public Key: (0x2c4ea5d48d1ad16e29b2b7aad29ea0946892568f8ad46c929ba2b9e6b9ed8b12 , 0xe642a823d7dd7c15840477f6b47a8b64976cee722df70f89f0ef632cdcd962e8)
R: 0x89093b963363b42a34861411d5c76a4273e0e39203768aa047e8cda3113a2bf2
S: 0x6f24eb3e358d74a0dbd6d140da57a06c73141b0783f68a07e2cd1dd55a30d522
Verifying Status: False

Message: 0x1e6616e1cc8f54fedfff324e8eb882fdbccfa521b31b3457264522f23a3d44d4
Private Key: 0x3d039d31da877c366315abbe8d5e42c469134d455f108c83309c7686ef463f7a
Public Key: (0x9975de904f35548ae97faadc461a34ad764ae8a0b1919b0885772600eb52b899 , 0x19c93167585e3c5999f10ca4f15e792f7105b7b3747e60ef80b06e67a6fbe142)
R: 0x940e141d90ea0bbf94e35d16ffe70262c20278b0456ade2a7d4f2f31b79eb4dc
S: 0x3a18ff3b63dd08d435c9a6d82e0df5c66546e2557f9e90514024cd882e959dc3
Verifying Status: False
```