import settings

#this file used to calculate % of our heights and widths so we
# get consisntent scaled varaibles instead of hard coded values

def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage):
    return(settings.WIDTH / 100) * percentage
