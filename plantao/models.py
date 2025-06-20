from django.db import models

class Plantao(models.Model):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    nome_medico = models.CharField(default='Liamara Correa', max_length=100)

    def horas_trabalhadas(self):
        return abs(self.hora_fim.hour - self.hora_inicio.hour)

    def turno(self):
        return "dia" if self.hora_inicio.hour < 19 else "noite"

    def is_dia_util(self):
        return self.data.weekday() < 5 

    def categoria(self):
        if self.is_dia_util():
            return 1 if self.turno() == "dia" else 2
        else:
            return 3 if self.turno() == "dia" else 4

    def __str__(self):
        return f"Plantão do/a {self.nome_medico} em {self.data.strftime('%d/%m/%Y')} - {self.hora_inicio} às {self.hora_fim}"