


#test the number of Translation unit
#number of en tags
#number of ids 
#check 
#--------------ideally they should all be the same number
import duplicateChecker
import unittest

class TestImages(unittest.TestCase):
    
    #creation of something which will be used often within a setUp method
    @classmethod
    def setUpClass(cls):
        path = "Pdf-Proofing/Sample/imageDetection/Unvalidated/Unvalidated/Trimble Roadworks Asphalt Compactor Operator_s Manual V2.11.xA (ENG).pdf"
        cls.images1 = duplicateChecker.noImages(path)
            
    #need to figure this function out
    @classmethod
    def tearDownClass(cls):
        pass
    
    #is the image empty?
    def test_isEmpty(self):
        self.assertTrue(self.images1!=0)
        self.assertTrue(self.images2!=0)
    
    def test_isDifferent(self):
        self.assertTrue(self.images1 != self.images2)
    
    
    


if __name__ == '__main__':
    unittest.main()