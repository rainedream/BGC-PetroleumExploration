__author__ = 'YMeng3'

RESERVOIR_WIDTH = 96                # Reservoir dimension - number of cells – width Min:10 Max: 512
RESERVOIR_HEIGHT = 96               # Reservoir dimension - number of cells - height Min:10 Max: 512
RESERVOIR_BLOCKPRICE = 5000         # Cost of purchase of one cell of the reservoir Min:1000 Max: 100000
RESERVOIR_CAPACITY = 20000          # Total reservoir capacity spread aver the reservoir size
RESERVOIR_CELL_MAXCAPACITY = 10     # Maximum capacity for one cell

COST_OF_PRODUCTION = 1500            # Each producing cell will cost this amount until stopped

COST_OF_SERVICE_EXPLORE_SLB = 7500   # Cost of exploration service - Schlumberger
COST_OF_SERVICE_EXPLORE_HAL = 6500   # Cost of exploration service - Halliburton

NODE_INITIAL_MONEY = 1000000         # Initial money to start working with
OIL_UNIT_PRICE = 2500                # For each unit extracted, owner of rig will get this amount

COST_OF_SERVICE_DRILL_SLB = 20000    # Cost of drilling - Schlumberger
COST_OF_SERVICE_DRILL_HAL = 15000    # Cost of drilling - Halliburton

COST_OF_SERVICE_STIMULATE_SLB = 20000    # Cost of stimulation - Schlumberger
COST_OF_SERVICE_STIMULATE_HAL = 15000    # Cost of stimulation - Halliburton
