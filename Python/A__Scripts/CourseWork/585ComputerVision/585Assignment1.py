import math
import cv2
import numpy as np


class HistogramEqualization:
    def __init__(self):
        self.levelsOfGrayScaleL = 256
        self.heapOfPixels = []

        self.image = cv2.imread("Unequalized_Hawkes_Bay_NZ.jpg")
        (self.imageHeight, self.imageWidth, d) = self.image.shape

        self.numberOfPixelsInImageN = len(self.image)
        self.abreviatedPixelDictionaryPercentage = dict()
        self.abreviatedPixelDictionary = dict()
        self.abreviatedCDV = dict()
        self.totalPercent = 0
        self.currentDistribution = 0
        self.heapOfPixelsCDV = []

        #Create the pixel heapsort
        self.PixelHeapConstructor()

        #print("The Pixel Heap: ", self.heapOfPixels)
        #print(self.heapOfPixels)

        #CreateCDV values from the heapsort
        self.CreateCDVValues()

        self.min = self.Min(self.heapOfPixelsCDV)
        self.imageArea = self.imageHeight * self.imageWidth
        self.equalizedValue = []
        self.abreviatedEqualizedValue = dict()

        #print(self.heapOfPixelsCDV)
        #Create the Equalized Values
        self.EqualizedValues()

        #print(self.equalizedValue)
        #initialize your dictionaries for ease of look up
        self.initalizeDictionaries()

        #print("Abreviated Pixel Heap: ", self.abreviatedPixelDictionary)
        #print("Pixel Percentage: ", self.abreviatedPixelDictionaryPercentage)
        #print("Total Percent:", self.totalPercent)
        #print("Abreviated CDV: ", self.abreviatedCDV)
        #print("Abreviated Equalized Value: ", self.abreviatedEqualizedValue)

        #Create replace your values from the original image with your equalized values
        self.EqualizedValueReplacement()

        #display images
        cv2.imshow('Original Image', self.image)
        cv2.imshow('New Image', self.newImage)
        cv2.waitKey()

        #print("Image with equalization: ", self.image)

    def EqualizedValueReplacement(self):
        self.newImage = self.image.copy()
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                for c in range(self.image.shape[2]):
                    try:
                        self.newImage[y, x, c] = self.abreviatedEqualizedValue[self.image[y, x, c]]
                    except:
                        self.newImage[y, x, c] = 0

    def initalizeDictionaries(self):
        for number in range(0, len(self.heapOfPixels)):
            if (self.heapOfPixels[number] == 0):
                continue
            else:
                self.abreviatedPixelDictionary[number] = self.heapOfPixels[number]
                self.currentPercent = round(self.heapOfPixels[number] / self.numberOfPixelsInImageN * 100, 1)
                self.totalPercent = self.totalPercent + self.currentPercent
                self.abreviatedPixelDictionaryPercentage[number] = \
                    str(self.currentPercent) + '%'
                self.abreviatedCDV[number] = self.heapOfPixelsCDV[number]
                self.abreviatedEqualizedValue[number] = self.equalizedValue[number]

    def EqualizedValues(self):
        for number in self.heapOfPixelsCDV:
            tempEqualizedValue = round((number - self.min) / (self.imageArea - self.min) *
                                       (self.levelsOfGrayScaleL - 1))
            self.equalizedValue.append(tempEqualizedValue)

    def CreateCDVValues(self):
        for number in range(0, len(self.heapOfPixels)):
            self.currentDistribution = self.currentDistribution + self.heapOfPixels[number]
            self.heapOfPixelsCDV.append(self.currentDistribution)

    def PixelHeapConstructor(self):
        for i in range(0, self.levelsOfGrayScaleL):
            self.heapOfPixels.append(0)
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                for c in range(self.image.shape[2]):
                    self.heapOfPixels[self.image[y, x, c]] = self.heapOfPixels[self.image[y, x, c]] + 1
        for y in range(len(self.heapOfPixels)):
            self.heapOfPixels[y] = round(self.heapOfPixels[y] / 3)

    def Min(self, array):
        arrayLen = len(array) - 1
        smallest = array[arrayLen]
        for number in array:
            if number == 0:
                continue
            elif smallest > number:
                smallest = number
        return smallest

    def Max(self, array):
        largest = array[0]
        for number in array:
            if largest < number:
                largest = number
        return largest

    #\ p_{x}(i)=p(x=i)={\frac {n_{i}}{n}},\quad 0\leq i<L
    #{\displaystyle \ cdf_{x}(i)=\sum _{j=0}^{i}p_{x}(x=j)},


def problem2():
    """Implement the Histogram Equilization according to the explanation in the Wikipedia article.
        https://en.wikipedia.org/wiki/Histogram_equalization"""
    histogram = HistogramEqualization()

problem2()