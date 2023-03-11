from vet_sys.models_abstracts import TemNome, Descritivel, ModeloBase


class Especie(TemNome, Descritivel, ModeloBase):

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"

    def __str__(self):
        return self.nome
