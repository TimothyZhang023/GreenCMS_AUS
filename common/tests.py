from django.test import TestCase
import models


class OpinionModelsTestCase(TestCase):
    def setUp(self):
        pass

    def test_save_opinion(self):
        models.Opinion.save_opinion('test_key1', 'test_value2')
        print models.Opinion.get_opinion('test_key1')

    def test_save_twice_opinion(self):
        models.Opinion.save_opinion('test_key1', 'test_value2')
        models.Opinion.save_opinion('test_key1', 'test_value2')

    def test_get_opinion(self):
        print models.Opinion.get_opinion('test_key1')
        print models.Opinion.get_opinion('test_key2')

    def test_delete_opinion(self):
        #print models.Opinion.del_opinion('test_key1')
        #print models.Opinion.get_opinion('test_key1')
        pass
