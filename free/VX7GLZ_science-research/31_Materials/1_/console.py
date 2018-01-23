import xml.etree.ElementTree as ET
fpath = "test2.mm"
# fpath = "test.mm"
# fpath = "copy.mm"
tree = ET.parse(fpath)
root = tree.getroot()

g1 = root[0]
g2 = []
for item in g1 : g2.append(item)

g2

####
g2[0].attrib
for item in g2[0] :
    print(item.tag)
        # icon
        # attribute
        # node
        # node
        # node

### 
g2_0_g3_0 = []

for item in g2[0] :
    g2_0_g3_0.append(item)

g2_0_g3_0[1]    #=> <Element 'attribute' at 0x0000000000C652C8>
g2_0_g3_0[1].tag    #=> 'attribute'
g2_0_g3_0[1].attrib    #=> {'VALUE': '18/01/21', 'NAME': 'created'}

###
import datetime
s = 1516537071171 / 1000.0
# s = 1236472051807 / 1000.0
datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

##########
stamp = "2018-01-21 19:33:54.781000"
data2 = ET.Element("attribute"
                    , {"NAME": "created"
                      , "VALUE" : stamp
                 })
data3 = ET.Element(
            "attribute_layout"
            , {"NAME_WIDTH": 75
              , "VALUE_WIDTH" : 120
                 })
