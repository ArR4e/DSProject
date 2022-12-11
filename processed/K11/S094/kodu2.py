# Kasutame numpy-t et saada tavaline maatriks, seejärel ta vastupidiseks
# töödelda.
import numpy

def transponeeriK(maatriks):
    transponeeritud = numpy.transpose(maatriks)
    # pöörame eelmise listi vastupidi.
    vastupidi = transponeeritud[::-1]
    # reversime eelmiselt saadud rea et saada tulemus
    tulemus = numpy.fliplr(vastupidi)
    return tulemus