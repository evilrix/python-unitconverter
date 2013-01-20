'''
inch.py: handlers convertion to yard.
'''

from unitconverter._handler._base import _Base

class _Inches(_Base):

    @property
    def from_units(self):
        return {
                'in' : 'inch',
                'inch' : 'inch',
                'inches' : 'inch',
                }

    @property
    def to_units(self):
        return {
                'm' : 'metre',
                'meter' : 'metre',
                'metre' : 'metre',
                'meters' : 'metre',
                'metres' : 'metre',
                'yd' : 'yard',
                'yard' : 'yard',
                'yards' : 'yard',
                }
        
    @property
    def converter(self):
        return {
                # conversions according to Google
                'metre' : lambda x : x * 0.0254,
                'yard' : lambda x : x * 0.0277778,                            
                }
