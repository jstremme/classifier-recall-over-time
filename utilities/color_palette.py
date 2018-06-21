class ColorPalette():

    def __init__(self):

        color_dict = {'background': '#FFEBCD',
          		  	  'text': '#000080',
                      'recalled': '#4682B4',
                      'diagnosed': '#ADD8E6'}
        self.colors = color_dict
        self.background = color_dict['background']
        self.text = color_dict['text']
        self.recalled = color_dict['recalled']
        self.diagnosed = color_dict['diagnosed']
        
    def get_colors(self):

        return self.colors

if __name__ == '__main__':

    palette = ColorPalette()
    print(palette.get_colors())
    print(palette.text)