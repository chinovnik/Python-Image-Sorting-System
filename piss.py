# Python Image Sorting System (PISS)
# by Roman Gelman

import os
from exif import Image
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

extensions = ['.mov']
images = [f for f in os.listdir(os.getcwd()) if os.path.splitext(f)[1].lower() in extensions]

for image in images:
    print(f"Sorting {image}")
    with open(image, 'rb') as i:
        #meta = Image(i)
        #print(meta.has_exif)
        try:
            parser = createParser(image)
            metadata = extractMetadata(parser)
            print(metadata.get('creation_date'))
        except:
            pass