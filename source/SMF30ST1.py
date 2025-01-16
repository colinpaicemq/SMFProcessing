''
Process SMF 30 subtype 1 SMF records
'''
#import struct
import  smfobjects as q

def process():
    '''
    main ( and only ) processing
    '''

    subsystem = [q.xu(n="SubsystemType",l=2),  # unsigned integer 
                 q.xu(n="Reserved",l=1),
                 q.xu(n="flags",l=1),
                 q.xu(n="Version",l=1,o=4),
                 q.xs(n="SubsystemName",l=8),   #string converted to ASCII for printable
                 q.xs(n="OpSysLvl",l=8),
                 q.xs(n="SystemName",l=8),
                 q.xs(n="SysplexName",l=8,o=30), # o=30 allows you to check the offsets are correct and you do not have it wrong
    ]

    id_self        = [q.xs(n="Jobname",l=8),
                 q.xs(n="PgmName",l=8),
                 q.xs(n="StepName",l=8),
                 q.xs(n="Userid",l=8),
                 q.xs(n="JESID",l=8),
                 q.xu(n="StepNumber",l=2,o=40),
                 q.xs(n="JobClass",l=1),
                 q.xx(n="Flag",l=1,o=43),
                 q.xu(n="ignored",l=2),
                 q.xu(n="JesPriority",l=2),
                 q.xhun(n="DevAllocTime",l=4),
                 q.SMFTime(n="probProgStartTime"),
                 q.SMFTime(n="InitSelTime",o=56),
                 #q.SMFDate(n="InitSelDate"),
                 q.xu(n="INITSELDATE",l=4),
                 q.SMFTime(n="JobReadTime",o=64),
                 #q.SMFDate(n="JobReadDate"),
                 q.xu(n="JOBREADDATE",l=4),
                 q.SMFTime(n="JobEndTime",o=72),
                 #q.SMFDate(n="JobEndDate"),
                 q.xu(n="JobEndDate",l=4),
                 q.xs(n="ProgName",l=20),
                 q.xs(n="RACFGROUP",l=8),
                 q.xs(n="RACFUserid",l=8,o=108),
                 q.xs(n="RACFTerminid",l=8),
                 q.xu(n="intStartStck",l=8),
                 q.xu(n="intEndStck",l=8),
                 q.xs(n="Unix Program Name",l=16),
                 q.xu(n="ASID",l=4),
                 q.xs(n="Jes Correlator",l=64,o=186),


    ]

    opts = [q.xu(n="RecLen",c="RecordLength",l=2),
            q.xu(n="Seg",c="Segment",l=2,o=2),
            q.xx(n="Flag",c="",l=1),
            q.xu(n="RecordType",c="",l=1),
            q.SMFTime(n="Time",c=""),
            q.SMFDate(n="Date",c=""),
            q.xs(n="SID",c="",l=4),
            q.xs(n="Subsys",c="",l=4),
            q.xu(n="RecordSubType",c="",l=2,o=22),
            q.xtriplet(n="Subsystem",o=24,t=subsystem),
            q.xtriplet(n="Identification",o=32,t=id_self),
            ]
    return opts
