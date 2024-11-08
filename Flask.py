import unittest
import mongomock client = mongomock.MongoClient()
from mockupdb import go, Command, MockupDB


class MockupDBFlaskTest(unittest.TestCase):
    def setUp(self):
        self.server = MockupDB(auto_ismaster=True)
        self.server.run()
        self.app = make_app(self.server.uri).test_client()

    def tearDown(self):
        self.server.stop()