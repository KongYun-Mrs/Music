import re

from django.test import TestCase

# Create your tests here.

str = 'rewards_points/1321325/'

print(re.match(r'[\w_]+/(\d+)/', str).group(1))