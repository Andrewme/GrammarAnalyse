import re

class Algorithms():
    def UnNTerminals(self, inputData):
        print "Unproductive not terminals"

        t_out = []
        t_in = []
        unproductive = []
        productive = []

        '''split by rows'''
        inputData = inputData.split("\n")

        t_out = self._SearchAfter(inputData)
        t_in = self._SearchBefore(inputData)

        productive = self._Productive(t_out, t_in)
        unproductive = self._UnProductive(productive, t_in)

        return unproductive

    def Follow(sef, inputData):
        followSet = []


        return followSet

    #Private methods
    def _SearchAfter(self, inputData):
        _t_out = []

        s_ter = re.compile(r"\w+ -> ")
        [_t_out.append(s_ter.split(inputData[i])[1]) 
                                              for i in range(0, len(inputData))]

        return _t_out

    def _SearchBefore(self, inputData):
        _t_in = []

        s_nter = re.compile(r"[^\w+ -> ]")
        [_t_in.append(s_nter.split(inputData[i][0])) 
                                              for i in range(0, len(inputData))]

        return _t_in

    '''# is Epsilon'''
    def _CharCase(self, data):
        if data.islower() or data == '#':
            return True
        else:
            return False

    def _CharCaseProductiv(self, data, product):
        check_lower = 0
        check_product = 0

        for i in range(len(data)):
            if data[i].islower():
                check_lower = 1
            if data[i] in product:
                check_product = 1

        if check_lower == 1 and check_product == 1:
            return True
        else:
            return False

    def _Productive(self, t_out, t_in):
        _productive = []

        for i in range(len(t_out)):
            if self._CharCase(t_out[i]):
                if t_in[i][0] not in _productive:
                    _productive.append(t_in[i][0])

        for i in range(len(t_out)):
            if self._CharCaseProductiv(t_out[i], _productive):
                if t_in[i][0] not in _productive:
                    _productive.append(t_in[i][0])

        return _productive

    def _UnProductive(self, productive, t_in):
        _unproductive = []

        for i in range(len(t_in)):
            if (t_in[i][0] not in productive) and (t_in[i][0] not in _unproductive):
                _unproductive.append(t_in[i][0])

        return _unproductive
