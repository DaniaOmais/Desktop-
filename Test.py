{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import unittest \
from math_operations import add \
\
class TestMathOperations(unittest.TestCase): \
	def test_add(self):\
		self.assertEqual(add(1, 2), 3) \
		self.assertEqual(add(-1, 1), 0) \
		self.assertEqual(add(-1, -1), -2) \
		self.assertEqual(add(0, 0), 0) \
\
if __name__ == '__main__': \
	unittest.main()}
	print ("ello World")