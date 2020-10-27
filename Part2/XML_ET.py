import xml.etree.ElementTree as ET

xmlString = '''
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>
'''

#########################################
# XML 스트링에서 검색

# XML 스트링을 XDM 트리로 메모리에 로딩
root = ET.fromstring(xmlString)             # tree 전체가 아니라 root element만 가져옴.
print(root.tag, root.attrib, root.text, end='')
print()

for child in root:
    print(child.tag, child.attrib, child.text, end='')
print()

print(root[1][2].text)
print()

for neighbor in root.iter('neighbor'):      # 서브트리 전체에서 모두 검색
    print(neighbor.attrib)
print()

for country in root.findall('country'):     # direct children 에서 모두 검색
    name = country.get('name')              # 속성을 검색
    rank = country.find('rank').text        # direct children 에서 첫번째 노드 검색
    print(name, rank)
print()

#########################################
# XML 스트링을 수정

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')              # 속성을 추가하거나 수정함.

ET.dump(root)
print()

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)                # 엘리먼트를 삭제함.

ET.dump(root)
print()

for country in root.findall('country'):
    capital = ET.Element('capital')         # 자식 엘리먼트를 생성함.
    country.append(capital)                 # 자식 엘리먼트를 추가함.

ET.dump(root)
print()

for country in root.findall('country'):
    ET.SubElement(country, 'population')       # 자식 엘리먼트를 생성하여 추가함.

ET.dump(root)
print()

# XDM 트리를 화일에 출력
tree = ET.ElementTree(root)
tree.write('country.xml')