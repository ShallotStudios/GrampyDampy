import pygame

pygame.joystick.init()
controllers = []

if pygame.joystick.get_count() != 0 :
    for cont in range(pygame.joystick.get_count()) :
        controllers.append( pygame.joystick.Joystick(cont) )
        controllers[cont].init()

focus = -1
if len(controllers) > 0 :
    focus = 0

#GENERIC HAT
def getHat() :
    if focus != -1 :
        return controllers[focus].get_hat(0)
    return

#AXISES
def getAxis0() :
    if focus != -1 :
        return controllers[focus].get_axis(0)
def getAxis1() :
    if focus != -1 :
        return controllers[focus].get_axis(1)
    return
def getAxis2() :
    if focus != -1 :
        return controllers[focus].get_axis(2)
    return
def getAxis3() :
    if focus != -1 :
        return controllers[focus].get_axis(3)
    return
def getAxis4() :
    if focus != -1 :
        return controllers[focus].get_axis(4)
    return

#BUTTONS
def getButton(i) :
    f = False
    for cont in range(len(controllers)) :
        if controllers[cont].get_button(i) :
            f = True
            focus = cont
            break
    return f
def getButton0() : #A Button
    if focus != -1 :
        return getButton(0)
    return
def getButton1() : #B Button
    if focus != -1 :
        return getButton(1)
    return
def getButton2() : #X Button
    if focus != -1 :
        return getButton(2)
    return
def getButton3() : #Y Button
    if focus != -1 :
        return getButton(3)
    return
def getButton4() : #LB Button
    if focus != -1 :
        return getButton(4)
    return
def getButton5() : #RB Button
    if focus != -1 :
        return getButton(5)
    return
def getButton6() : #SELECT
    if focus != -1 :
        return getButton(6)
    return
def getButton7() : #START
    if focus != -1 :
        return getButton(7)
    return
def getButton8() : #LEFT AXIS BUTTON
    if focus != -1 :
        return getButton(8)
    return
def getButton9() : #RIGHT AXIS BUTTON
    if focus != -1 :
        return getButton(9)
    return
