class Clock:

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds // 60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes // 60)) % 24

    def print_clock(self):
        print('{:02d} : {:02d} : {:02d}'.format(self.hours, self.minutes, self.seconds))

    def add_clocks(self, clock2):
        seconds = self.seconds + clock2.seconds
        minutes = self.minutes + clock2.minutes
        hours = self.hours + clock2.hours
        return Clock(hours, minutes, seconds)

my_clock = Clock()
print('My clock is: ', my_clock)
print('Type is:', type(my_clock))
print(dir(my_clock))

new_clock = Clock(10, 15, 30)
new_clock.print_clock()
tst_clock = Clock(23, 59, 60)
tst_clock.print_clock()
c1 = Clock(10, 59, 59)
c2 = Clock (1, 1, 1)
c3 = c1.add_clocks(c2)
c1.print_clock()
c2.print_clock()
c3.print_clock()