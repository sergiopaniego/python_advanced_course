from django.utils import timezone

# Ver la zona horaria actual
print("Current time zone:", timezone.get_current_timezone_name())

# Crear una marca de tiempo actual y ver cómo se muestra
current_time = timezone.now()
print("Current time with timezone:", current_time)
