import unittest
from repo import Repo
import os
import config
import hashlib
import json
import shutil

class TestRepo(unittest.TestCase):
    def setUp(self):
        if os.path.exists(config.TEST_DIR):
            shutil.rmtree(config.TEST_DIR)
        
        os.makedirs(config.TEST_DIR)
        self.test_dir = config.TEST_DIR

        return super().setUp()

    def tearDown(self):
        if os.path.exists(config.TEST_DIR):
            shutil.rmtree(config.TEST_DIR)
        return super().tearDown()
    
    def test_should_init_correctly(self):
        repo = Repo(self.test_dir, push=False)
        self.assertEqual(repo.path, self.test_dir)
        self.assertEqual(repo.dir_state, {})
        self.assertIsNotNone(repo.UUID)
        self.assertEqual(repo.repo_dir, os.path.join(self.test_dir, config.REPO_DIR))
        self.assertTrue(os.path.exists(repo.repo_dir))
        self.assertTrue(os.path.exists(repo.index_file))
        self.assertTrue(os.path.exists(repo.uuid_file))

    def test_hash_file(self):
        repo = Repo(self.test_dir, push=False)
        test_file = os.path.join(self.test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        file_hash = repo.hash_file(test_file)
        self.assertIsNotNone(file_hash)
        self.assertEqual(file_hash, hashlib.sha1(b'test content').hexdigest())

    def test_update_file_state(self):
        repo = Repo(self.test_dir, push=False)
        test_file = os.path.join(self.test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        repo.update_file_state(test_file, created=True)
        self.assertIn(test_file, repo.dir_state)
        self.assertEqual(repo.dir_state[test_file], hashlib.sha1(b'test content').hexdigest())
    
    def test_update_index_file_state(self):
        repo = Repo(self.test_dir, push=False)
        test_file = os.path.join(self.test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        repo.update_file_state(test_file, created=True)
        with open(repo.index_file, 'r') as f:
            index = json.load(f)
            self.assertIn(test_file, index)
            self.assertEqual(index[test_file], hashlib.sha1(b'test content').hexdigest())

    def test_delete_file_state(self):
        repo = Repo(self.test_dir, push=False)
        test_file = os.path.join(self.test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test content')
        
        repo.update_file_state(test_file, created=True)
        repo.delete_file_state(test_file)
        self.assertNotIn(test_file, repo.dir_state)
    
    def should_reinitialize_correctly(self):
        repo = Repo(self.test_dir, push=False)
        test_file = os.path.join(self.test_dir, 'test.txt')
        uuid = repo.UUID
        with open(test_file, 'w') as f:
            f.write('test content')
        
        repo.update_file_state(test_file, created=True)
        repo.commit()
        repo = Repo(self.test_dir, push=False)
        self.assertEqual(repo.UUID, uuid)
        self.assertIn(test_file, repo.dir_state)
        self.assertEqual(repo.dir_state[test_file], hashlib.sha1(b'test content').hexdigest())

if __name__ == '__main__':
    unittest.main()