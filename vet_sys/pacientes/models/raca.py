from vet_sys.models_abstracts import TemNome, Descritivel, ModeloBase


class Raca(TemNome, Descritivel, ModeloBase):

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"

    def __str__(self):
        return self.nome
