

import numpy as np

###################### import ##################


class BackPropagationNetwork:

    ###
    ###class memebers
    ###
    layercount = 0
    shape = None
    weight = []


    #
    ### class methods
    #
    def __init__(self,layersize):
        ### initialize the method ###
        self.layercount= len(layersize)-1
        self.shape = layersize


        #### input /output ####
        self._layerInput = []
        self._layerOutput = []

        ## creation of weighted arrays
        for (l1, l2) in zip(layersize[:-1], layersize[1:]):
            self.weight.apphend()

if __name__ == "__main__":
    bpn = BackPropagationNetwork(())
    print (bpn.shape)
    print (bpn.weight)
    
