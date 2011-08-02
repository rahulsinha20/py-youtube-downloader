'''
Created on 02/08/2011

@author: asinha
'''

class ApplicationException(Exception):
    '''
    Application Based Exception
    '''

    def __init__(self, value):
        '''
        Constructor
        '''
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        