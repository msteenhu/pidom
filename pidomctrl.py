import gpio
import lightstate



class PidomCtrl:
    def __init__(self, switches, persistent_state, redis_host, redis_port, redis_db, redis_password):
        self.switches = switches
        self.persistent_state = persistent_state
 
        self.light_state = lightstate.LightState(
            redis_host=redis_host, redis_port=redis_port, 
            redis_db=redis_db, redis_pass=redis_password)
        self.output = gpio.Output()

    def __getPersistedLocation(self, switch_id):
        pos = 0
        while pos < len(self.persistent_state):
            if self.persistent_state[pos] == switch_id:
                return pos
            pos = pos + 1

        if pos == len(self.persistent_state):
            return -1 # not found

        return pos
    

    def pulse(self, switch_id, duration = None, set_state = True):
        if duration:
            self.output.pulse(self.switches[switch_id], duration)
        else:
            self.output.pulse(self.switches[switch_id])

        # if switch state persisted, adjust state
        if set_state and switch_id in self.persistent_state:
            position = self.__getPersistedLocation(switch_id)
            self.light_state.toggle(position)

    def enforce0(self):
        '''Set real life to state 0..0'''
        self.pulse('persistedoff')
    def enforce1(self):
        '''Set real life to state 1..1'''
        self.pulse('persistedon')

    def getState(self):
        return self.light_state.getState()

    def setState(self, state):
        self.light_state.setState(state)
        
        # sync real life to 0..0
        self.enforce0()

        # Put on lights according to state
        pos = 0
        while pos < len(self.persistent_state):
            if state[pos]:
                self.pulse(self.persistent_state[pos], set_state=False)
            pos = pos +1

        return state