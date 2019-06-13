import Model
import View

class controller:

	def __init__ (self, model, view):
		self.model=model
		self.view=view



		while (model.Jeu_en_cours):
			model.jouer()
			view.rafraichir(model)


model=Model.Plateau(1)
view=View.Plateau(model)
controller=controller(model, view)
