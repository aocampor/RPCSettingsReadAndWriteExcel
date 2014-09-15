import os,sys
from pandas import *

if __name__ == "__main__":

    xl = pandas.ExcelFile('RPCDCS_FSM_postinstallation_settings.xlsx')
    df = xl.parse('1')
    for index, row in df.iterrows():
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.i0\", ' + str(row['i0']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.i0\", ' + str(row['i0']) + ');'
        #print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.i1\", ' + str(row['i0']) + ');'
        print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.i1\", ' + str(row['i1']) + ');'
        print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.rUp\", ' + str(row['rUp']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.rUp\", ' + str(row['rUp']) + ');'
        #print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.rDwn\", ' + str(row['rDw']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.rDwn\", ' + str(row['rDw']) + ');'
        #print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.tripTime\", ' + str(row['tripTime']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.tripTime\", ' + str(row['tripTime']) + ');'
        #print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.v0\", ' + str(row['v0']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.v0\", ' + str(row['v0']) + ');'
        #print temp
        temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.vMaxSoftValue\", ' + str(row['vMaxSoftValue']) + ');'
        print temp
        #temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.vMaxSoftValue\", ' + str(row['vmax']) + ');'
        #print temp
    xl1 = pandas.ExcelFile('test1.xlsx')
    df1 = xl1.parse('sheet1')
    for index1, row1 in df1.iterrows():
        for index, row in df.iterrows():
            if( row1['Logical Name'] == row['Logical Name']):
                temp = 'dpSet(\"' + str(row['Hardware Name']) + '.settings.v1\", ' + str(row1['v1']) + ');'
                print temp
                temp = 'dpSet(\"' + str(row['Hardware Name']) + '.readBackSettings.v1\", ' + str(row1['rbv1']) + ');'
                print temp
