#!/usr/bin/env python

import unittest
import os
from .. import resolve_file_path

class TestZusiCommon(unittest.TestCase):

    def mock_os_path_exists(self, path):
        return path in self.existing_paths 

    def setUp(self):
        self.test_file_base_dir = "/mnt/zusi/Zusi3/Daten/RollingStock/ICE/"
        self.test_zusi_data_dir = "/mnt/zusi/Zusi3/Daten/"
        self.existing_paths = []

        os.path.exists = self.mock_os_path_exists

    def assertResolveFilePath(self, file_path, expected):
       self.assertEqual(
            resolve_file_path(
                file_path,
                self.test_file_base_dir,
                self.test_zusi_data_dir,
            ),
            expected)

    def test_resolve_path_same_dir(self):
        self.existing_paths.append(self.test_file_base_dir + "ICE.ls3")
        self.assertResolveFilePath("ICE.ls3", self.test_file_base_dir + "ICE.ls3")

    def test_resolve_path_relative_to_data_path(self):
        self.existing_paths.append(self.test_file_base_dir + "ICE.ls3")
        self.assertResolveFilePath("RollingStock/ICE/ICE.ls3", self.test_file_base_dir + "ICE.ls3")

if __name__ == '__main__':
    unittest.main()
