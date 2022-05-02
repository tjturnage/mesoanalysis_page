#print('hello!')
#dest = open('C:/data/desc.txt', 'w')
#with open('C:/data/PAH_MESO_Remote_V2.txt', 'r', encoding='utf-8-sig') as src:
#    dat = src.readlines()
#    for d in dat:
#        if 'title' in d and 'onfocus' in d:
#            print(d)
#            dest.write(d)

#dest.close()

#sites = ['UIL','OTX','SLE','MFR','BOI','TFX','GGW','RIW','SLC','LKN','REV','OAK','VEF','NKX','FGZ','TUS','GJT','DNR','ABQ','EPZ','DRT','MAF','AMA','OUN','DDC','TOP','LBF','OAX','UNR','ABR','BIS','INL','MPX','GRB','DVN','ILX','SGF','LZK','FWD','CRP','BRO','SHV','LCH','JAN','LIX','APX','DTX','ILN','BNA','BMX','TBW','TAE','FFC','EYW','MFL','JAX','CHS','MHX','GSO','RNK','BUF','PBZ','IAG','WAL','OKX','CHH','ALY','GYX','CAR']
sites = ['ABQ', 'ABR', 'ALY', 'AMA', 'APX', 'BIS', 'BMX', 'BNA', 'BOI', 'BRO', 'BUF', 'CAR', 'CHH', 'CHS', 'CRP', 'DDC', 'DNR', 'DRT', 'DTX', 'DVN', 'EPZ', 'EYW', 'FFC', 'FGZ', 'FWD', 'GGW', 'GJT', 'GRB', 'GSO', 'GYX', 'IAG', 'ILN', 'ILX', 'INL', 'JAN', 'JAX', 'LBF', 'LCH', 'LIX', 'LKN', 'LZK', 'MAF', 'MFL', 'MFR', 'MHX', 'MPX', 'NKX', 'OAK', 'OAX', 'OKX', 'OTX', 'OUN', 'PBZ', 'REV', 'RIW', 'RNK', 'SGF', 'SHV', 'SLC', 'SLE', 'TAE', 'TBW', 'TFX', 'TOP', 'TUS', 'UIL', 'UNR', 'VEF', 'WAL']
#sites.sort()
#print(sites)
#<div class="col-sm-2 image" id="MPX"> MPX </div>
for s in sites:
    line = f'<div class="col-sm-1 image" id="{s}">{s}</div>'
    print(line)