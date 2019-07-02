import unittest
import uuid

from ormuco_cache.command import CommandParser, RetrieveCommand, StoreCommand
from ormuco_cache.settings import OrmucoCacheServerSettings

class TestCommandParser(unittest.TestCase):
    def test_retrieve_command_test(self):
        settings = OrmucoCacheServerSettings()

        command_parser = CommandParser(settings)

        retrieve_command = "RTRV " + str(uuid.uuid4())
        result = command_parser.parse(retrieve_command)
        self.assertEqual(result, None)

    def test_retrieve_after_store_command_test(self):
        settings = OrmucoCacheServerSettings()

        command_parser = CommandParser(settings)

        store_command = "STR Key [1,2,3]"
        result = command_parser.parse(store_command)
        self.assertEqual(result, True)

        retrieve_command = "RTRV Key"
        result = command_parser.parse(retrieve_command)
        self.assertEqual(result, [1,2,3])

    def test_acknowledgement_parsing(self): 
        settings = OrmucoCacheServerSettings()

        command_parser = CommandParser(settings)

        command = "ACK"
        result = command_parser.parse(command)
        self.assertEqual(result, True)

    def test_miss_parsing(self): 
        settings = OrmucoCacheServerSettings()

        command_parser = CommandParser(settings)

        command = "MISS"
        result = command_parser.parse(command)
        self.assertEqual(result, None)

    def test_invalid_command_parsing(self): 
        settings = OrmucoCacheServerSettings()

        command_parser = CommandParser(settings)

        command = "FOOBAR"
        with self.assertRaises(Exception):
            result = command_parser.parse(command)

        command = "NOT A COMMAND"
        with self.assertRaises(Exception):
            result = command_parser.parse(command)



