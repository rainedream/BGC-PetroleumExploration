from worldcup.domain_s2.state import *


class RandomExploration:
    lastAction = None
    
    def __init__(self, block_map):
        self.block_map = block_map

    def do(self, last_operation_status):
        if not last_operation_status:
            current_state = Null(self.block_map)
        else:
            current_state = self.recover_state(RandomExploration.lastAction, parse_to_bool(last_operation_status))
        RandomExploration.lastAction = current_state.next_action()
        return RandomExploration.lastAction

    def recover_state(self, last_action, is_last_action_success):
        if last_action.type == ActionType.BUY:
            if is_last_action_success:
                return Owned(self.block_map, last_action.x, last_action.y)
            else:
                return Occupied(self.block_map, last_action.x, last_action.y)


def parse_to_bool(text):
    if text.lower() == 'true':
        return True
    return False