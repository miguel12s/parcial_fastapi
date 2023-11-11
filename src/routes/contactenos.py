from typing import List
from fastapi import APIRouter
from schemas.Notification import Notification, NotificationSend
from controllers.admin_controller import AdminController


admin=APIRouter(prefix='/admin')

new_admin=AdminController()


@admin.post('/create-notification')

def createNotification(contactForm:Notification):
    rpta=new_admin.createNotifiaction(contactForm)  
    return rpta

@admin.get('/get-notifications')

def getNotifications():
    rpta=new_admin.getNotifications()
    return rpta

@admin.get('/get-notifications/{id}')

def getNotifications(id):
    rpta=new_admin.getNotification(id)
    return rpta

@admin.post('/send-response/{id}')

def sendResponse(response:NotificationSend,id:int):
    rpta=new_admin.sendResponse(response,id)
    return rpta

@admin.get('/get-notifications-finish')

def getNotificationsFinish():
    rpta=new_admin.getNotificationsFinish()
    return rpta

@admin.get('/get-notifications-finish/{id}')

def getNotificationFinish(id):
    rpta=new_admin.getNotificationFinish(id)
    return rpta


