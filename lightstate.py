import redis

NR_OF_LIGHTS = 2

class LightState:
 
    def __init__(self, redis_host, redis_port, redis_db, redis_pass):
        self.state = "00"
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_pass)

    def getState():
        return LightState.__strings_to_bools(redis.get('state'))

    def setState(bools):
        redis.set('state', LightState.__bools_to_string(bools))

    @staticmethod
    def __strings_to_bools(state_str):
        bools = []
        for char in state_str:
            if char == "0":
                bools = bools + False
            else:
                bools = bools + True
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