from pathlib import Path
import os


def exporting_to_file(name, ingredients, steps):
    recipeFile = '..\\recipes\\' + name + '.txt'
    osCommandString = "notepad.exe " + recipeFile

    if Path(recipeFile).is_file():
        print('file exist')
        os.system(osCommandString)
    else:
        with open(recipeFile, 'wt', encoding='utf-8') as newFile:
            print('New recipe file has been created and filled with the data')
            newFile.write('Ingredients:'+'\n')
            newFile.write('\n'.join(items for items in ingredients))
            newFile.write('\n')
            newFile.write('Cooking Steps:'+'\n')
            newFile.write('\n'.join(step for step in steps))
            newFile.write('\n')

    os.system(osCommandString)

def validating_file(name):
    


