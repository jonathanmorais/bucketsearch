import unittest

class TestJsonResponse(unittest.TestCase):

    def count_array_response():
        c = []
        obj = {
            "bucket-name": [
                "2019-04-29-20:36:54",
                "30",
                "4161"
                ]
            }

        for i in obj['bucket-name']:
            c.append(i)

        return len(c)

    def test_count_array_response(self):
        count_response = TestJsonResponse.count_array_response()
        self.assertEqual(count_response, 3)    

if __name__ == '__main__':
    unittest.main()