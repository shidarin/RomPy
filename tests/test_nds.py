import mock
import os
import unittest

import rompy

SAMPLE_ROMS_ALL_DASH = [
    "2926 - My Little Pony - Pinkie Pie's Party (US).zip",
    "3422 - Unou Ikusei - IQ Breeder - Pet to Nakayoku IQ Lesson (JP)(BAHAMUT).7z",
    "5234 - Shrek Forever After (DSi Enhanced) (E)(ROM)(NDS6.com).zip",
    "2073 - Naruto - Ninja Destiny (U)(SQUiRE).rar",
    "2178 - Kachou Shima Kousaku DS - Dekiru Otoko no Love & Success (J)(Independent).7z",
    "4373 - Let's Play Flight Attendant (EU)(M5).zip",
    "2497 - Guitar Hero - On Tour (EU).zip",
    "2114 - Bunnyz (E)(SQUiRE).7z",
    "0374 - Contact (J)(WRG).zip",
    "3471 - Cosmopolitan - Total Relooking (FR)(EXiMiUS).7z"
]

SAMPLE_ROMS_MIXED_DASH = [
    "2926 - My Little Pony - Pinkie Pie's Party (US).zip",
    "3422 Unou Ikusei - IQ Breeder - Pet to Nakayoku IQ Lesson (JP)(BAHAMUT).7z",
    "5234 - Shrek Forever After (DSi Enhanced) (E)(ROM)(NDS6.com).zip",
    "2073 - Naruto - Ninja Destiny (U)(SQUiRE).rar",
    "2178 Kachou Shima Kousaku DS - Dekiru Otoko no Love & Success (J)(Independent).7z",
    "4373 - Let's Play Flight Attendant (EU)(M5).zip",
    "2497 Guitar Hero - On Tour (EU).zip",
    "2114 - Bunnyz (E)(SQUiRE).7z",
    "0374 Contact (J)(WRG).zip",
    "3471 - Cosmopolitan - Total Relooking (FR)(EXiMiUS).7z"
]

SAMPLE_ROMS_NO_DASH = [
    "2926 My Little Pony - Pinkie Pie's Party (US).zip",
    "3422 Unou Ikusei - IQ Breeder - Pet to Nakayoku IQ Lesson (JP)(BAHAMUT).7z",
    "5234 Shrek Forever After (DSi Enhanced) (E)(ROM)(NDS6.com).zip",
    "2073 Naruto - Ninja Destiny (U)(SQUiRE).rar",
    "2178 Kachou Shima Kousaku DS - Dekiru Otoko no Love & Success (J)(Independent).7z",
    "4373 Let's Play Flight Attendant (EU)(M5).zip",
    "2497 Guitar Hero - On Tour (EU).zip",
    "2114 Bunnyz (E)(SQUiRE).7z",
    "0374 Contact (J)(WRG).zip",
    "3471 Cosmopolitan - Total Relooking (FR)(EXiMiUS).7z"
]

SAMPLE_ROMS_NO_GROUP = [
    "2926 - My Little Pony - Pinkie Pie's Party (US).zip",
    "3422 - Unou Ikusei - IQ Breeder - Pet to Nakayoku IQ Lesson (JP).7z",
    "5234 - Shrek Forever After (DSi Enhanced) (E)(ROM).zip",
    "2073 - Naruto - Ninja Destiny (U).rar",
    "2178 - Kachou Shima Kousaku DS - Dekiru Otoko no Love & Success (J).7z",
    "4373 - Let's Play Flight Attendant (EU).zip",
    "2497 - Guitar Hero - On Tour (EU).zip",
    "2114 - Bunnyz (E).7z",
    "0374 - Contact (J).zip",
    "3471 - Cosmopolitan - Total Relooking (FR).7z"
]


class TestAddDash(unittest.TestCase):

    @mock.patch('rompy.nds.os.rename')
    @mock.patch('rompy.nds.os.listdir')
    def testBasics(self, mock_listdir, mock_rename):
        mock_listdir.return_value = SAMPLE_ROMS_NO_DASH
        rompy.nds.add_ds_dash('banana')
        for i, rom in enumerate(SAMPLE_ROMS_NO_DASH):
            mock_rename.assert_any_call(
                os.path.join('banana', rom),
                os.path.join('banana', SAMPLE_ROMS_ALL_DASH[i])
            )

    @mock.patch('rompy.nds.os.rename')
    @mock.patch('rompy.nds.os.listdir')
    def testMixed(self, mock_listdir, mock_rename):
        mock_listdir.return_value = SAMPLE_ROMS_MIXED_DASH
        rompy.nds.add_ds_dash('apple')
        for i, rom in enumerate(SAMPLE_ROMS_MIXED_DASH):
            if rom[5] != '-':
                mock_rename.assert_any_call(
                    os.path.join('apple', rom),
                    os.path.join('apple', SAMPLE_ROMS_ALL_DASH[i])
                )

    @mock.patch('rompy.nds.os.rename')
    @mock.patch('rompy.nds.os.listdir')
    def testAllDash(self, mock_listdir, mock_rename):
        mock_listdir.return_value = SAMPLE_ROMS_ALL_DASH
        rompy.nds.add_ds_dash('zebra')
        mock_rename.assert_not_called()

if __name__ == '__main__':
    unittest.main()
