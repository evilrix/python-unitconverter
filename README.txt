==============
Unit Converter
==============

Specification:

Convert between length units
==============================

You are required to write a simple library that converts lengths in different
units. For example:

    6 m to yard = 6.562 yd
    2.5 yd to inch = 90 in

The units to be supported are: metre (m), yard (yd) and inch (in). The design
of the library should support adding new units easily.

It should also support representing the measures as user-friendly strings (e.g.,
"2.3 m", "6 yd", "0.4 in").

To keep things simple, capturing and handling user input is not required. So
parsing strings like "6 m to yd" isn't needed, unless you consider this to be a
useful development aid.

End-user documentation is not expected.

Rules
-----

This library should be implemented using:

- A high-level programming language (preferably Python).
- Test-Driven Development.

Description:

Unit Converter provides the ability to convert between different measurement
units. The interface is very simple, it requires a string input that describes
both the source unit, the source value and the destination unit.

E.g.

'6 m to yard = 6.562 yd'
'2.5 yd to inch = 90 in'

The output will be the result of the conversion in the requested units.

The following units are currently supported (case insensitive).

Yards: yd, yard, yards
Inches: in, inch, inches
Metre: m, meter, metre, meters, metres

Example (see UnitConverter/bin/main):

#!/usr/bin/env python

'''
main: example program showing how to use UnitConverter
'''

# modules
import unitconverter

# create instance of converter
converter = unitconverter.Converter()

# convert from a formatted string
print converter.convert('6 m to yd')
print converter.convert('6 m to in')
print converter.convert('36 in to m')
print converter.convert('36 in to yd')
print converter.convert('2 m to in')
print converter.convert('2 m to yd')
