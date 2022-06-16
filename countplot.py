class CountPlot:
    """ 
    Barplot Graph showing the Count and Percentage of Categorical Variables. 
    
    TODO: Specify the design paramenters in the class instance and the data parameters in the display mehtod.
    """
    def __init__(self, data, order = None, title_sentence = None, position = 'right' ):
        self.data = data
        self.order = order
        self.title_sentence = title_sentence
        self.position = position
    

    def display(self):
        """ 
        Displaying the Graph.
        """

        frequencies = self.data.value_counts()
        len_frequencies = len(self.data.value_counts())
        total = float(len(self.data))

        if (len_frequencies > 15) and ((frequencies.min()/frequencies.max())<0.1):
            """ Condition the number of Vardiables to appear. """
        
            mask_obs = frequencies[15:].index
            mask_dict = dict.fromkeys(mask_obs, 'other')
            new_data = self.data.replace(mask_dict) 
            assert new_data.shape == self.data.shape
    
        else :
            new_data = self.data

        if self.order is None:
            """ Specify the order of appearance of Variables in x axis. Default order is sorted ascedning.  """
            self.order = new_data.value_counts().index
        else:
            self.order = self.order

        if self.title_sentence is None:
            """ Specify the title of the Graph.  """
            pass
        else:
            plt.title(self.title_sentence, fontsize=20)
    
        ax = sns.countplot(x = new_data, order = self.order)

        for p in ax.patches:
            percentage = '{:.1f}%'.format(100 * p.get_height()/total)
            x = p.get_x() + p.get_width()
            y = p.get_height()
            ax.annotate(percentage, (x, y), ha = self.position )
            ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha= self.position )
            plt.tight_layout()
        plt.show()
