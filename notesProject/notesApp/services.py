from django.db import transaction
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from .models import Notes

def update_note(note_id, user, titulo, contenido, client_updated_at):
    with transaction.atomic():
        note = Notes.objects.select_for_update().get(id=note_id, user=user)
        if note.updated_at != client_updated_at:
            raise ValidationError("La nota fue modificada por otra instancia. Por favor, actualiza y revisa los cambios.")
        note.titulo = titulo
        note.contenido = contenido
        note.updated_at = now()
        note.save()
