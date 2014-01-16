import urllib,urllib2,requests

def get_example_images():
    f = fits.open('/Users/willettk/Astronomy/Research/GalaxyZoo/ukidss/gz2_ukidss.fits')
    gu = f[1].data
    f.close()
    
    for name in gu.names[3:]:                                                           
        flagged = gu['dr7objid_1'][(gu[name] == 1) & (gu['Hmag'] < 16)]
        for f in flagged[:10]:
            url = 'http://www.sdss.org.uk/ukidsszoo/%s_.jpg' % f
            newname = '/Users/willettk/Desktop/ukidss_helpimages/%s_%s.jpg' % (name[:-5],f)
            r = requests.get(url)
            with open(newname,'wb') as code:
                code.write(r.content)

    return None

if __name__ == '__main__':
    get_example_images()
