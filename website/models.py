class Member:
    # status
    baby = 1
    technician = 2
    senior_technician = 3
    manager_technician = 4

    # kind
    man = 32
    woman = 24

    #
    daily = 5
    weekly = 6

    def __init__(self, first_name, last_name, kind, m_a, job, departures):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__kind = kind
        self.__m_a = m_a
        self.__job = job
        self.__departures = departures

    def str(self):
        txt = "שם: " + self.__first_name + ",שם משפחה: " + self.__last_name + ", מין: " + self.__kind
        txt += ", מ.א: " + self.__m_a + ", תואר: " + self.__job + ", יציאות: " + self.__departures
        return txt


'''
import datetime

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


class Duty:

    __i = 13

    def __init__(self, name, count, loc):
        self.__name = name
        self.__count = count
        self.__loc = loc

    def get_loc(self):
        return self.__loc

    def str(self):
        txt = "name: " + self.__name + ", count: " + self.__count + ", loc : " + str(self.__loc)
        return txt

'''