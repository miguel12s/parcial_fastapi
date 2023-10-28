from fastapi import APIRouter
from models.Notification import Notification
from controllers.admin_controller import AdminController


admin=APIRouter(prefix='/admin')

new_admin=AdminController()


@admin.post('/create-notification')

def createNotification(contactForm:Notification):
    rpta=new_admin.createNotifiaction(contactForm)  
    return rpta

