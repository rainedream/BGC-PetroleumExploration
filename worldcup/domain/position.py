from  worldcup.domain.states.state import State
from worldcup.domain.states.null import Null
from worldcup.domain.states.explored import Explored
from worldcup.domain.states.occupied import Occupied
from worldcup.domain.states.owned import Owned
from worldcup.domain.states.stimulated import Stimulated
from worldcup.domain.states.stopped import Stopped
from worldcup.domain.states.production import Production
from worldcup.domain.Cost import *
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = Null()
        self.expected_volume = 0
        self.produced_volume = 0
        self.produced_at_last_run = 0
        self.stimulation_has_effect = False

    def UpdateProduction(self, newTotalProductionVolume):
        self.produced_at_last_run = newTotalProductionVolume - self.produced_volume
        self.produced_volume = newTotalProductionVolume

    def UpdateStatus(self, lastOperation, lastOperationStatus, value):
        if lastOperationStatus == 'False':
            if lastOperation == "Buy":
                self.state = Occupied()
            elif lastOperation == "Explore":
                self.state = Production()
            elif lastOperation == "Drill":
                self.state = Production()
            elif lastOperation == "Stimulate":
                self.state = Production()
            elif lastOperation == "StopProduction":
                self.state = Stopped()
        else:
            if lastOperation == "Buy":
                self.state = Owned()
            elif lastOperation == "Explore":
                self.state = Explored()
                self.expected_volume = int(float(value))
            elif lastOperation == "Drill":
                self.state = Production()
                self.expected_volume = int(float(value))
            elif lastOperation == "Stimulate":
                self.state = Stimulated()
                self.expected_volume = int(float(value))
            elif lastOperation == "StopProduction":
                self.state = Stopped()

    def IsBelowProfit(self):
        return ( self.IsDrilling() or self.IsStimulated() ) and self.produced_at_last_run * OIL_UNIT_PRICE < COST_OF_PRODUCTION # less than the production cost

    def IsBelowProfitProactive(self):
        return ( self.IsDrilling() or self.IsStimulated() ) and self.produced_at_last_run * OIL_UNIT_PRICE < COST_OF_PRODUCTION * 2 # less than the production cost

    def IsExplored(self):
        return isinstance(self.state,Explored)

    def IsPurchased(self):
        return isinstance(self.state,Owned)

    def IsStimulated(self):
        return isinstance(self.state,Stimulated)

    def IsDrilling(self):
        return isinstance(self.state,Production)

    def IsAvailable(self):
        return isinstance(self.state, Null)

    def IsOccupied(self):
        return isinstance(self.state, Occupied)

class ProductionInfo:
    def __init__(self, x, y, productionVolume):
        self.x = x
        self.y = y
        self.productionVolume = productionVolume


