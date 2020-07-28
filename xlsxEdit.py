# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/27 8:04 下午
@Describe 

"""
import time

import pandas
import xlrd #读
import xlwt #写

class xlsxEdit():
    def __init__(self,data):
        self.filename = 'myxlsx.xls'
        # 需写入文件的数据
        self.data = data
        # 得到写入完毕的文件
        self.workbook = self.get_xls()


    def write(self):
        # {item1:{},item2:{},,,}
        row,col = 0,0
        for item in self.data:
            # 设置单元格宽度
            self.worksheet.col(0).width = 4444
            self.worksheet.col(1).width = 33333
            # 为单元格设置背景色
            pattern = xlwt.Pattern()  # Create the Pattern
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
            pattern.pattern_fore_colour = 5  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
            style = xlwt.XFStyle()  # Create the Pattern
            style.pattern = pattern  # Add Pattern to Style

            # 参数对应 行, 列, 值
            self.worksheet.write(row, col, item, style)
            for i in self.data[item]:
                row += 1
                self.worksheet.write(row, col, label=i)
                self.worksheet.write(row, col+1, label=str(self.data[item][i]))
            row+=1




    def get_xls(self):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        self.worksheet = workbook.add_sheet('My Worksheet')
        # 写入
        self.write()
        # 保存
        workbook.save(self.filename)
        print('[{}]xls file already got!'.format(time.strftime('%Y-%m-%d %H:%M:%S')))

        return self.filename