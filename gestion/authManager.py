from django.contrib.auth.models import BaseUserManager



class UsuarioManager(BaseUserManager):

    def create_superuser(self,nombre,correo,apellido,tipoUsuario,password):

        if not correo:
            raise ValueError('El usuario debe indicar obligatoriamente el correo')
        correoNormalizado = self.normalize_email(correo)
        nuevoUsuario=self.model(correo=correoNormalizado,nombre=nombre,apellido=apellido,tipoUsuario=tipoUsuario)

        nuevoUsuario.set_password(password)

        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True

        nuevoUsuario.save(using=self._db)