import unittest
from mock import mock
from rfidhid.core import RfidHid, PayloadResponse

 
class TestPayloadResponse(unittest.TestCase):
    payload = None
    payloadW26 = None

    def setUp(self):
        """Initialize common objects for test cases"""
        self.payload = PayloadResponse([3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 0, 77, 73, 150, 2, 210, 68, 3]) # 32 bits uid
        self.payloadW26 = PayloadResponse([3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 0, 77, 00, 150, 2, 210, 13, 3]) # 24 bits uid


    def test_get_tag_uid_as_byte_sequence_base10(self):
        expected = [73, 150, 2, 210]
        actual = self.payload.get_tag_uid_as_byte_sequence()
        self.assertEqual(expected, actual)
    
    def test_get_tag_uid_as_byte_sequence_base16(self):
        expected = ['0x49', '0x96', '0x02', '0xd2']
        actual = self.payload.get_tag_uid_as_byte_sequence(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)
    
    def test_get_tag_uid_as_byte_sequence_base2(self):
        expected = ['0b01001001', '0b10010110', '0b00000010', '0b11010010']
        actual = self.payload.get_tag_uid_as_byte_sequence(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)


    def test_get_tag_cid_base10(self): 
        expected = 77
        actual = self.payload.get_tag_cid()
        self.assertEqual(expected, actual)
    
    def test_get_tag_cid_base16(self): 
        expected = '0x4d'
        actual = self.payload.get_tag_cid(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)
    
    def test_get_tag_cid_base2(self): 
        expected = '0b01001101'
        actual = self.payload.get_tag_cid(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)

 
    def test_get_tag_uid_base10(self): 
        expected = 1234567890
        actual = self.payload.get_tag_uid()
        self.assertEqual(expected, actual)
    
    def test_get_tag_uid_base16(self): 
        expected = '0x499602d2'
        actual = self.payload.get_tag_uid(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)
    
    def test_get_tag_uid_base2(self): 
        expected = '0b01001001100101100000001011010010'
        actual = self.payload.get_tag_uid(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)
    

    def test_get_tag_w26_base_invalid(self): 
        expected = None # w26 expects 24bits uid not 32bits
        actual = self.payload.get_tag_w26()
        self.assertEqual(expected, actual)
    
    def test_get_tag_w26_base10(self): 
        expected = (150, 722)
        actual = self.payloadW26.get_tag_w26()
        self.assertEqual(expected, actual)
    
    def test_get_tag_w26_base16(self): 
        expected = ('0x96', '0x2d2')
        actual = self.payloadW26.get_tag_w26(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)
    
    def test_get_tag_w26_base2(self): 
        expected = ('0b10010110', '0b001011010010')
        actual = self.payloadW26.get_tag_w26(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)
    

    def test_get_crc_sum_base10(self): 
        expected = 68
        actual = self.payload.get_crc_sum()
        self.assertEqual(expected, actual)
    
    def test_get_crc_sum_base16(self): 
        expected = '0x44'
        actual = self.payload.get_crc_sum(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)
    
    def test_get_crc_sum_base2(self): 
        expected = '0b01000100'
        actual = self.payload.get_crc_sum(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)


    def test_get_raw_data_base10(self):
        expected = [3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 0, 77, 73, 150, 2, 210, 68, 3]
        actual = self.payload.get_raw_data()
        self.assertEqual(expected, actual)
    
    def test_get_raw_data_base16(self):
        expected = ['0x03', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x02', '0x00', '0x06', '0x00', '0x4d', '0x49', '0x96', '0x02', '0xd2', '0x44', '0x03']
        actual = self.payload.get_raw_data(base=PayloadResponse.BASE16)
        self.assertEqual(expected, actual)

    def test_get_raw_data_base2(self):
        expected = ['0b00000011', '0b00000000', '0b00000000', '0b00000000', '0b00000000', '0b00000000', '0b00000000', '0b00000000', '0b00000010', '0b00000000', '0b00000110', '0b00000000', '0b01001101', '0b01001001', '0b10010110', '0b00000010', '0b11010010', '0b01000100', '0b00000011']
        actual = self.payload.get_raw_data(base=PayloadResponse.BASE2)
        self.assertEqual(expected, actual)
