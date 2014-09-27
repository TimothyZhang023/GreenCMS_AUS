from django.test import TestCase
import models
# Create your tests here.

print '=================save and get======================'

models.Opinion.save_opinion('test_key1', 'test_value2')
print models.Opinion.get_opinion('test_key1')


print '===============get empty key========================'

print models.Opinion.get_opinion('test_key1')
print models.Opinion.get_opinion('test_key2')

print '=================del and get=========================='

print models.Opinion.del_opinion('test_key1')
print models.Opinion.get_opinion('test_key1')

print '=================save twice========================'

models.Opinion.save_opinion('test_key1', 'test_value2')
models.Opinion.save_opinion('test_key1', 'test_value2')

print '===================================================='
