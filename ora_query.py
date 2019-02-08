import cx_Oracle
from xml.dom import minidom

conn=cx_Oracle.connect('BUDGET2018_TEST2/prostoy2@BDGT')
cursor=conn.cursor()
cursor.execute("select bd.facialacc_cls facailacc_cls,bd.budgetref budget,bd.kvsr kvsr,bd.kfsr kfsr,kcsr.code kcsr,kvr.code kvr,kesr.code kesr,bd.subkesr subkesr,bd.meanstype meanstype,bd.summayear1 summa from budnotify bn join budgetdata bd on  (bn.id=bd.recordindex) join kvr on (bd.kvr=kvr.id) join kcsr on (bd.kcsr=kcsr.id) join kesr on (bd.kesr=kesr.id) where bn.dat is not null and bn.REJECTCLS is null and bd.progindex=32")
#создание xml документа
doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
for (ls,budget,kvsr,kfsr,kcsr,kvr,kesr,subkesr,meanstype,summa) in cursor.fetchall():
    row = doc.createElement('row')
    #лицевой счет
    ls_xml = doc.createElement('facialacc_cls')
    ls_text = doc.createTextNode(str(ls))
    ls_xml.appendChild(ls_text)
    row.appendChild(ls_xml)
    #бюджет
    budget_xml = doc.createElement('budget')
    budget_text = doc.createTextNode(str(budget))
    budget_xml.appendChild(budget_text)
    row.appendChild(budget_xml)
    #КВСР
    kvsr_xml = doc.createElement('kvsr')
    kvsr_text = doc.createTextNode(str(kvsr))
    kvsr_xml.appendChild(kvsr_text)
    row.appendChild(kvsr_xml)
    #КФСР
    kfsr_xml = doc.createElement('kfsr')
    kfsr_text = doc.createTextNode(str(kfsr))
    kfsr_xml.appendChild(kfsr_text)
    row.appendChild(kfsr_xml)
    #КЦСР
    kcsr_xml = doc.createElement('kcsr')
    kcsr_text = doc.createTextNode(str(kcsr))
    kcsr_xml.appendChild(kcsr_text)
    row.appendChild(kcsr_xml)
    #КВР
    kvr_xml = doc.createElement('kvr')
    kvr_text = doc.createTextNode(str(kvr))
    kvr_xml.appendChild(kvr_text)
    row.appendChild(kvr_xml)
    #КЭСР
    kesr_xml = doc.createElement('kesr')
    kesr_text = doc.createTextNode(str(kesr))
    kesr_xml.appendChild(kesr_text)
    row.appendChild(kesr_xml)
    #СубКЭСР
    subkesr_xml = doc.createElement('subkesr')
    subkesr_text = doc.createTextNode(str(subkesr))
    subkesr_xml.appendChild(subkesr_text)
    row.appendChild(subkesr_xml)
    #СубКЭСР
    meanstype_xml = doc.createElement('meanstype')
    meanstype_text = doc.createTextNode(str(meanstype))
    meanstype_xml.appendChild(meanstype_text)
    row.appendChild(meanstype_xml)
    #Сумма
    summa_xml = doc.createElement('summa')
    summa_text = doc.createTextNode(str(summa))
    summa_xml.appendChild(summa_text)
    row.appendChild(summa_xml)
    root.appendChild(row)

xml_str = doc.toprettyxml(indent="  ")
with open("budgetdata.xml", "w") as file:
    file.write(xml_str)
#закрываем соединение
conn.close()

