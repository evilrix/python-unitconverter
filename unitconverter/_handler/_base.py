'''
_base.py: base class for conversion handlers.
'''

# allows us to create an abstract base class
import abc

class _Base(object):
    __metaclass__ = abc.ABCMeta
    
    def can_handle(self, parsed):
        return (parsed['from_unit'] in self.from_units and
                parsed['to_unit'] in self.to_units)

    @abc.abstractproperty
    def from_units(self):
        None

    @abc.abstractproperty
    def to_units(self):
        None
        
    @abc.abstractproperty
    def converter(self):
        None

    @property
    def name(self):
        return self.__class__.__name__[1:].lower()

    def __call__(self, parsed):
        to_unit = self.to_units[parsed['to_unit'].lower()]
        from_value = float(parsed['from_value'])
        
        return self.converter[to_unit](from_value)
