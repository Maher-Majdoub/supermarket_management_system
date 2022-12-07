from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

def verify_entries(frame):
    for child in frame.findChildren(QtWidgets.QWidget):
        type_ = child.accessibleName()[:child.accessibleName().find(' ')]
        name = child.accessibleName()[child.accessibleName().find(' ') + 1 : ]
        try:
            val = child.text().strip()
        except:
            continue

        test = True
        match type_ :
            case 'integer': test = verify_integer(val, name)
            case 'text' :test =  verify_text(val, name)
            case 'decimal':test =  verify_decimal(val, name)
            case 'password':test = verify_password(val, name)
            
        if test == False:
            return False
    return True

def verify_integer(i, name):
    if i == '': 
        throw_error(f'Please Enter a {name})')
        return False
    if i.isnumeric():
        if int(i) <= 0:
            throw_error(f'Please Enter a valid {name}')
            return False
        else:
            return True 
    else:
        throw_error(f'Please Enter a valid {name}')
        return False       
    
def verify_text(text, name):
    text = text.strip()
    if text != '':
        for i in text:
            if not 'A' <= i.upper() <= 'Z' or i in [' ', '-', '_'] or '0' <= i <= '9':
                return False
        return True
    else :
        throw_error(f'Please Enter a valid {name}')
        return False
    
def verify_decimal(dec, name):
    if dec == '': 
        throw_error(f'Please Enter a {name}')
        return False
    dec = dec.replace(',', '.')
    if dec.find('.') != -1:
        if len(dec)-1 - dec.find('.') > 2:
            throw_error(f'Please Enter A Number With Two Digits Only After The Decimal In {name}')
            return False
    for i in dec:
        if not '0' <= i <= '9' and i != '.' :
            throw_error(f'Please Enter a valid {name}')
            return False
    return True
    
def verify_password(pwd, name):
    if len(pwd) < 6:
        throw_error(f'The {name} must contains at least 6 characters')
        return False
    return True 


def throw_error(message):
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle('Warning')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def throw_quetion(title ,message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    r = msg.exec_()   
    return r

def throw_info(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(' ')
    msg.setText(message)
    msg.exec_()
    

    

