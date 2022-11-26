from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

def verify_entries(frame):
    for child in frame.findChildren(QtWidgets.QWidget):
        print(child.accessibleName())
        type_ = child.accessibleName()[:child.accessibleName().find(' ')]
        name = child.accessibleName()[child.accessibleName().find(' ') + 1 : ]
        try:
            val = child.text().strip()
        except:
            continue

        test = True
        match type_ :
            case 'id': test = verify_id(val, name)
            case 'text' :test =  verify_text(val, name)
            case 'decimal':test =  verify_decimal(val, name)
            case 'password':test = verify_password(val, name)
            
        if test == False:
            return False
    return True

def verify_id(id, name):
    print(id)
    if id.isnumeric():
        if int(id) <= 0:
            throw_error(f'Please Enter a valid {name}')
            return False
        else:
            return True 
    else:
        print(id)
        print('aw lahne') 
        throw_error(f'Please Enter a valid {name}')
        return False       
    
def verify_text(text, name):
    text = text.strip()
    if text.isalpha() and text != '':
        return True
    else :
        throw_error(f'Please Enter a valid {name}')
        return False
    
def verify_decimal(dec, name):
    dec = dec.replace(',', '.')
    if dec.find('.') != -1:
        if len(dec) - dec.find('.') > 2:
            throw_error(f'Please Enter A Number With Two Digits Only After The Decimal In {name}')
            return False
    for i in dec:
        if not '0' <= dec[i] <= '9' and dec[i] != '.' :
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
    

    

