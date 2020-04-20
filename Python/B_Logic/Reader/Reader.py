import os

from Reader.compressed import bzipped, gzipped

extentsion_map = {
    '.bz2' : bzipped.opener,
    '.gz' : gzipped.opener,
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extentsion_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()