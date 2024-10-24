import datetime

class Contagem():
    def __init__(self):
        self.__x = datetime.datetime.now()
        self._lunch = 12
        self.__go_out = 16
        self.__go_out_minut = 50
        self.get_day_of_week()
        self.get_hour_of_day()
        
    def get_day_of_week(self):
        if self.__x.strftime('%A') == 'Monday':
            print('Monday is a new beginning. Make it count! Start each day with a smile and a grateful heart')
            print('Believe you can and you`re halfwat there')
        if self.__x.strftime('%A') == 'Tuesday':
            print('Tuesday is the perfect day to tackle your goals.')
            print('You are capable of more than you know')
        if self.__x.strftime('%A') == 'Wednesday':
            print('Wednesday, Every challenge is an opportunity to grow Stay focused on your path')
        if self.__x.strftime('%A') == 'Thursday':
            print('Thursday is the day to celebrate progress and is almost Friday.')
        if self.__x.strftime('%A') == 'Friday':
            print('Friday is the day to relax and recharge, Look forward to a fantastic weekend.')        

    def get_hour_of_day(self):
        if self.__x > datetime.datetime.combine(self.__x.date(), datetime.time(self._lunch ,0)):
            print('Just passed the lunch time, Thank GOD!!!!')
            print('')
        else:            
            time_left = str(datetime.datetime.combine(self.__x.date(), datetime.time(self._lunch ,0)) - self.__x)
            hour, minut, second  = time_left.split(':')
            if hour == '0':
                if minut == '1':
                    print('Calm down little grasshopper, there are {} minut left for lunch'.format(minut))
                else:
                    print('Calm down little grasshopper, there are {} minuts left for lunch'.format(minut))
            elif hour == '1':
                if minut == '1':
                    print('Calm down little grasshopper, there are {} hour e {} minut left for lunch'.format(hour, minut))
                else:
                    print('Calm down little grasshopper, there are {} hour e {} minuts left for lunch'.format(hour, minut))
            else:
                print('Calm down little grasshopper, there are {} hours e {} minuts left for lunch'.format(hour, minut))
            print('')
        if not self.__x > datetime.datetime.combine(self.__x.date(), datetime.time(self.__go_out ,self.__go_out_minut)):
            time_left = str(datetime.datetime.combine(self.__x.date(), datetime.time(self.__go_out ,self.__go_out_minut)) - self.__x)
            hour, minut, second = time_left.split(':')
            if hour == '0':
                if minut == '1':
                    print('And left {} minut to go home'.format(hour, minut))
                else:
                    print('And left {} minuts to go home'.format(hour, minut))
            elif hour == '1':
                if minut == '1':
                    print('And left {} hour and {} minut to go home'.format(hour, minut))
                else:
                    print('And left {} hour and {} minuts to go home'.format(hour, minut))
            else:
                print('And left {} hours and {} minuts to go home'.format(hour, minut))
cont = Contagem()
cont
