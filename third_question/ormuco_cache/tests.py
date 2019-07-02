import unittest
import uuid

from ormuco_cache.client import OrmucoCacheClient


class TestCacheClient(unittest.TestCase):
    def test_retrieve_command_test(self):
        client = OrmucoCacheClient()

        key = str(uuid.uuid4())
        result = client.retrieve(key)
        self.assertEqual(result, None)

    def test_retrieve_after_store_command_test(self):
        client = OrmucoCacheClient()

        key = str(uuid.uuid4())
        data = [1, 2, 3]
        store_result = client.store(key, data)
        self.assertEqual(store_result, True)

        retrieve_result = client.retrieve(key)
        self.assertEqual(retrieve_result, data)
