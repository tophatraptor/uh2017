#Maps the frequency of sound to the RGB value of the color

#Sound Freq -> RGB value (Int, Int, Int)
def toRGB(soundFreq):
    #for now just using this range from:
    #http://www.phy.mtu.edu/~suits/notefreqs.html
    soundFreqRange = 7900.
    colorFreqRange = 300.

    minSoundFreq = 20.
    maxSoundFreq = 6000.

    minColorWL = 400.
    maxColorWL = 700.

    #the color wave lengthh
    colorWL = (soundFreq - minSoundFreq)/19. + minColorWL
    
    #http://www.efg2.com/Lab/ScienceAndEngineering/Spectra.htm

    red = 0.
    green = 0.
    blue = 0.
    if (colorWL >= 380.) and (colorWL <= 439.):
        red = -(colorWL - 440.) / (440. - 380.)
        green = 0.
        blue = 1.
    elif (colorWL >= 440.) and (colorWL <= 489.):
        red = 0.
        green = (colorWL- 440.)/(490. - 440.)
        blue = 1.
    elif (colorWL >= 490.) and (colorWL <= 509.):
        red = 0.
        green = 1.
        blue = (colorWL- 510.)/(510. - 490.) 
    elif (colorWL >= 510.) and (colorWL  <= 579.):
        red = (colorWL - 510.)/(580.- 510.)
        green = 1.
        blue = 0.
    elif (colorWL >= 580.) and (colorWL <= 644.):
        red = 1.
        green = -(colorWL - 645.)/(645. - 580.)
        blue = 0.
    elif (colorWL >= 645.) and (colorWL <= 780.):
        red = 1.
        green = 0.
        blue = 0.
    else:
        red = 0.
        green = 0.
        blue = 0.
    factor = 0.
    if (colorWL >= 380.) and (colorWL <= 419.):
        factor = 0.3 +0.7 * (colorWL - 380.) / (420. - 380.)
    elif (colorWL >= 420.) and (colorWL <= 700.):
        factor = 1.
    elif (colorWL >= 701.) and (colorWL <= 780.):
        factor = 0.3 * 0.7 * (780. - colorWL) / (780. - 700.)
    else:
        factor = 0.

    red = 255 * (red * factor) ** 0.8
    green = 255 * (green * factor) ** 0.8
    blue = 255 * (blue * factor) ** 0.8

    return (red, green, blue)
    

    
