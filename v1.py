from collections import defaultdict
import pybgpstream

stream = pybgpstream.BGPStream(
    # Consider this time interval:
    # Sat, 01 Aug 2015 7:50:00 GMT -  08:10:00 GMT
    from_time="2017-08-01 07:50:00", until_time="2017-08-01 08:50:00",
    collectors=["route-views.sg"],
    record_type="ribs",
    )

dico = {}
#dico = defaultdict()

for rec in stream.records():
    for elem in rec :
        pfx = elem.fields["prefix"]
        # Get the list of ASes in the AS path
        ases = elem.fields["as-path"].split(" ")
       # print(pfx, ",", ases)
       # dico[pfx].add(ases)
    
        if(pfx in dico):
           dico[pfx].append(ases)
           
        else :
            dico[pfx]=[ases]
print(dico)
        
#for pfx in dico:
 #   print((pfx, ",".join(dico[pfx])))
    