from django.db import models

# Create your models here.
class Pais(models.Model):
    idPais = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idPais')
    Nombre = models.CharField(max_length=45, null=False)  
    ISO = models.CharField(max_length=2, null = False)
    codNumIso = models.IntegerField(blank=True, null=True)
    formDirec = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'Pais'

class Estado(models.Model):
    idEstado = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idEstado')
    Nombre = models.CharField(max_length=25, null=False)  
    ISO = models.CharField(max_length=4,blank=True, null=True) 
    fk_Pais = models.ForeignKey(Pais,on_delete=models.CASCADE, db_column='fk_Pais', verbose_name='País')

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'Estado'

class Mundeleg(models.Model):
    idMunDeleg = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idMunDeleg')
    Nombre = models.CharField(max_length=45, null=False)  
    fk_Estado = models.ForeignKey(Estado,on_delete=models.CASCADE, db_column='fk_Estado', verbose_name='Estado')

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'MunDeleg'

class CP(models.Model): 
    cp = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='cp')
    fk_MpioDel = models.ForeignKey(Mundeleg,on_delete=models.CASCADE, db_column='fk_MpioDel', verbose_name='Municipio')

    def __str__(self):
        return f'{self.cp}'

    class Meta:
        db_table = 'CP'