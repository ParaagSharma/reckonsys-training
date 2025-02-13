class FileManager():
    '''
        Write a simple context manager that opens a file, 
        writes some text into it, and then automatically closes 
        it when the context is exited. Use the with statement to 
        manage the file handling.
    '''
    
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('Opening file...')
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        print('Closing file...')
 

with FileManager('hello.txt', 'a') as f:
    f.write('\nContext Manager')