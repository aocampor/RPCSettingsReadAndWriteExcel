import os, sys
from pandas import DataFrame


if __name__ == "__main__":
    
    print 'test'

    logical = []
    hardware = []
    li0 = []
    lv0 = []
    lvmax = []
    ltrip = []
    lrup = []

    f = open('copy.txt', 'r')
    type = 0

    values = {'i0':-1,'i1':-1,'v0':-1,'v1':-1,'vmax':-1,'trip':-1,'rup':-1,'rbi0':-1,
              'rbi1':-1,'rbv0':-1,'rbv1':-1,'rbvmax':-1,'rbtrip':-1,'rbrup':-1}
    lvalues = {'i0':[],'i1':[],'v0':[],'v1':[],'vmax':[],'trip':[],'rup':[],'rbi0':[],
               'rbi1':[],'rbv0':[],'rbv1':[],'rbvmax':[],'rbtrip':[],'rbrup':[]}

    for line in f:
        line1 = line.rsplit('[')
        if( len( line1 ) > 1):
            if( line1[1] == '\"Channel \"]' ):
                if( type != 0 ):
                    for key in values:
                        if(values[key] != -1):
                            lvalues[key].append(values[key])
                            values[key] = -1
                        else:
                            lvalues[key].append(0)
                type = 1
                line2 = line1[3].rsplit('\"')
                line3 = line1[4].rsplit('\"')
                logical.append( line3[1] )
                hardware.append( line2[1] )
                if( len(line3[1].rsplit('HV')) > 1 ):
                     type = 5
                elif( len(line3[1].rsplit('LBB_LV')) > 1 ):
                     type = 5 
                elif( len(line3[1].rsplit('LV')) > 1 ):
                     type = 3
            else:
                if( len(line1[1].rsplit('settings.i0')) > 1 ):
                    values['i0'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.i0')) > 1 ):
                    values['rbi0'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.i1')) > 1 ):
                    values['i1'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.i1')) > 1 ):
                    values['rbi1'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.v0')) > 1 ):
                    values['v0'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.v0')) > 1 ):
                    values['rbv0'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.v1')) > 1 ):
                    values['v1'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.v1')) > 1 ):
                    values['rbv1'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.vMaxSoftValue')) > 1 ):
                    values['vmax'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.vMaxSoftValue')) > 1 ):
                    values['rbvmax'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.tripTime')) > 1 ):
                    values['trip'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.tripTime')) > 1 ):
                    values['rbtrip'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('settings.rUp')) > 1 ):
                    values['rup'] = line1[2].rsplit(']')[0]
                elif( len(line1[1].rsplit('readBackSettings.rUp')) > 1 ):
                    values['rbrup'] = line1[2].rsplit(']')[0]

    for key in values:
        if(values[key] != -1):
            lvalues[key].append(values[key])
            values[key] = -1
        else:
            lvalues[key].append(0)

    print len(logical), len(hardware)
    for key in lvalues:
        print len(lvalues[key])
          
    f.close()    

    df = DataFrame({'Logical Name': logical, 'Hardware Name': hardware, 
                    'i0': lvalues['i0'], 'rbi0': lvalues['rbi0'], 
                    'i1': lvalues['i1'], 'rbi1': lvalues['rbi1'], 
                    'v0': lvalues['v0'], 'rbv0': lvalues['rbv0'],
                    'v1': lvalues['v1'], 'rbv1': lvalues['rbv1'],
                    'vMaxSoftValue': lvalues['vmax'], 'rbvMaxSoftValue': lvalues['rbvmax'],
                    'tripTime': lvalues['trip'], 'rbtripTime': lvalues['rbtrip'],
                    'rup': lvalues['rup'], 'rbrup': lvalues['rbrup']})
    df.to_excel('test1.xlsx', sheet_name='sheet1',index=False)
