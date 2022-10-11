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

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_kind(self):
        return self.__kind

    def get_m_a(self):
        return self.__m_a

    def get_job(self):
        return self.__job

    def get_departures(self):
        return self.__departures

    def str(self):
        txt = "שם: " + self.__first_name + ",שם משפחה: " + self.__last_name + ", מין: " + self.__kind
        txt += ", מ.א: " + self.__m_a + ", תואר: " + self.__job + ", יציאות: " + self.__departures
        return txt


class Duty:

    def __init__(self, duty_name, count):
        self.__duty_name = duty_name
        self.__count = count

    def get_duty_name(self):
        return self.__duty_name

    def get_count(self):
        return self.__count

    def str(self):
        txt = "name: " + self.__duty_name + ", count: " + self.__count
        return txt

