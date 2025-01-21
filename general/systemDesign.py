# System design
# El diseño de sistemas implica planificar y estructurar sistemas escalables y eficientes. Aquí, creamos un diseño básico para un sistema de notificaciones que podría adaptarse para diferentes tipos de mensajes (email, SMS, push notifications).
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass

class EmailNotification(Notification):
    def send(self, message: str, recipient: str) -> None:
        print(f"Sending Email to {recipient}: {message}")

class SMSNotification(Notification):
    def send(self, message: str, recipient: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")

class NotificationService:
    def __init__(self, notification_type: Notification):
        self.notification_type = notification_type

    def notify(self, message: str, recipient: str) -> None:
        self.notification_type.send(message, recipient)

# Usage
email_service = NotificationService(EmailNotification())
email_service.notify("Hello! This is an email.", "user@example.com")
