from selenium import webdriver
import sys
import time
from translatingText import translating
from export import exporting_to_file

# Reading the website, argument, language from the parameter file
# def reading_parm_file():

# Entering parm via console checking.


def check_arg():
    if len(sys.argv) > 1:
        argument = ' '.join(sys.argv[1:])
        return argument
    else:
        print('No input argument. Exiting...')
        exit()


# Starting Selenium process.
def invoke_web(parm):
    browser = webdriver.Firefox()
    browser.get('https://www.ica.se/recept')

    searchEle = browser.find_element_by_id('search2')
    searchEle.send_keys(parm)
    searchEle.submit()
    time.sleep(2)

    recipeEle = browser.find_element_by_link_text(parm)
    browser.execute_script("arguments[0].click();", recipeEle)
    # recipeEle.click()
    time.sleep(5)

    cookingStepList = browser.find_elements_by_class_name(
        'cooking-step__content__instruction')
    ingredientsList = browser.find_elements_by_class_name(
        'ingredients__list__item')

    cookingStepText = list()
    ingredientsText = list()

    for steps in cookingStepList:
        cookingStepText.append(steps.text)

    for items in ingredientsList:
        ingredientsText.append(items.text)

    # translating part
    translatedSteps = translating(cookingStepText)
    translatedItems = translating(ingredientsText)

    return translatedItems, translatedSteps


if __name__ == "__main__":
    parm = check_arg()
    # items, steps = invoke_web(parm)
    exporting_to_file(parm, items, steps)

exit()