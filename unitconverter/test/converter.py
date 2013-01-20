'''
converter.py: test suite for converter class

This test can be run using PyUnit's test discovery from the comment line.

> cd project_directory
> python -m unittest discover

NB. For the sake of simplicity we are only testing the conversion of a single
    unit value. Were this real production code it would probably be an idea to 
    add some auto-generated data tests that test a range of values for each unit
    type and check that the conversion process was successful. For the purposes
    of this coding exercise I believe that this is adequate to demonstrate my
    general appreciation for writing unit tests using PyUnit.
'''

import unittest
import unitconverter

class ConverterTestCase(unittest.TestCase):
    
    def setUp(self):
        self.__converter = unitconverter.Converter()
    
    def testFromMetresToYards(self):
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 m to yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 m to yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 m to yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 meter to yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 meter to yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 meter to yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 metre to yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 metre to yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 metre to yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 meters to yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 meters to yard'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 metres to yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 metres to yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 metres to yards'))

    def testFromMetresToInches(self):
        self.assertEquals('39.3700787 in', self.__converter.convert('1 m to in'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 m to inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 m to inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 meter to in'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 meter to inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 meter to inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 metre to in'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 metre to inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 metre to inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 meters to in'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 meters to inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 meters to inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 metres to in'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 metres to inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 metres to inches'))

    def testFromYardsToInches(self):
        self.assertEquals('36.0 in', self.__converter.convert('1 yd to in'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yd to inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yd to inches'))
        self.assertEquals('36.0 in', self.__converter.convert('1 yard to in'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yard to inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yard to inches'))
        self.assertEquals('36.0 in', self.__converter.convert('1 yards to in'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yards to inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yards to inches'))

    def testFromYardsToMetress(self):
        self.assertEquals('0.9144 m', self.__converter.convert('1 yd to m'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yd to meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yd to metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yd to meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yd to metres'))
        self.assertEquals('0.9144 m', self.__converter.convert('1 yard to m'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yard to meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yard to metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yard to meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yard to metres'))
        self.assertEquals('0.9144 m', self.__converter.convert('1 yards to m'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yards to meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yards to metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yards to meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yards to metres'))
        
    def testFromInchesToYards(self):
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 in to yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 in to yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 in to yards'))        
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 inch to yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 inch to yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 inch to yards'))
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 inches to yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 inches to yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 inches to yards'))
        
    def testFromInchesToMetress(self):
        self.assertEquals('0.0254 m', self.__converter.convert('1 in to m'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 in to meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 in to metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 in to meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 in to metres'))
        self.assertEquals('0.0254 m', self.__converter.convert('1 inch to m'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 inch to meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 inch to metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 inch to meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 inch to metres'))
        self.assertEquals('0.0254 m', self.__converter.convert('1 inches to m'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 inches to meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 inches to metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 inches to meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 inches to metres'))

    def testFromMetresToYardsMixedCase(self):
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 M to Yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 M to Yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 M to Yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 Meter to Yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 Meter to Yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 Meter to Yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 Metre to Yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 Metre to Yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 Metre to Yards'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 Meters to Yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 Meters to Yard'))
        self.assertEquals('1.0936133 yd', self.__converter.convert('1 Metres to Yd'))
        self.assertEquals('1.0936133 yard', self.__converter.convert('1 Metres to Yard'))
        self.assertEquals('1.0936133 yards', self.__converter.convert('1 Metres to Yards'))

    def testFromMetresToInchesMixedCase(self):
        self.assertEquals('39.3700787 in', self.__converter.convert('1 M to In'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 M to Inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 M to Inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 Meter to In'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 Meter to Inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 Meter to Inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 Metre to In'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 Metre to Inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 Metre to Inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 Meters to In'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 Meters to Inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 Meters to Inches'))
        self.assertEquals('39.3700787 in', self.__converter.convert('1 Metres to In'))
        self.assertEquals('39.3700787 inch', self.__converter.convert('1 Metres to Inch'))
        self.assertEquals('39.3700787 inches', self.__converter.convert('1 Metres to Inches'))

    def testFromYardsToInchesMixedCase(self):
        self.assertEquals('36.0 in', self.__converter.convert('1 yd to In'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yd to Inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yd to Inches'))
        self.assertEquals('36.0 in', self.__converter.convert('1 yard to In'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yard to Inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yard to Inches'))
        self.assertEquals('36.0 in', self.__converter.convert('1 yards to In'))
        self.assertEquals('36.0 inch', self.__converter.convert('1 yards to Inch'))
        self.assertEquals('36.0 inches', self.__converter.convert('1 yards to Inches'))

    def testFromYardsToMetressMixedCase(self):
        self.assertEquals('0.9144 m', self.__converter.convert('1 yd to M'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yd to Meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yd to Metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yd to Meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yd to Metres'))
        self.assertEquals('0.9144 m', self.__converter.convert('1 yard to M'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yard to Meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yard to Metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yard to Meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yard to Metres'))
        self.assertEquals('0.9144 m', self.__converter.convert('1 yards to M'))
        self.assertEquals('0.9144 meter', self.__converter.convert('1 yards to Meter'))
        self.assertEquals('0.9144 metre', self.__converter.convert('1 yards to Metre'))
        self.assertEquals('0.9144 meters', self.__converter.convert('1 yards to Meters'))
        self.assertEquals('0.9144 metres', self.__converter.convert('1 yards to Metres'))
        
    def testFromInchesToYardsMixedCase(self):
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 In to Yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 In to Yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 In to Yards'))        
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 Inch to Yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 Inch to Yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 Inch to Yards'))
        self.assertEquals('0.0277778 yd', self.__converter.convert('1 Inches to Yd'))
        self.assertEquals('0.0277778 yard', self.__converter.convert('1 Inches to Yard'))
        self.assertEquals('0.0277778 yards', self.__converter.convert('1 Inches to Yards'))
        
    def testFromInchesToMetressMixedCase(self):
        self.assertEquals('0.0254 m', self.__converter.convert('1 In to M'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 In to Meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 In to Metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 In to Meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 In to Metres'))
        self.assertEquals('0.0254 m', self.__converter.convert('1 Inch to M'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 Inch to Meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 Inch to Metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 Inch to Meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 Inch to Metres'))
        self.assertEquals('0.0254 m', self.__converter.convert('1 Inches to M'))
        self.assertEquals('0.0254 meter', self.__converter.convert('1 Inches to Meter'))
        self.assertEquals('0.0254 metre', self.__converter.convert('1 Inches to Metre'))
        self.assertEquals('0.0254 meters', self.__converter.convert('1 Inches to Meters'))
        self.assertEquals('0.0254 metres', self.__converter.convert('1 Inches to Metres'))
