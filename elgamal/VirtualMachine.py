class VirtualMachine():
    '''A very simple class that represents a machine's data. 
       It just has a name and owns objects (PrivateScalars and Shares).'''
    def __init__(self, name):
        self.name = name
        self.objects = []
    
    def __repr__(self):
        return f'VirtualMachine(\'{self.name}\')\n - ' + '\n - '.join(map(str, self.objects))