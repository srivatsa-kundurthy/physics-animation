class Stats(object):

    def update(self):
        pass

    def getcard(self, details):
        """
        :param details: a list of lists of length 2 in the format [name, item]
        :return: string of formatted details
        """
        string = ''
        for elem in details:
            string += str(elem[0]) + ': ' + str(elem[1]) + '\n'


        return string



