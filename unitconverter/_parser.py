'''
parser.py: parser class - parses a string into units and values.

Input strings are expected to be in the format "value unit to value". For
example: "6 m to yard" or "2.5 yd to inch". Parsing is performed using a simple
regular expression, which can be augmented to support other formats.

'''

# modules
import re

# regex used to perform the parsing
_re = re.compile(R'(?P<from_value>\d+(?:.\d+)?)\s*(?P<from_unit>\w+)\s*to\s*(?P'
                 R'<to_unit>\w+)', re.IGNORECASE)

def _Parser(string):
    m = _re.match(string)
    
    if not m:
        raise ValueError('unable to parse string ({0})'.format(string))
    
    return {
            'from_value' : m.group('from_value'),
            'from_unit' : m.group('from_unit').lower(),
            'to_unit' : m.group('to_unit').lower(),
            }