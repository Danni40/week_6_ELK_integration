import logging
import logstash
import random
import sys

host = '18.224.55.196'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)

class Rectangle: #define the rectangle class
    def __init__(self, name, length, width):  #initiate the constructor and attributes
        self.name = name
        self.length = length
        self.width = width
        
        test_logger.info('Created Rectangle: {} - {}l:{}w'.format(self.name, self.length, self.width))
    
    def area(self):  #method to calculate the area of a rectangle
        area = self.length * self.width
        return area
       
    def is_square(self):  #method that returns true if rectangle is also a square / else - false
        if self.length == self.width:
            return True
        else:
            return False

        
#test cases
a1 = random.randrange(1, 100)
a2 = random.randrange(1, 100)
rect = Rectangle('Rect', a1, a2)
danni = Rectangle('Danni', random.randrange(1, 100), random.randrange(1, 100))
paula = Rectangle('Paula', random.randrange(1, 100), random.randrange(1, 100))
