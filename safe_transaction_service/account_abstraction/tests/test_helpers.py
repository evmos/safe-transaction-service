from django.test import TestCase

from hexbytes import HexBytes
from safe_eth.eth.tests.mocks.mock_bundler import user_operation_mock
from safe_eth.safe.tests.safe_test_case import SafeTestCaseMixin

from ..helpers import DecodedInitCode, decode_init_code


class TestAccountAbstractionHelpers(SafeTestCaseMixin, TestCase):
    def test_decode_init_code(self):
        with self.assertRaises(ValueError):
            decode_init_code(b"", self.ethereum_client)

        expected = DecodedInitCode(
            factory_address="0x4e1DCf7AD4e460CfD30791CCC4F9c8a4f820ec67",
            factory_data=HexBytes(
                "0x1688f0b900000000000000000000000029fcb43b46531bca003ddc8fcb67ffe91900c7620000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001e4b63e800d000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000010000000000000000000000008ecd4ec46d4d2a6b64fe960b3d64e8b94b2234eb0000000000000000000000000000000000000000000000000000000000000140000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000648d0dc49f00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000001000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b40370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            ),
            initializer=b"\xb6>\x80\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8e\xcdN\xc4mM*kd\xfe\x96\x0b=d\xe8\xb9K\"4\xeb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x81\xc4\xa4\xdbqu0$d\xff<\x068\x0b\xc3'\x0b@7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Z\xc2U\x88\x98\x82\xac\xd3\xda*\xa99g\x9e?=L\xea\"\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x8d\r\xc4\x9f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x81\xc4\xa4\xdbqu0$d\xff<\x068\x0b\xc3'\x0b@7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            singleton="0x29fcB43b46531BcA003ddC8FCB67FFE91900C762",
            salt_nonce=0,
            expected_address="0xB0B5c0578Aa134b0496a6C0e51A7aae47C522861",
            owners=["0x5aC255889882aCd3da2aA939679E3f3d4cea221e"],
            threshold=1,
            to="0x8EcD4ec46D4D2a6B64fE960B3D64e8B94B2234eb",
            data=b"\x8d\r\xc4\x9f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x81\xc4\xa4\xdbqu0$d\xff<\x068\x0b\xc3'\x0b@7",
            fallback_handler="0xa581c4A4DB7175302464fF3C06380BC3270b4037",
            payment_token="0x0000000000000000000000000000000000000000",
            payment=0,
            payment_receiver="0x0000000000000000000000000000000000000000",
        )
        result = decode_init_code(
            HexBytes(user_operation_mock["result"]["userOperation"]["initCode"]),
            self.ethereum_client,
        )
        self.assertEqual(result, expected)
