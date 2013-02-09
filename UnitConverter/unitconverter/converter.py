'''
converter.py: convertor class - manages the conversion handers.
'''

# standard modules
import inspect

# local private modules
import _handler
from unitconverter._parser import _Parser

# classes
class Converter(object):
    
    def __init__(self):
        self.__handlers = [_handler.__dict__[x]() for x in dir(_handler) 
                           if inspect.isclass(_handler.__dict__[x])]
    
    def convert(self, string, throw_on_fail = False):
        parsed = _Parser(string)
        
        for handler in self.__handlers:
            if handler.can_handle(parsed):
                return '{0} {1}'.format(handler(parsed), parsed['to_unit'])
        
        if throw_on_fail:
            raise NotImplementedError(
                'Conversion unsupported ({0})'.format(string))

        return None