import unittest

from python_repos_visual import r, repo_dicts

class TestCase(unittest.TestCase):
    """Tests for the Python Repos Visual."""

    def test_status_code(self):
        self.assertEqual(r.status_code, 200)

    def test_repo_amount(self):
        self.assertGreater(len(repo_dicts), 25)

if __name__ == '__main__':
    unittest.main()