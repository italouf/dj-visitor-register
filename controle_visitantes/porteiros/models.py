from django.db import models

class Porteiro(models.Model):

    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.PROTECT
    )
    
    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=128,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone para contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now_add=False,
        auto_now=False,
    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"
    
    def __str__(self):
        return self.nome_completo