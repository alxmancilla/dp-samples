class ImageFinder:
    """ Inteface / Abstract Class concept for readability. """

    def find(self, image):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, ImageFinder is supposed to be an interface / abstract class!')

class ImageFinderFlickr(ImageFinder):
    ''' Locates images in flickr'''

    def find(self, image):
        # in reality, query Flickr API for image path
        return "Found image in Flickr: " + image


class ImageFinderDatabase(ImageFinder):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return "Found image in database: " + image
    
    
    
if __name__ == "__main__" :

    finderBase = ImageFinder()
    finderFlickr = ImageFinderFlickr()
    finderDatabase = ImageFinderDatabase()

    try:
        #this is going to blow up!
        print(finderBase.find('chickens'))
    except NotImplementedError as e:
        print "The following exception was expected:"
        print e
        

    print finderFlickr.find('chickens')
    print finderFlickr.find('rabbits')
    print finderDatabase.find('dogs')
    print finderDatabase.find('cats')  
