import redis

NR_OF_LIGHTS = 2

class LightState:
 
    def __init__(self, redis_host, redis_port, redis_db, redis_pass):
        self.state = "00"
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_pass)

    def getState(self):
        state = self.redis.get('state')
        if state is None:
            state = '00'
        return LightState.__strings_to_bools(state)

    def setState(self, bools):
        self.redis.set('state', LightState.__bools_to_string(bools))

    def toggle(self, position):
        state = self.redis.get('state')
        if state is None:
            state = '00'
        bools = LightState.__strings_to_bools(state)
        bools[position] = not bools[position]
        self.setState(bools)

    @staticmethod
    def __strings_to_bools(state_str):
        bools = []
        for char in state_str:
            if char == "0":
                bools.append(False)
            else:
                bools.append(True)
        return bools

    @staticmethod
    def __bools_to_string(bools):
        state_str = ""
        for boolean in bools:
            if boolean:
                state_str = state_str + "1"
            else:
                state_str = state_str + "0"
        return state_str