class SimpleWorkout(object):
    cal_per_hr = 200
    def __init__(self,start,end,calories):
        self.start = start
        self.end = end
        self.calories = calories
        self.icon = ':)'
        self.kind = 'workout'

    def get_calories(self):
        return self.calories

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_calories(self, calories):
        self.calories = calories

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

my_workout = SimpleWorkout('3/22/2026 6:30 PM','3/22/2026 6:30 PM',200)
print(SimpleWorkout.__dict__.keys())
print(SimpleWorkout.__dict__.values())

class Workout(object):
    cal_per_hr = 200
    def __init__(self,start,end,calories=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = ':)'
        self.kind = 'workout'

    def get_calories(self):
        if self.calories is None:
            return Workout.cal_per_hr*(self.end-self.start).total_seconds()/3600
        else:
            return self.calories
        