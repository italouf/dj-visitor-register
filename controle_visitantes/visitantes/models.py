from django.db import models

class Visitante(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO","Aguardando autorização"),
        ("EM_VISITA","Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]

    status = models.CharField(
        max_length=10,
        verbose_name = "Status",
        choices=STATUS_VISITANTE,
        default="AGUARDANDO",
        )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=128,)

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now_add=False,
        auto_now = False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name = "Numero da Casa",
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do Veículo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horario de entrada na portaria",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horario de saída na portaria",
        auto_now_add=False,
        blank=True,
        null=True,
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horario de autorização de entrada",
        auto_now = False,
        blank = True,
        null= True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Morador responsável pela autorização",
        max_length=128,
        blank=True,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete= models.PROTECT,
        )
    
    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return "Horário de saída não registrado"
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
        return "Visitante aguardando autorização"
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
        return "Veículo não registrado"

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
    
    def __str__(self):
        return self.nome_completo