'''
metre.py: handlers convertion to metres.
'''

from unitconverter._handler._base import _Base

class _Metres(_Base):
    
    @property
    def from_units(self):
        return {
                'm' : 'metre',
                'meter' : 'metre',
                'metre' : 'metre',
                'meters' : 'metre',
                'metres' : 'metre',
                }


    @property
    def to_units(self):
        return {
                'yd' : 'yard',
                'yard' : 'yard',
                'yards' : 'yard',
                'in' : 'inch',
                'inch' : 'inch',
                'inches' : 'inch',
                }
        
        
    @property
    def converter(self):
        return {
                # conversions according to Google
                'yard' : lambda x : x * 1.0936133,
                'inch' : lambda x : x * 39.3700787,                           
                }


        
