from worldcup.domain_s2.state import *


class RandomExploration:
    lastAction = None
    
    def __init__(self, block_map):
        self.block_map = block_map

    def do(self, last_operation_status, last_operation_value):
        if not last_operation_status:
            current_state = Null(self.block_map)
        else:
            current_state = self.recover_state(RandomExploration.lastAction, parse_to_bool(last_operation_status), last_operation_value)
        RandomExploration.lastAction = current_state.next_action()
        return RandomExploration.lastAction

    def recover_state(self, last_action, is_last_action_success, last_operation_value):
        if last_action.type == ActionType.BUY:
            if is_last_action_success:
                return Owned(self.block_map, last_action.x, last_action.y)
            else:
                return Occupied(self.block_map, last_action.x, last_action.y)
        elif last_action.type == ActionType.EXPLORE:
            if is_last_action_success:
                return Explored(self.block_map, last_action.x, last_action.y, int(last_operation_value))
            else:
                # TODO: insufficient funds
                pass
        elif last_action.type == ActionType.DRILL:
            if is_last_action_success:
                return Production(self.block_map, last_action.x, last_action.y)
            else:
                # TODO: insufficient funds
                pass


def parse_to_bool(text):
    if text.lower() == 'true':
        return True
    return False