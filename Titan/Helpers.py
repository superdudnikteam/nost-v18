import string
import random
import time

class Helpers:
    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self):
        length = 6
        return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))

    def randomClubID(self):
        length = 9
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def Timer(self):
        result = time.localtime(int(time.time()))
        return (86400 - (result.tm_sec + (result.tm_min * 60) + (result.tm_hour * 3600)))