import sys
import re
import datetime



class SpeedCamProcess:
    def __init__(self, limits):
        self.speed_limit_s = 120
        self.speed_limit_c = 80
        self.limits = limits
        self.list = parser_input()
        
        
    def parser_input(self):
        factors = self.limits.split()
        try factors_dict = { 'numbers': data[0],
                         'type': data[1],
                         'distance': float(data[2]),
                         'in_time': datetime.strptime(data[3], '%H:%M')
                         'out_time': datetime.strptime(data[4], '%H:%M')
                         }:
             
            return data_dict
        
        except ValueError:
            return {'BLAD': 'niepoprawny typ danych'}
        except TypeError:
            return {'BLAD': 'inny oczekiwany typ danych dotyczacych odleglosci'}
        except IndexError:
            return {'BLAD': 'bledna kolejnosc wprowadzania danych lub ich liczba'}
        

    def if_proper(self):
        if 'BLAD' in self.list:
            proper = FALSE
            if self.list['numbers'][0:2].isalpha():
                proper = TRUE
            if self.list['numbers'][2:6].isdigit() or len(self.list['numbers'][2:6]) = 4:
                proper = TRUE
            if self.list['type'] in ['S', 'C']:
                proper = TRUE
            if re.match('^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$'), self.list['in_time'] or re.match('^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$', self.list['out_time']):
                proper = TRUE
                        
        else:
            proper = TRUE
                    
            return proper

                
   def speed_analyzing(self):
        if self.if_proper():
            distance = self.list['distance']
            time = (self.list['out_time'] - self.list['in_time']).seconds
            vel = (distance / time) * 3.6

            return vel
        
        else:
            return 'BLAD'
    
    def output(self):
        vel = self.speed_analyzing()
        
            if speed != 'BLAD':
                if self.list['type'] == 'S' and vel <= 140:
                    return str(self.list['numbers']) + ' . ' + "{:.2f}".format(vel)
                elif self.list['type'] == 'S' and vel > 140:
                    return str(self.list['numbers']) + ' M ' + "{:.2f}".format(vel)
                elif self.list['type'] == 'C' and vel <= 80:
                    return str(self.list['numbers']) + ' . ' + "{:.2f}".format(vel)
                elif self.list['type'] == 'C' and vel > 80:
                    return str(self.list['numbers']) + ' M ' + "{:.2f}".format(vel)

            else: return 'BLAD'


    
    if __name__ == '__main__':

        print('wprowadz x aby zakonczyc')
        
        for line in sys.stdin:
            if line == 'x\n':
                break
            else: a = SpeedCamProcess(line)

                print(a.output())
