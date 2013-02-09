'''
yard.py: handlers convertion to yard.
'''

from unitconverter._handler._base import _Base

class _Yards(_Base):

    @property
    def from_units(self):
        return {
                'yd' : 'yard',
                'yard' : 'yard',
                'yards' : 'yard',
                }

    @property
    def to_units(self):
        return {
                'm' : 'metre',
                'meter' : 'metre',
                'meters' : 'metre',
                'metre' : 'metre',
                'metres' : 'metre',
                'in' : 'inch',
                'inch' : 'inch',
                'inches' : 'inch',
                }
    
    @property
    def converter(self):
        return {
                # conversions according to Google
                'metre' : lambda x : x * 0.9144,
                'inch' : lambda x : x * 36,                           
                }
        
        
        
