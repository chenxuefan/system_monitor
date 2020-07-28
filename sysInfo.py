# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/27 7:14 下午
@Describe 
获取系统信息：
1、cpu
2、memory
3、disk
4、net
5、pid
6、sensors

"""
import psutil

class sysInfo():
    def __init__(self):
        self.user = 'billie'
        self.cpu = self.get_cpu()
        self.memory = self.get_memory()
        self.disk = self.get_disk()
        self.net = self.get_net()
        self.pid = self.get_pid()
        self.sensors = self.get_sensors()
        self.others = self.get_others()
        self.allInfo = {'cpu':self.cpu,
                        'memory':self.memory,
                        'disk':self.disk,
                        'net':self.net,
                        'pid':self.pid,
                        'sensors':self.sensors,
                        'othors':self.others
                        }


    def get_cpu(self):
        cpu_dic = dict()
        cpu_dic['cpu_count']=psutil.cpu_count()
        cpu_dic['cpu_percent']=psutil.cpu_percent()
        cpu_dic['cpu_times']=psutil.cpu_times()
        cpu_dic['cpu_times_percent']=psutil.cpu_times_percent()
        cpu_dic['cpu_stats']=psutil.cpu_stats()
        cpu_dic['cpu_freq']=psutil.cpu_freq()
        return cpu_dic

    def get_memory(self):
        memory_dict = dict()
        memory_dict['virtual_memory']=psutil.virtual_memory()
        memory_dict['swap_memory']=psutil.swap_memory()
        return memory_dict

    def get_disk(self):
        disk_dict = dict()
        disk_dict['disk_io_counters']=psutil.disk_io_counters()
        disk_dict['disk_partitions']=psutil.disk_partitions()
        disk_dict['disk_usage']=psutil.disk_usage('/')
        return disk_dict

    def get_net(self):
        net_dict = dict()
        net_dict['net_if_addrs']=psutil.net_if_addrs()
        net_dict['net_if_stats']=psutil.net_if_stats()
        return net_dict

    def get_pid(self):
        pid_dict = dict()
        pid_dict['pids']=psutil.pids()
        return pid_dict

    def get_sensors(self):
        sensors_dict = dict()
        # sensors_dict['sensors_temperatures']=psutil.sensors_temperatures(fahrenheit=False)
        # sensors_dict['sensors_fans']=psutil.sensors_fans()
        # sensors_dict['sensors_battery']=psutil.sensors_battery()
        return sensors_dict
    def get_others(self):
        others_dict = dict()
        others_dict['users'] = psutil.users()
        others_dict['boot_time'] = psutil.boot_time()
        return others_dict
