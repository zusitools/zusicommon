#!/usr/bin/env python

import unittest
import os
import sys
from .. import resolve_file_path

ZUSI_DATAPATH = r"Z:\Zusi3\Daten" if sys.platform.startswith("win") else "/mnt/zusi3/daten"
NON_ZUSI_PATH = r"Z:\NichtZusi" if sys.platform.startswith("win") else "/mnt/nichtzusi"

class TestZusiCommon(unittest.TestCase):

    def mock_os_path_exists(self, path):
        return path in self.existing_paths 

    def setUp(self):
        self.test_file_base_dir = os.path.join(ZUSI_DATAPATH, "RollingStock", "ICE")
        self.existing_paths = []

        os.path.exists = self.mock_os_path_exists

    def assertResolveFilePath(self, expected, file_path):
       self.assertEqual(expected,
            resolve_file_path(
                file_path,
                self.test_file_base_dir,
                ZUSI_DATAPATH,
            ))

    def test_resolve_path_same_dir(self):
        self.existing_paths.append(os.path.join(self.test_file_base_dir, "ICE.ls3"))
        self.assertResolveFilePath(os.path.join(self.test_file_base_dir, "ICE.ls3"), "ICE.ls3")

    def test_resolve_path_relative_to_data_path(self):
        self.existing_paths.append(os.path.join(self.test_file_base_dir, "ICE.ls3"))
        self.assertResolveFilePath(os.path.join(self.test_file_base_dir, "ICE.ls3"), r"RollingStock\ICE\ICE.ls3")

if __name__ == '__main__':
    unittest.main()
