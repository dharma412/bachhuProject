from selenium.webdriver.support.select import Select
def selectByIndex(elementDdl,index):
    elementSelect=Select(elementDdl)
    elementSelect.select_by_index(index)
def selectByVisibleText(elementDdl,text):
    elementSelect=Select(elementDdl)
    elementSelect.select_by_visible_text(text)
def selectByvalue(elementDdl,value):
    elementSelect=Select(elementDdl)
    elementSelect.select_by_value(value)
def deSelectByIndex(elementDdl,index):
    elementSelect=Select(elementDdl)
    elementSelect.deselect_by_index(index)
def deSelectByVisibleText(elementDdl,text):
    elementSelect=Select(elementDdl)
    elementSelect.deselect_by_visible_text(text)
def deSelectByValue(elementDdl,value):
    elementSelect=Select(elementDdl)
    elementSelect.deselect_by_value(value)
def deSelectAllOption(elementDdl):
    elementSelect=Select(elementDdl)
    elementSelect.deselect_all()

