from selenium.webdriver import ActionChains


def moveToElement(element,browser):
    actionClass=ActionChains(browser)
    actionClass.move_to_element(element).perform()
def contextClick(element,browser):
    actionClass = ActionChains(browser)
    actionClass.context_click(element).perform()
def doubleClick(element,browser):
    actionClass = ActionChains(browser)
    actionClass.double_click(element).perform()
def dragAndDrop(browser,src,targat):
    actionClass = ActionChains(browser)
    actionClass.drag_and_drop(src,targat).perform()

